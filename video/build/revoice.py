"""Переозвучка готового ролика без исходников (клипов, оверлеев, музыки).
Тайминг сцен берётся из старого .srt: каждая сцена готового видео растягивается под длину новой озвучки
(резы проходят по середине существующих кроссфейдов), звук собирается заново:
голос vo/eleven_s*.wav + музыка music.mp3 + саунд-дизайн из sound.json (файлы sfx/, см. sound.py).
Запуск из рабочей папки:
  python3 revoice.py OLD.mp4 OLD.srt --plan          # только timeline.json (нужен sound.py)
  python3 revoice.py OLD.mp4 OLD.srt OUT.mp4 OUT.srt  # рендер"""
import json, os, re, subprocess, sys
SRC, SRT = sys.argv[1:3]
PLAN = sys.argv[3] == '--plan'
VOICE = 'eleven'; XF = 0.4; LEAD = 0.3; TAIL = 0.7
HERE = os.path.dirname(__file__)

def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))

def sec(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

def stamp(t):
    ms = round(t * 1000); return f'{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}'

blocks = [b for b in open(SRT, encoding='utf-8').read().strip().split('\n\n')]
subs = []
for b in blocks:
    lines = b.split('\n'); t = re.findall(r'(\d+):(\d+):(\d+),(\d+)', lines[1])
    subs.append((sec(*t[0]), sec(*t[1])))
n = len(subs); total_old = dur(SRC)
offs = [s - LEAD for s, _ in subs]                             # начало каждой части в старом ролике
cuts = [0.0] + [o + XF / 2 for o in offs[1:]] + [total_old]    # резы по середине кроссфейдов
old_d = [max(LEAD + (e - s) + TAIL, 4.0) + (2.5 if i == n - 1 else 0) for i, (s, e) in enumerate(subs)]
vo = [f'vo/{VOICE}_s{i + 1}.wav' for i in range(n)]
new_d = [max(LEAD + dur(v) + TAIL, 4.0) + (2.5 if i == n - 1 else 0) for i, v in enumerate(vo)]
k = [nd / od for nd, od in zip(new_d, old_d)]
text = [re.sub(r'\[[a-z ]+\]\s*', '', s['vo']) for s in json.load(open(os.path.join(HERE, '..', 'scenes.json')))['scenes']]

fc = ''; pos = 0.0; starts = []; scene_at = []; srt = []
for i in range(n):
    a, b = cuts[i], cuts[i + 1]
    fc += f'[0:v]trim={a:.3f}:{b:.3f},setpts=(PTS-STARTPTS)*{k[i]:.4f},fps=30[v{i}];'
    vs = pos + (offs[i] + LEAD - a) * k[i]                     # где в новом ролике начинается фраза
    scene_at.append(pos); starts.append(vs)
    srt.append(f'{i + 1}\n{stamp(vs)} --> {stamp(vs + dur(vo[i]))}\n{text[i]}\n')
    pos += (b - a) * k[i]
total = pos
scene_len = [b - a for a, b in zip(scene_at, scene_at[1:] + [total])]
json.dump({'total': total, 'scene_start': scene_at, 'scene_len': scene_len, 'vo_start': starts},
          open('timeline.json', 'w'), indent=1)
if PLAN:
    print('timeline.json', round(total, 2)); sys.exit()
OUT, OUT_SRT = sys.argv[3:5]

inputs = ['-i', SRC] + sum((['-i', v] for v in vo), []) + ['-i', 'music.mp3']
fc += ''.join(f'[v{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0,format=yuv420p[vout];'
for i in range(n):
    ms = int(starts[i] * 1000); fc += f'[{i + 1}:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={ms}|{ms}[a{i}];'
fc += ''.join(f'[a{i}]' for i in range(n)) + f'amix=inputs={n}:normalize=0,apad,atrim=0:{total:.3f}[voice];'
fc += (f'[{n + 1}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=0.3,afade=in:d=0.8,'
       f'afade=out:st={total - 2.5:.3f}:d=2.5,apad,atrim=0:{total:.3f}[mus];')

# саунд-дизайн: эмбиенты сцен, акценты, вжухи на резах
fx = []
def add(path, at, vol, length=None, fade=0.0):
    idx = len(inputs) // 2; inputs.extend(['-i', path]); at = max(0.0, at); ms = int(at * 1000)
    f = f'[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={vol}'
    if length:
        f += f',atrim=0:{length:.3f},afade=in:d={fade}' + f',afade=out:st={max(0, length - fade):.3f}:d={fade}'
    fc_parts.append(f + f',adelay={ms}|{ms}[fx{len(fx)}];'); fx.append(f'[fx{len(fx)}]')
fc_parts = []
if os.path.exists(os.path.join(HERE, '..', 'sound.json')) and os.path.isdir('sfx'):
    sd = json.load(open(os.path.join(HERE, '..', 'sound.json')))
    for i, s in enumerate(sd['scenes']):
        t0, ln = scene_at[i], scene_len[i]
        add(f'sfx/amb_s{s["id"]}.mp3', t0 - 0.3, s['ambience']['volume'], ln + 0.6, 0.6)
        for j, a in enumerate(s['accents']):
            add(f'sfx/acc_s{s["id"]}_{j}.mp3', t0 + (a['at'] if a['at'] >= 0 else ln + a['at']), a['volume'])
        if i:
            tr = sd['transition']; add(f'sfx/whoosh_{i % 2}.mp3', t0 - tr['duration'] / 2, tr['volume'])
fc += ''.join(fc_parts)
if fx:
    fc += ''.join(fx) + f'amix=inputs={len(fx)}:normalize=0,apad,atrim=0:{total:.3f}[sfx];[mus][sfx]amix=inputs=2:normalize=0[bed];'
else:
    fc += '[mus]anull[bed];'
fc += ('[voice]asplit[vx][sc];[bed][sc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400[duck];'
       '[vx][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[aout]')
cmd = ['ffmpeg', '-v', 'error', '-y'] + inputs + [
       '-filter_complex', fc, '-map', '[vout]', '-map', '[aout]', '-t', f'{total:.3f}',
       '-c:v', 'libx264', '-preset', 'slow', '-crf', '20', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
       '-movflags', '+faststart', OUT]
subprocess.run(cmd, check=True)
open(OUT_SRT, 'w', encoding='utf-8').write('\n'.join(srt))
print('scenes', [round(x, 2) for x in k], 'fx', len(fx), 'total', round(total, 2))

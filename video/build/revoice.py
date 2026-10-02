"""Переозвучка готового ролика без исходников (клипов, оверлеев, музыки).
Тайминг сцен берётся из старого .srt: каждая сцена готового видео растягивается под длину новой озвучки
(резы проходят по середине существующих кроссфейдов), сверху кладутся vo/eleven_s*.wav и music.mp3.
Запуск из рабочей папки:  python3 revoice.py OLD.mp4 OLD.srt OUT.mp4 OUT.srt"""
import re, subprocess, sys
SRC, SRT, OUT, OUT_SRT = sys.argv[1:5]
VOICE = 'eleven'; XF = 0.4; LEAD = 0.3; TAIL = 0.7

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
    subs.append((sec(*t[0]), sec(*t[1]), '\n'.join(lines[2:])))
n = len(subs); total_old = dur(SRC)
offs = [s - LEAD for s, _, _ in subs]                          # начало каждой части в старом ролике
cuts = [0.0] + [o + XF / 2 for o in offs[1:]] + [total_old]    # резы по середине кроссфейдов
old_d = [max(LEAD + (e - s) + TAIL, 4.0) + (2.5 if i == n - 1 else 0) for i, (s, e, _) in enumerate(subs)]
vo = [f'vo/{VOICE}_s{i + 1}.wav' for i in range(n)]
new_d = [max(LEAD + dur(v) + TAIL, 4.0) + (2.5 if i == n - 1 else 0) for i, v in enumerate(vo)]
k = [nd / od for nd, od in zip(new_d, old_d)]

fc = ''; pos = 0.0; starts = []; srt = []
for i in range(n):
    a, b = cuts[i], cuts[i + 1]
    fc += f'[0:v]trim={a:.3f}:{b:.3f},setpts=(PTS-STARTPTS)*{k[i]:.4f},fps=30[v{i}];'
    vs = pos + (offs[i] + LEAD - a) * k[i]                     # где в новом ролике начинается фраза
    starts.append(vs); srt.append(f'{i + 1}\n{stamp(vs)} --> {stamp(vs + dur(vo[i]))}\n{subs[i][2]}\n')
    pos += (b - a) * k[i]
total = pos
fc += ''.join(f'[v{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0,format=yuv420p[vout];'
for i in range(n):
    ms = int(starts[i] * 1000); fc += f'[{i + 1}:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={ms}|{ms}[a{i}];'
fc += ''.join(f'[a{i}]' for i in range(n)) + f'amix=inputs={n}:normalize=0,apad,atrim=0:{total:.3f}[voice];'
fc += (f'[{n + 1}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=0.25,afade=in:d=1.5,'
       f'afade=out:st={total - 2.5:.3f}:d=2.5,apad,atrim=0:{total:.3f}[mus];'
       '[voice]asplit[vx][sc];[mus][sc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400[duck];'
       '[vx][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[aout]')
cmd = ['ffmpeg', '-v', 'error', '-y', '-i', SRC] + sum((['-i', v] for v in vo), []) + ['-i', 'music.mp3',
       '-filter_complex', fc, '-map', '[vout]', '-map', '[aout]', '-t', f'{total:.3f}',
       '-c:v', 'libx264', '-preset', 'slow', '-crf', '20', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
       '-movflags', '+faststart', OUT]
subprocess.run(cmd, check=True)
open(OUT_SRT, 'w', encoding='utf-8').write('\n'.join(srt))
print('scenes', [round(x, 2) for x in k], 'total', round(total, 2))

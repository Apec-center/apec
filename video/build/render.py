"""Монтаж: каждая сцена рендерится отдельной частью, затем части склеиваются с кроссфейдами,
поверх — музыка. Запуск из рабочей папки с clips/ (hd/c*.mp4), overlays/, vo/, music.mp3."""
import json, subprocess, sys, os
SC = sys.argv[1] if len(sys.argv) > 1 else '/home/user/apec/video/scenes.json'
VOICE = os.environ.get('VOICE', 'dmitri')
OUT = os.environ.get('OUT', 'apec_final.mp4')
XF = 0.4; LEAD = 0.3; TAIL = 0.7

def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))

def run(cmd):
    subprocess.run(cmd, check=True)

S = json.load(open(SC))['scenes']
os.makedirs('parts', exist_ok=True)
lens = []
for s in S:
    i = s['id']; vo = f'vo/{VOICE}_s{i}.wav'
    d = max(LEAD + dur(vo) + TAIL, 4.0) + (2.5 if i == len(S) else 0)
    clip = f'hd/c{i}.mp4'; cd = dur(clip)
    k = max(1.0, d / cd)  # замедляем клип, если сцена длиннее 8 секунд
    st = 0.0 if i == 1 else 0.3  # хук: инфографика видна с первого кадра
    ypos = "0" if not st else f"'if(lt(t,{st}),40,max(0,40-(t-{st})*80))'"
    fc = (f"[0:v]setpts={k:.4f}*PTS,trim=0:{d:.3f},setpts=PTS-STARTPTS,scale=1080:1920,fps=30,format=yuv420p[bg];"
          + (f"[1:v]format=rgba,fade=in:st={st}:d=0.5:alpha=1[ov];" if st else "[1:v]format=rgba[ov];") +
          f"[bg][ov]overlay=x=0:y={ypos}:eval=frame[v];"
          f"[0:a]atempo={1/k:.4f},volume=0.06,atrim=0:{d:.3f}[amb];"
          f"[2:a]adelay={int(LEAD*1000)}|{int(LEAD*1000)},volume=1.6[vo];"
          f"[amb][vo]amix=inputs=2:duration=first:normalize=0,apad,atrim=0:{d:.3f},aformat=sample_rates=48000:channel_layouts=stereo[a]")
    run(['ffmpeg', '-v', 'error', '-y', '-i', clip, '-loop', '1', '-t', f'{d:.3f}', '-i', f'overlays/o{i}.png', '-i', vo,
         '-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-t', f'{d:.3f}',
         '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-c:a', 'aac', '-b:a', '192k', f'parts/part{i:02d}.mp4'])
    lens.append(d); print('part', i, round(d, 2))

# склейка частей
inp = []; fc = ''; off = 0; pv = '0:v'; pa = '0:a'
for i, s in enumerate(S):
    inp += ['-i', f'parts/part{s["id"]:02d}.mp4']
for i in range(1, len(S)):
    off += lens[i - 1] - XF
    fc += f"[{pv}][{i}:v]xfade=transition=fade:duration={XF}:offset={off:.3f}[v{i}];"
    fc += f"[{pa}][{i}:a]acrossfade=d={XF}[a{i}];"
    pv, pa = f'v{i}', f'a{i}'
total = sum(lens) - XF * (len(S) - 1)
fc += (f"[{len(S)}:a]volume=0.22,afade=in:d=1.5,afade=out:st={total-2.5:.3f}:d=2.5,atrim=0:{total:.3f}[m];"
       f"[{pa}][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[aout]")
run(['ffmpeg', '-v', 'error', '-y', *inp, '-i', 'music.mp3', '-filter_complex', fc, '-map', f'[{pv}]', '-map', '[aout]',
     '-c:v', 'libx264', '-preset', 'slow', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
     '-movflags', '+faststart', OUT])
print('total', round(total, 2), OUT)

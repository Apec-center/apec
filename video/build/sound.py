"""Музыка и саунд-дизайн через ElevenLabs по sound.json и timeline.json (см. revoice.py --plan).
Музыка пишется по композиционному плану: разделы совпадают со сценами ролика.
Готовые файлы не перегенерируются; FORCE=1 — сгенерировать всё заново, ONLY=music|sfx — только часть.
Запуск из рабочей папки:  python3 sound.py  →  sfx/*.mp3, music.mp3"""
import json, os, sys, urllib.request

KEY = os.environ['ELEVENLABS_API_KEY']; API = 'https://api.elevenlabs.io/v1'
FORCE = os.environ.get('FORCE') == '1'; ONLY = os.environ.get('ONLY')
SD = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'sound.json')))
TL = json.load(open('timeline.json'))
os.makedirs('sfx', exist_ok=True)

def post(path, body, out, timeout=300):
    if os.path.exists(out) and not FORCE:
        return
    req = urllib.request.Request(f'{API}{path}?output_format=mp3_44100_192', data=json.dumps(body).encode(),
                                 headers={'xi-api-key': KEY, 'Content-Type': 'application/json'})
    open(out, 'wb').write(urllib.request.urlopen(req, timeout=timeout).read()); print(out, file=sys.stderr)

def sfx(prompt, seconds, out, loop=False):
    post('/sound-generation', {'text': prompt, 'duration_seconds': round(min(max(seconds, 0.5), 30), 1),
                               'prompt_influence': 0.5, 'loop': loop, 'model_id': 'eleven_text_to_sound_v2'}, out)

if ONLY != 'music':
    tr = SD['transition']
    for v in range(2):
        sfx(tr['prompt'], tr['duration'], f'sfx/whoosh_{v}.mp3')
    for i, s in enumerate(SD['scenes']):
        sfx(s['ambience']['prompt'], TL['scene_len'][i] + 1.0, f'sfx/amb_s{s["id"]}.mp3', loop=True)
        for j, a in enumerate(s['accents']):
            sfx(a['prompt'], a['duration'], f'sfx/acc_s{s["id"]}_{j}.mp3')

if ONLY != 'sfx':
    m = SD['music']; secs = []
    for sec in m['sections']:
        ms = int(sum(TL['scene_len'][i - 1] for i in sec['scenes']) * 1000)
        secs.append({'section_name': sec['name'], 'positive_local_styles': sec['styles'], 'negative_local_styles': [],
                     'duration_ms': ms, 'lines': []})
    secs[-1]['duration_ms'] += 2000  # хвост под затухание
    post('/music', {'composition_plan': {'positive_global_styles': m['global'], 'negative_global_styles': m['negative'],
                                         'sections': secs}, 'model_id': 'music_v1'}, 'music.mp3', timeout=600)

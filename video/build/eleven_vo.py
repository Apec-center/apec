"""Озвучка напрямую через API ElevenLabs.
Нужна переменная окружения ELEVENLABS_API_KEY; необязательно ELEVENLABS_VOICE_ID и ELEVENLABS_MODEL.
Модель по умолчанию eleven_v3: живая интонация и теги эмоций в тексте ([warmly], [excited] …).
Для eleven_multilingual_v2 теги вырезаются.
Запуск из рабочей папки:  python3 eleven_vo.py  →  затем  VOICE=eleven python3 render.py"""
import json, os, re, subprocess, sys, urllib.request

KEY = os.environ['ELEVENLABS_API_KEY']
VOICE_ID = os.environ.get('ELEVENLABS_VOICE_ID', '3EuKHIEZbSzrHGNmdYsx')  # Nikolay (библиотека ElevenLabs, ru), если голос не задан
MODEL = os.environ.get('ELEVENLABS_MODEL', 'eleven_v3')
V3 = MODEL == 'eleven_v3'
S = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'scenes.json')))['scenes']
os.makedirs('vo', exist_ok=True)

def spoken(t):  # латиница в русской речи читается по буквам — даём произношение
    t = t.replace('APEC Center', 'АПЕК Центр').replace('APEC', 'АПЕК').replace('«', '').replace('»', '')
    return t if V3 else re.sub(r'\[[a-z ]+\]\s*', '', t)

TRIM = ('silenceremove=start_periods=1:start_threshold=-50dB,areverse,'  # v3 оставляет ~1.5 с тишины по краям
        'silenceremove=start_periods=1:start_threshold=-50dB,areverse')
prev = ''
for i, s in enumerate(S):
    nxt = spoken(S[i + 1]['vo']) if i + 1 < len(S) else ''
    if V3:  # v3: stability только 0 / 0.5 / 1, контекст соседних фраз не поддерживается
        body = {'text': spoken(s['vo']), 'model_id': MODEL, 'voice_settings': {'stability': 0.5, 'similarity_boost': 0.8}}
    else:
        body = {'text': spoken(s['vo']), 'model_id': MODEL, 'previous_text': prev, 'next_text': nxt,
                'voice_settings': {'stability': 0.5, 'similarity_boost': 0.8, 'style': 0.0, 'use_speaker_boost': True, 'speed': 1.0}}
    req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}?output_format=mp3_44100_192',
                                 data=json.dumps(body).encode(), headers={'xi-api-key': KEY, 'Content-Type': 'application/json'})
    mp3 = f'vo/eleven_s{s["id"]}.mp3'
    open(mp3, 'wb').write(urllib.request.urlopen(req, timeout=180).read())
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp3, '-af', TRIM, '-ar', '48000', f'vo/eleven_s{s["id"]}.wav'], check=True)
    prev = spoken(s['vo']); print(s['id'], 'ok', file=sys.stderr)

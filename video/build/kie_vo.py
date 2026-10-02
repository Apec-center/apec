"""Перегенерация озвучки через ElevenLabs на kie.ai (когда сервис снова доступен).
Запуск из рабочей папки:  python3 kie_vo.py George  →  затем  VOICE=eleven python3 render.py"""
import json, sys, subprocess, os
sys.path.insert(0, os.path.dirname(__file__))
from kie import create, wait, dl
voice = sys.argv[1] if len(sys.argv) > 1 else 'George'
S = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'scenes.json')))['scenes']
os.makedirs('vo', exist_ok=True)
for s in S:
    t = create('elevenlabs/text-to-speech-multilingual-v2',
               {'text': s['vo'], 'voice': voice, 'stability': 0.55, 'similarity_boost': 0.75, 'style': 0.15, 'speed': 0.95})
    mp3 = dl(wait(t, 300)[0], f'vo/eleven_s{s["id"]}.mp3')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp3, '-ar', '48000', f'vo/eleven_s{s["id"]}.wav'], check=True)
    print(s['id'], 'ok')

import json,sys,re,sherpa_onnx,soundfile as sf
voice=sys.argv[1] if len(sys.argv)>1 else 'dmitri'
d=f'tts/vits-piper-ru_RU-{voice}-medium'
import glob
cfg=sherpa_onnx.OfflineTtsConfig(model=sherpa_onnx.OfflineTtsModelConfig(vits=sherpa_onnx.OfflineTtsVitsModelConfig(model=glob.glob(d+'/*.onnx')[0],tokens=d+'/tokens.txt',data_dir=d+'/espeak-ng-data',length_scale=1.06),num_threads=4))
tts=sherpa_onnx.OfflineTts(cfg)
S=json.load(open('/home/user/apec/video/scenes.json'))
def spoken(t):
    t=t.replace('APEC Center','АПЕК Сэнтер').replace('APEC','АПЕК').replace('ВЭД','вэд').replace('МИД','мид').replace('«','').replace('»','')
    return t
for s in S['scenes']:
    a=tts.generate(spoken(s['vo']),sid=0,speed=1.0)
    sf.write(f'vo/{voice}_s{s["id"]}.wav',a.samples,a.sample_rate); print(s['id'],round(len(a.samples)/a.sample_rate,2))

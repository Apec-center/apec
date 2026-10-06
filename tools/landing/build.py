# Builds site/index.html from src.html + content.py (+ dot map, emblem).
# Usage: python3 tools/landing/build.py   (ARTIFACT_OUT=path also writes a self-contained preview)
import json,re,sys,base64,os
S=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(S,'..','..'))
OUT=os.environ.get('ARTIFACT_OUT')
sys.path.insert(0,S)
import content as C
src=open(S+'/src.html').read()
dots=open(S+'/dots.json').read()
em=open(ROOT+'/site/img/emblem.svg').read()
inner=re.sub(r'^\s*<svg[^>]*>','',em); inner=re.sub(r'</svg>\s*$','',inner).strip()
lg=open(ROOT+'/site/img/logo.svg').read()
logo=re.sub(r'</svg>\s*$','',re.sub(r'^\s*<svg[^>]*>','',lg.strip())).strip()
faq=[dict(t=t,q=q,a=a) for t,q,a in C.FAQ]
rub=lambda t:re.sub(r"\{R:(\d+)\}",lambda m:"{:,} ₽".format(int(m.group(1))).replace(","," "),t)
ld=",".join(json.dumps({"@type":"Question","name":f["q"],"acceptedAnswer":{"@type":"Answer","text":rub(f["a"])}},ensure_ascii=False) for f in faq)
rep={'/*DOTS*/null':dots,'<!--EMBLEM-->':inner,'<!--LOGO-->':logo,'/*PAINSJSON*/[]':json.dumps(C.PAINS,ensure_ascii=False),'/*FAQJSON*/[]':json.dumps(faq,ensure_ascii=False),'/*FAQLD*/':ld,'<!--DOCS_STD-->':C.DOCS_STD,'<!--DOCS_PRI-->':C.DOCS_PRI,'/*FLAGS*/{}':open(S+'/flags.json').read()}
for k,v in rep.items():
    assert k in src,k
    src=src.replace(k,v)
open(ROOT+'/site/index.html','w').write(src)
# artifact build
a=src
a=re.sub(r'<!doctype html>\s*<html[^>]*>\s*<head>\s*','',a)
a=re.sub(r'<meta charset[^>]*>\s*<meta name="viewport"[^>]*>\s*','',a)
a=re.sub(r'<link rel="icon"[^>]*>\s*','',a); a=re.sub(r'<link rel="preload"[^>]*>\s*','',a)
for f in ['Benzin_Medium','Benzin_Semibold','GrtskTera_Semibold']:
    b=base64.b64encode(open(f'{ROOT}/site/fonts/{f}.woff2','rb').read()).decode()
    a=a.replace(f'url(fonts/{f}.woff2)',f'url(data:font/woff2;base64,{b})')
a=re.sub(r'<title>[^<]*</title>','<title>APEC Center</title>',a,count=1)
a=a.replace('</head>','').replace('<body>','',1).replace('</body>','').replace('</html>','')
if OUT:
    open(OUT,'w').write(a.strip())
print('ok',len(src),len(a))

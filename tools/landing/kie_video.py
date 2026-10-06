import json,os,sys,time,urllib.request
K=os.environ['KIE_API_KEY'];H={"Authorization":"Bearer "+K,"Content-Type":"application/json"};OUT=sys.argv[1]
J={
 "phuket":"Slow cinematic aerial drone shot gliding over a calm turquoise Andaman sea bay in Phuket at golden hour, longtail boats, green hills, soft warm light, gentle smooth camera motion, seamless calm loop feel. No text, no people close up, no logos.",
 "lane":"Cinematic slow dolly shot in a modern Asian international airport passport control hall: a traveller with a carry-on suitcase walks calmly through an empty dedicated fast-track lane while long queues wait in the blurred background, warm ambient light, elegant architecture, shallow depth of field. No text, no logos, no readable signs."
}
names=sys.argv[2:] or list(J)
T={}
for n in names:
  b=json.dumps({"prompt":J[n],"model":"veo3_fast","aspectRatio":"16:9","enableFallback":True}).encode()
  r=json.load(urllib.request.urlopen(urllib.request.Request("https://api.kie.ai/api/v1/veo/generate",b,H),timeout=60))
  print(n,r,flush=True); T[n]=r["data"]["taskId"]
for _ in range(120):
  for n,t in list(T.items()):
    r=json.load(urllib.request.urlopen(urllib.request.Request("https://api.kie.ai/api/v1/veo/record-info?taskId="+t,headers=H),timeout=60))
    d=r.get("data") or {}
    f=d.get("successFlag")
    if f==1:
      urls=d.get("response",{}).get("resultUrls") or json.loads(d.get("resultUrls") or "[]")
      urllib.request.urlretrieve(urls[0],os.path.join(OUT,n+".mp4"));print("OK",n,flush=True);del T[n]
    elif f in (2,3): print("FAIL",n,d.get("errorMessage"),flush=True);del T[n]
  if not T:break
  time.sleep(10)
print("left",T)

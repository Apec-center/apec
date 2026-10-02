import os,sys,json,time,urllib.request
K=os.environ['KIE_API_KEY']; B='https://api.kie.ai/api/v1'
def req(path,body=None):
    r=urllib.request.Request(B+path,data=json.dumps(body).encode() if body else None,headers={'Authorization':'Bearer '+K,'Content-Type':'application/json'},method='POST' if body else 'GET')
    return json.load(urllib.request.urlopen(r,timeout=60))
def create(model,inp,cb=None):
    d=req('/jobs/createTask',{'model':model,'input':inp})
    if d.get('code')!=200: raise Exception(d)
    return d['data']['taskId']
def wait(tid,timeout=1200):
    t0=time.time()
    while time.time()-t0<timeout:
        d=req('/jobs/recordInfo?taskId='+tid)['data']
        if d['state']=='success': return json.loads(d['resultJson'])['resultUrls']
        if d['state']=='fail': raise Exception(d.get('failMsg'))
        time.sleep(8)
    raise Exception('timeout')
def dl(url,path):
    urllib.request.urlretrieve(url,path); return path
if __name__=='__main__':
    for t in sys.argv[1:]: print(t,wait(t))

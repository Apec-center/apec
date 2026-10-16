"""Minimal kie.ai client: create a market task, poll it, download results."""
import json, os, sys, time, urllib.request

API = "https://api.kie.ai/api/v1/jobs"
KEY = os.environ["KIE_API_KEY"]


def _req(url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET",
                                 headers={"Authorization": f"Bearer {KEY}",
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def create(model, inp):
    r = _req(f"{API}/createTask", {"model": model, "input": inp})
    if r.get("code") != 200:
        raise RuntimeError(r)
    return r["data"]["taskId"]


def wait(task_id, timeout=600):
    t0 = time.time()
    while time.time() - t0 < timeout:
        d = _req(f"{API}/recordInfo?taskId={task_id}")["data"]
        if d["state"] == "success":
            return json.loads(d["resultJson"])["resultUrls"]
        if d["state"] == "fail":
            raise RuntimeError(f"{task_id}: {d.get('failMsg')}")
        time.sleep(5)
    raise TimeoutError(task_id)


def download(url, path):
    with urllib.request.urlopen(url, timeout=120) as r, open(path, "wb") as f:
        f.write(r.read())


if __name__ == "__main__":
    # usage: kie.py wait <taskId> <out.png>
    urls = wait(sys.argv[2])
    download(urls[0], sys.argv[3])
    print(sys.argv[3], urls[0])

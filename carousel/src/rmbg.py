"""Remove backgrounds of generated objects via kie.ai recraft/remove-background."""
import json, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import kie

ASSETS = Path(__file__).resolve().parent.parent / "assets"
urls = json.loads((ASSETS / "urls.json").read_text())


def run(name):
    tid = kie.create("recraft/remove-background", {"image": urls[name]})
    kie.download(kie.wait(tid)[0], ASSETS / f"{name}_cut.png")
    return name


with ThreadPoolExecutor(10) as ex:
    for n in ex.map(run, sys.argv[1:]):
        print("cut", n, flush=True)

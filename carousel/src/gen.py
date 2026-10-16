"""Generate carousel assets on kie.ai (nano-banana-pro) in parallel."""
import json, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import kie

ASSETS = Path(__file__).resolve().parent.parent / "assets"

OBJ = ("Premium 3D render in Cinema 4D / Octane style, glossy and soft-touch materials, "
       "high detail, soft studio lighting with a cool electric-blue (#287FF2) rim light from behind, "
       "the object floats in mid-air with a slight dynamic tilt, isolated on a pure white seamless "
       "background, no ground shadow, no extra objects, no text unless specified. Subject: ")

JOBS = {
    "cover": ("16:9", None,
        "Hyper-realistic cinematic 3D render that looks like a premium travel photograph: a tropical Thai beach "
        "in Phuket at golden hour. Hero in the foreground, placed at about one third of the frame width from the "
        "left in the lower half: an ice-cold green glass bottle of Chang beer covered in heavy condensation droplets "
        "and a light frost, standing on a small teak side table right next to a white sun lounger with a rolled "
        "striped beach towel and sunglasses. Background: turquoise Andaman Sea, limestone karst islands on the horizon, "
        "a traditional Thai longtail boat with colorful ribbons on its bow, coconut palms leaning in from the right edge. "
        "The upper 40% of the frame is clean warm sky with soft clouds, empty space for a headline. Gentle sun flare, "
        "vivid but natural colors, shallow depth of field on the bottle. Wide 16:9 composition, no people, "
        "no text except the bottle label."),
    "minivan": ("1:1", None, OBJ +
        "a white Thai tourist minivan (Toyota Commuter style) with two suitcases strapped to the roof rack, "
        "three-quarter view, driving towards the right, slightly stylized realistic look."),
    "card": ("1:1", None, OBJ +
        "a sleek premium plastic travel card in dynamic perspective, gradient from deep cobalt blue (#1F4985) to "
        "electric blue (#287FF2), gold EMV chip, subtle holographic globe line pattern, printed in clean white "
        "wide sans-serif letters: large 'APEC' and below it smaller 'BUSINESS TRAVEL CARD'. Glossy reflections."),
    "passport": ("1:1", None, OBJ +
        "an open passport booklet with a dark burgundy cover (no emblem visible), the right inner page shows a large "
        "fresh round ink stamp in electric blue reading 'THAILAND' and '90 DAYS' with a small stylized elephant, "
        "plus a couple of faded smaller stamps. Pages slightly curved."),
    "hourglass": ("1:1", None, OBJ +
        "an elegant hourglass with a glossy navy-blue lacquered frame and clear glass, filled with white tropical "
        "beach sand flowing down, a tiny pink seashell and a small starfish resting on its base."),
    "stopwatch": ("1:1", None, OBJ +
        "a chrome and navy-blue stopwatch with an electric-blue glowing bezel, the hand pointing at 2 minutes, "
        "subtle motion speed lines, dynamic angle."),
    "globe": ("1:1", None, OBJ +
        "a stylized glossy globe with deep navy-blue oceans and light pearl-grey continents, turned to show "
        "Southeast Asia, China, Japan, Korea, Indonesia and Australia, about twelve glowing electric-blue map pins "
        "standing on Asian countries, a thin luminous orbit ring around it."),
    "plane": ("1:1", None, OBJ +
        "a white passenger jet airplane, stylized clean 3D, flying to the right and slightly upward, three-quarter "
        "view from the front-left, small electric-blue accent stripe on the tail, no airline logo."),
    "plumeria": ("1:1", None, OBJ +
        "two fresh white-and-yellow frangipani (plumeria) flowers, one slightly in front of the other."),
    "palm": ("1:1", None, OBJ +
        "a single lush green tropical coconut palm frond with a graceful dynamic curve, natural leaf texture."),
}


def run(name):
    ar, refs, prompt = JOBS[name]
    inp = {"prompt": prompt, "aspect_ratio": ar, "resolution": "2K", "output_format": "png"}
    if refs:
        inp["image_input"] = refs
    tid = kie.create("nano-banana-pro", inp)
    url = kie.wait(tid)[0]
    kie.download(url, ASSETS / f"{name}.png")
    return name, url


if __name__ == "__main__":
    names = sys.argv[1:] or list(JOBS)
    with ThreadPoolExecutor(10) as ex:
        res = {}
        for fut in [ex.submit(run, n) for n in names]:
            try:
                n, u = fut.result()
                res[n] = u
                print("ok", n, u, flush=True)
            except Exception as e:
                print("FAIL", e, flush=True)
    urls = ASSETS / "urls.json"
    old = json.loads(urls.read_text()) if urls.exists() else {}
    old.update(res)
    urls.write_text(json.dumps(old, indent=1))

"""Assets for carousel variants B («Математика зимовки») and C («Я больше не делаю визараны»)."""
import sys
from concurrent.futures import ThreadPoolExecutor
import gen

SCENE = ("Hyper-realistic cinematic 3D render that looks like a premium travel advertising photograph, "
         "Phuket, Thailand, golden hour, turquoise Andaman Sea, limestone karst islands, coconut palms, "
         "shallow depth of field, warm sun flare, no people. ")
OBJ = gen.OBJ

gen.JOBS.update({
    "b_cover": ("16:9", None, SCENE +
        "Close foreground, at about one third of the frame width from the left, lower half: an ice-cold frosty green "
        "bottle of Chang beer with big condensation droplets standing on a teak beach table, next to it a sleek "
        "retro calculator and a small neat stack of Thai baht banknotes and coins. A white sun lounger and a traditional "
        "longtail boat further right. The top 38% of the frame is clean warm golden sky, empty space for a headline. "
        "Wide 16:9, no text except the bottle label 'Chang' and 'BEER'."),
    "c_cover": ("16:9", None, SCENE +
        "Close foreground, at about one third of the frame width from the left, lower half: an ice-cold frosty green "
        "bottle of Chang beer with big condensation droplets standing in the sand next to a white sun lounger with a "
        "striped towel and sunglasses — relaxed, nowhere to hurry. On the right third of the frame, in the background "
        "on a palm-lined coastal road, a white Toyota Commuter tourist minivan with luggage on its roof is driving away. "
        "The top 38% of the frame is clean warm golden sky, empty space for a headline. Wide 16:9, no text except the "
        "bottle label 'Chang' and 'BEER'."),
    "b_end": ("4:5", None, SCENE +
        "A teak beach-bar table at the water's edge with a frosty green bottle of Chang beer and a fresh coconut with a "
        "straw, all objects in the lower 40% of the frame, slightly to the right. The upper 60% is calm sea and soft golden "
        "sky, clean empty space for text. Label reads 'Chang' 'BEER'."),
    "c_end": ("4:5", None, SCENE +
        "A woven hammock strung between two leaning coconut palms on a quiet beach, a frosty green bottle of Chang beer "
        "in the sand beneath it, all objects in the lower 45% of the frame. Upper 55% calm sea and golden sky, clean "
        "empty space for text. Label reads 'Chang' 'BEER'."),
    "b_money": ("1:1", None, OBJ +
        "a dynamic stack of Thai baht banknotes (red and purple notes) and gold coins, a few notes flying off the top."),
    "b_study": ("1:1", None, OBJ +
        "a navy-blue graduation cap with a tassel resting on a stack of three textbooks, beside it a small glossy red "
        "round prohibition sign with a white airplane icon crossed out."),
    "b_paperwork": ("1:1", None, OBJ +
        "a tall messy stack of paper documents and forms with paper clips, a heavy rubber stamp on top and a small "
        "navy padlock, conveying bureaucracy and difficulty."),
    "b_globe": ("1:1", None, OBJ +
        "a glossy globe with deep navy-blue oceans and light pearl-grey continents showing Asia, with three small white "
        "passenger jets flying around it along glowing electric-blue dotted orbit trails."),
    "c_calendar": ("1:1", None, OBJ +
        "a 3D desk tear-off calendar showing the big number '30', with a sheet of days on it crossed out with bold red "
        "marker X marks, a few torn pages flying around."),
    "c_boarding": ("1:1", None, OBJ +
        "a passport with a dark burgundy cover (no emblem visible) with three white airline boarding passes fanned out "
        "from it, electric-blue accents on the boarding passes, no readable personal data."),
    "c_gate": ("1:1", None, OBJ +
        "a sleek airport fast-track passport control lane: a short glossy white e-gate with a glowing electric-blue "
        "overhead sign that reads 'FAST TRACK' and a bright arrow on the floor, clean stylized look."),
    "c_stamps": ("1:1", None, OBJ +
        "an open passport booklet (burgundy cover, no emblem) whose pages are full of colorful ink entry stamps from "
        "Asian countries — Singapore, Japan, Korea, Indonesia, Vietnam — with a few stamps floating out of the pages."),
})

if __name__ == "__main__":
    names = sys.argv[1:]
    with ThreadPoolExecutor(12) as ex:
        for f in [ex.submit(gen.run, n) for n in names]:
            try:
                n, u = f.result(); print("ok", n, u, flush=True)
            except Exception as e:
                print("FAIL", e, flush=True)

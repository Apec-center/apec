"""Per-slide photo scenes for redesigned carousels B and C (each slide its own Thai scene)."""
import json, sys
from concurrent.futures import ThreadPoolExecutor
import gen

PHOTO = ("Ultra-realistic vivid travel photograph, Thailand, natural cinematic light, rich colors, high detail, "
         "no text, no logos, no watermarks, no close-up faces. Vertical 4:5 composition. ")
B_SPACE = "Keep the lower 45% of the frame visually calm and slightly darker (ground, water, floor) for overlaid text. "
C_SPACE = "Keep the top 25% and the bottom 35% of the frame calm and uncluttered for overlaid text. "

JOBS = {
    # ---- B: "Математика зимовки" — reference style, a different place on every slide
    "B2": B_SPACE + "A hot, dusty Thai land border checkpoint (Thailand–Malaysia, Sadao style): a long queue of tired tourists "
          "with suitcases, several white Toyota tourist minivans parked, immigration booths with roofs, harsh midday sun, palm trees.",
    "B3": B_SPACE + "A bright language-school classroom in Bangkok: rows of empty wooden desks, a whiteboard with Thai alphabet letters, "
          "big windows with palm trees and city outside, afternoon sun rays.",
    "B4": B_SPACE + "A busy visa office desk in Thailand: a towering stack of paper forms and folders, rubber stamps, a queue-number "
          "display glowing red in the background, small Thai flag, fluorescent light, bureaucratic mood.",
    "B5": B_SPACE + "A luxury infinity-pool villa in Phuket at golden hour overlooking the Andaman Sea and limestone islands, "
          "a frosty green bottle of Chang beer on the pool edge, sun lounger, frangipani flowers floating in the water.",
    "B6": B_SPACE + "A Bangkok rooftop sky bar at blue hour: glass railing, city skyline with lit skyscrapers and the Chao Phraya "
          "river, warm table lamps, cocktails on a table, deep blue sky.",
    "B7": B_SPACE + "Inside a modern Thai airport terminal at sunset: a large departures board (only the word 'Departures' "
          "readable), floor-to-ceiling windows with palm trees and a parked airliner outside, warm golden light on the floor.",
    "B8": B_SPACE + "A wooden beach restaurant deck in Krabi at sunset: teak tables and chairs with candles, thatched-roof "
          "pavilion on the left, turquoise water with two traditional longtail boats, limestone karst islands, pastel sky.",
    # ---- C: "Я больше не делаю визараны" — first-person story scenes
    "C2": C_SPACE + "First-person view from the back seat inside a cramped white tourist minivan on a Thai highway: rows of "
          "seats, backpacks and suitcases stacked, curtains on windows, palm trees blurred outside, tired mood, harsh daylight.",
    "C3": C_SPACE + "A wall calendar in a small Phuket condo with most days crossed out in red marker, a passport lying on a "
          "desk below, balcony door open to palm trees and sea in the background, morning light.",
    "C5": C_SPACE + "View through an airplane window over Phang Nga Bay, Thailand: turquoise sea, dozens of limestone karst "
          "islands, tiny longtail boats with white wakes, soft morning light, the oval window frame visible around the view.",
    "C6": C_SPACE + "Phuket airport immigration hall: on the right a long crowded queue of travellers, on the left an empty "
          "separate lane with a glowing blue overhead sign 'FAST TRACK', glossy floor, palm plants, bright and clean.",
    "C7": C_SPACE + "A golden Thai temple roof with ornate chofa finials in the foreground at sunset, a passenger jet "
          "taking off in the orange sky above it, palm silhouettes, epic travel mood.",
    "C8": C_SPACE + "A Thai beach at night during a lantern festival: dozens of glowing paper sky lanterns (khom loi) rising "
          "over the calm sea, warm string lights on palm trees, silhouettes of people far away, magical mood.",
}


def run(name):
    gen.JOBS[name] = ("4:5", None, PHOTO + JOBS[name])
    return gen.run(name)


if __name__ == "__main__":
    names = sys.argv[1:] or list(JOBS)
    res = {}
    with ThreadPoolExecutor(13) as ex:
        for f in [ex.submit(run, n) for n in names]:
            try:
                n, u = f.result(); res[n] = u; print("ok", n, flush=True)
            except Exception as e:
                print("FAIL", e, flush=True)
    d = json.load(open(gen.ASSETS / "urls.json")); d.update(res)
    json.dump(d, open(gen.ASSETS / "urls.json", "w"), indent=1)

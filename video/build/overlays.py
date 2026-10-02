"""Брендовые инфографические оверлеи APEC Center (1080x1920, прозрачный PNG)."""
import os, sys, qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FD = os.environ.get('FONTS', 'fonts')
W, H = 1080, 1920
NAVY = (15, 30, 54); GOLD = (212, 175, 55); GOLD_SOFT = (226, 196, 110)
WHITE = (246, 243, 236); MUTED = (176, 184, 198); CORAL = (232, 144, 122); GREEN = (110, 200, 160)
X0 = 72  # левый отступ

def F(kind, size):
    name = {'serif': 'Source_Serif_4_wght_400', 'serifb': 'Source_Serif_4_wght_600',
            'sans': 'Source_Sans_3_wght_400', 'sansb': 'Source_Sans_3_wght_600', 'sansbb': 'Source_Sans_3_wght_700'}[kind]
    return ImageFont.truetype(f'{FD}/{name}.ttf', size)

def spaced(d, xy, text, font, fill, spacing):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill); x += d.textlength(ch, font=font) + spacing
    return x

def rich(d, xy, lines, font, lh, base=WHITE, accent=GOLD):
    """Строки, где фрагменты в [квадратных скобках] — золотые."""
    x0, y = xy
    for line in lines:
        x = x0
        for i, part in enumerate(line.replace(']', '[').split('[')):
            if part:
                d.text((x, y), part, font=font, fill=accent if i % 2 else base); x += d.textlength(part, font=font)
        y += lh
    return y

def card(img, box, fill=(20, 34, 60, 215), outline=(212, 175, 55, 90), r=26, width=2):
    lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); ImageDraw.Draw(lay).rounded_rectangle(box, r, fill=fill, outline=outline, width=width)
    img.alpha_composite(lay)

def base_frame(idx, total, grad_from=0.42):
    """Фон-слой: градиент снизу + шапка бренда."""
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    g = Image.new('L', (1, H))
    for y in range(H):
        t = (y / H - (grad_from - 0.1)) / (1 - (grad_from - 0.1)) * 1.35
        g.putpixel((0, y), int(max(0, min(1, t)) ** 0.9 * 242))
    grad = Image.new('RGBA', (W, H), NAVY + (0,)); grad.putalpha(g.resize((W, H)))
    top = Image.new('L', (1, H))
    for y in range(H): top.putpixel((0, y), int(max(0, 1 - y / 300) * 150))
    tg = Image.new('RGBA', (W, H), NAVY + (0,)); tg.putalpha(top.resize((W, H)))
    img.alpha_composite(grad); img.alpha_composite(tg)
    return img

def header(img, idx, total):
    d = ImageDraw.Draw(img)
    cx, cy, r = X0 + 22, 132, 22  # глобус-логотип
    d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=WHITE, width=3)
    d.ellipse((cx - 10, cy - r, cx + 10, cy + r), outline=WHITE, width=2)
    d.line((cx - r, cy, cx + r, cy), fill=WHITE, width=2)
    spaced(d, (X0 + 60, 116), 'APEC CENTER', F('sansb', 30), WHITE, 5)
    f = F('serif', 30)
    t1, t2 = f'{idx:02d}', f' / {total:02d}'
    w = d.textlength(t1 + t2, font=f)
    d.text((W - X0 - w, 114), t1, font=f, fill=GOLD); d.text((W - X0 - w + d.textlength(t1, font=f), 114), t2, font=f, fill=MUTED)

def eyebrow(d, y, text, color=GOLD):
    d.line((X0, y + 17, X0 + 50, y + 17), fill=color, width=2)
    spaced(d, (X0 + 68, y), text, F('sansb', 28), color, 6)

def save(img, path):
    img.save(path)

def footer(d, text):
    spaced(d, (X0, 1650), text, F('sans', 24), MUTED, 4)

# ---------- сцены ----------
def s1(o):
    img = base_frame(1, 9); header(img, 1, 9); d = ImageDraw.Draw(img)
    eyebrow(d, 1010, 'ТАИЛАНД · С 15 СЕНТЯБРЯ 2026', CORAL)
    rich(d, (X0, 1062), ['Безвиз — [30 дней]'], F('serif', 96), 110)
    card(img, (X0, 1210, 530, 1440)); card(img, (550, 1210, W - X0, 1440), outline=CORAL + (140,))
    d = ImageDraw.Draw(img)
    d.text((X0 + 32, 1240), '+30', font=F('serif', 72), fill=WHITE)
    d.multiline_text((X0 + 32, 1335), 'продление —\nтолько раз в год', font=F('sans', 32), fill=MUTED, spacing=6)
    d.text((582, 1240), '≈11', font=F('serif', 72), fill=CORAL)
    d.multiline_text((582, 1335), 'выездов в год\nбез карты', font=F('sans', 32), fill=MUTED, spacing=6)
    return img

def s2(o):
    img = base_frame(2, 9, 0.48); header(img, 2, 9); d = ImageDraw.Draw(img)
    eyebrow(d, 1060, 'APEC BUSINESS TRAVEL CARD')
    rich(d, (X0, 1110), ['Один документ', 'на [5 лет]'], F('serif', 88), 100)
    stats = [('5 лет', 'многократных\nвъездов'), ('90 дней', 'за один\nвъезд'), ('18 стран', 'Азиатско-\nТихоокеанского\nрегиона')]
    cw = (W - 2 * X0 - 2 * 18) // 3
    for i, (a, b) in enumerate(stats):
        x = X0 + i * (cw + 18); card(img, (x, 1330, x + cw, 1580)); d = ImageDraw.Draw(img)
        d.text((x + 24, 1352), a, font=F('serif', 54), fill=GOLD)
        d.multiline_text((x + 24, 1430), b, font=F('sans', 28), fill=WHITE, spacing=4)
    return img

def s3(o):
    img = base_frame(3, 9); header(img, 3, 9); d = ImageDraw.Draw(img)
    eyebrow(d, 1010, 'ТАИЛАНД: ВЫЕЗДОВ В ГОД')
    rich(d, (X0, 1062), ['[4] вместо 11'], F('serif', 96), 110)
    card(img, (X0, 1210, W - X0, 1520)); d = ImageDraw.Draw(img)
    maxw = W - 2 * X0 - 64 - 200
    for j, (lab, n, col) in enumerate([('Без карты', 11, CORAL), ('С картой', 4, GOLD)]):
        y = 1250 + j * 130
        d.text((X0 + 32, y), lab, font=F('sansb', 32), fill=WHITE)
        bw = int(maxw * n / 11)
        d.rounded_rectangle((X0 + 32, y + 50, X0 + 32 + bw, y + 86), 10, fill=col)
        d.text((X0 + 48 + bw, y + 40), f'{n}', font=F('serif', 48), fill=col)
    footer(d, 'РАЗ В КВАРТАЛ · БЕЗ ВИЗИТОВ В ИММИГРАЦИОННУЮ')
    return img

def s4(o):
    img = base_frame(4, 9, 0.36); header(img, 4, 9); d = ImageDraw.Draw(img)
    eyebrow(d, 880, '18 СТРАН АТЭС · СЕЙЧАС')
    rich(d, (X0, 930), ['Без карты → [с картой]'], F('serif', 80), 96)
    rows = [('Сингапур', 'нужна виза', 'без визы'), ('Тайвань', 'нужна виза', 'без визы'),
            ('Гонконг', '14 дней', '60 дней'), ('Малайзия, Китай', '30 дней', '60 дней'), ('Корея', 'K-ETA', 'без K-ETA')]
    card(img, (X0, 1060, W - X0, 1060 + 96 * len(rows) + 24)); d = ImageDraw.Draw(img)
    for i, (c, a, b) in enumerate(rows):
        y = 1084 + i * 96
        if i: d.line((X0 + 28, y - 12, W - X0 - 28, y - 12), fill=(212, 175, 55, 50), width=1)
        d.text((X0 + 32, y + 8), c, font=F('sansb', 34), fill=WHITE)
        d.text((560, y + 10), a, font=F('sans', 30), fill=MUTED)
        d.text((W - X0 - 32 - d.textlength(b, font=F('sansb', 34)), y + 8), b, font=F('sansb', 34), fill=GOLD)
    d.text((X0, 1640), 'Решение о въезде всегда принимает пограничник', font=F('sans', 24), fill=MUTED)
    return img

def s5(o):
    img = base_frame(5, 9); header(img, 5, 9); d = ImageDraw.Draw(img)
    eyebrow(d, 1150, 'ГРАНИЦА')
    rich(d, (X0, 1200), ['Коридор [APEC Lane]'], F('serif', 92), 106)
    d.multiline_text((X0, 1330), 'Отдельный паспортный контроль\nв аэропортах стран-участниц — \nмимо общей очереди', font=F('sans', 38), fill=WHITE, spacing=10)
    return img

def s6(o):
    img = base_frame(6, 9, 0.34); header(img, 6, 9); d = ImageDraw.Draw(img)
    eyebrow(d, 830, 'ЗАКОННЫЙ ПОРЯДОК · ЧЕРЕЗ МИД РФ')
    rich(d, (X0, 880), ['Своя компания', '[не нужна]'], F('serif', 84), 96)
    steps = [('01', 'Вы', 'нужен только загранпаспорт'),
             ('02', 'Аккредитованная ВЭД-компания', 'включает вас внешнеторговым советником'),
             ('03', 'ТПП РФ · РСПП · «Опора России»', 'подают заявление в МИД РФ')]
    for i, (n, t, s) in enumerate(steps):
        y = 1090 + i * 150
        card(img, (X0, y, W - X0, y + 132), fill=(20, 34, 60, 225) if i < 2 else (212, 175, 55, 40)); d = ImageDraw.Draw(img)
        d.text((X0 + 28, y + 30), n, font=F('serif', 56), fill=GOLD)
        d.text((X0 + 130, y + 22), t, font=F('sansb', 36), fill=WHITE)
        d.text((X0 + 130, y + 72), s, font=F('sans', 30), fill=MUTED)
    footer(d, 'ВСЁ УДАЛЁННО · ИЗ ЛЮБОЙ СТРАНЫ')
    return img

def s7(o):
    img = base_frame(7, 9); header(img, 7, 9); d = ImageDraw.Draw(img)
    eyebrow(d, 1040, 'БЕЗОПАСНОСТЬ СДЕЛКИ')
    rich(d, (X0, 1090), ['Договор-оферта'], F('serif', 92), 106)
    card(img, (X0, 1240, W - X0, 1500), fill=(14, 42, 46, 230), outline=GREEN + (150,)); d = ImageDraw.Draw(img)
    d.text((X0 + 36, 1266), 'Возврат 100%', font=F('serif', 76), fill=GREEN)
    d.multiline_text((X0 + 36, 1370), 'если МИД РФ официально откажет —\nвернём всю внесённую оплату', font=F('sans', 34), fill=WHITE, spacing=8)
    return img

def s8(o):
    img = base_frame(8, 9); header(img, 8, 9); d = ImageDraw.Draw(img)
    eyebrow(d, 1000, 'ТАРИФ «ПРИОРИТЕТ»')
    rich(d, (X0, 1050), ['Карта за [60–80 дней]'], F('serif', 86), 100)
    pts = [('0', 'оплата\nи подача'), ('~60', 'дней\nтрек-номер'), ('60–80', 'дней\nвременная карта')]
    xs = [X0 + 90, W // 2, W - X0 - 90]; y = 1270
    d.line((xs[0], y, xs[2], y), fill=GOLD, width=3)
    for i, ((n, lab), x) in enumerate(zip(pts, xs)):
        last = i == 2
        d.ellipse((x - 78, y - 78, x + 78, y + 78), fill=NAVY + (255,) if last else (246, 238, 220, 255), outline=GOLD, width=3)
        f = F('serif', 46 if len(n) > 3 else 54); tw = d.textlength(n, font=f)
        d.text((x - tw / 2, y - 32), n, font=f, fill=GOLD if last else NAVY)
        for k, ln in enumerate(lab.split('\n')):
            fw = d.textlength(ln, font=F('sans', 30)); d.text((x - fw / 2, y + 96 + k * 36), ln, font=F('sans', 30), fill=WHITE)
    card(img, (X0, 1470, W - X0, 1570), fill=(212, 175, 55, 45)); d = ImageDraw.Draw(img)
    t = 'Тарифы от 60 000 ₽ · госпошлины включены'; f = F('sansb', 34)
    d.text(((W - d.textlength(t, font=f)) / 2, 1497), t, font=f, fill=WHITE)
    return img

def s9(o):
    img = base_frame(9, 9, 0.38); header(img, 9, 9); d = ImageDraw.Draw(img)
    eyebrow(d, 930, 'БЕСПЛАТНО · БЕЗ ОБЯЗАТЕЛЬСТВ')
    rich(d, (X0, 980), ['Первый шаг —', '[проверка паспорта]'], F('serif', 80), 94)
    steps = [('01', 'Фото\nзагранпаспорта'), ('02', 'Проверка\nспециалистом'), ('03', 'Ответ\nи сроки')]
    cw = (W - 2 * X0 - 36) // 3
    for i, (n, t) in enumerate(steps):
        x = X0 + i * (cw + 18); card(img, (x, 1190, x + cw, 1360)); d = ImageDraw.Draw(img)
        d.text((x + 24, 1206), n, font=F('serif', 40), fill=GOLD)
        d.multiline_text((x + 24, 1262), t, font=F('sansb', 30), fill=WHITE, spacing=4)
    # QR + кнопка
    qr = qrcode.QRCode(border=2, box_size=8); qr.add_data('https://t.me/apec_center_bot'); qr.make(fit=True)
    q = qr.make_image(fill_color=(15, 30, 54), back_color='white').convert('RGBA').resize((210, 210), Image.NEAREST)
    card(img, (X0, 1390, X0 + 240, 1630), fill=(20, 34, 60, 230)); img.alpha_composite(q, (X0 + 15, 1405))
    btn = Image.new('RGBA', (W - X0 - (X0 + 262), 240))
    bd = ImageDraw.Draw(btn)
    for x in range(btn.width):
        t = x / btn.width; c = tuple(int(a + (b - a) * t) for a, b in zip((232, 205, 120), (190, 148, 40)))
        bd.line((x, 0, x, btn.height), fill=c + (255,))
    m = Image.new('L', btn.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, btn.width - 1, btn.height - 1), 26, fill=255); btn.putalpha(m)
    img.alpha_composite(btn, (X0 + 262, 1390)); d = ImageDraw.Draw(img)
    bx = X0 + 296
    spaced(d, (bx, 1420), 'TELEGRAM', F('sansbb', 26), NAVY, 6)
    d.text((bx, 1462), '@apec_center_bot', font=F('sansbb', 44), fill=NAVY)
    d.text((bx, 1540), 'Пройти проверку →', font=F('sansb', 32), fill=NAVY)
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else 'overlays'
    os.makedirs(out, exist_ok=True)
    for i, fn in enumerate([s1, s2, s3, s4, s5, s6, s7, s8, s9], 1):
        save(fn(None), f'{out}/o{i}.png')
    print('ok')

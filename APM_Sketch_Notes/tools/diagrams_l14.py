# Excalidraw scenes for Chapter 17 (page 14, l14-*). Run: python3 diagrams_l14.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'
PINK = '#9c36b5'


def scale_x(v, lo=0, hi=1200, x0=40, x1=920):
    return x0 + (v - lo) / (hi - lo) * (x1 - x0)


# 1 ─ price anchors ───────────────────────────────────────────────────────────────────────────────────
def d_price_anchors():
    s = Scene()
    title(s, 'Three anchors around one price',
          'cost is the floor, competitors the reference, customer value the ceiling (Rs, per month)')
    # cost floor row
    s.box(scale_x(0), 100, scale_x(100) - scale_x(0), 40, None, 'pink', opacity=70)
    s.text(scale_x(100) + 14, 108, 'cost floor: about Rs 60 a month; under about', 15, INK)
    s.text(scale_x(100) + 14, 128, 'Rs 100 it loses money after CAC', 15, INK)
    # competitor row
    s.box(scale_x(150), 170, scale_x(400) - scale_x(150), 40, None, 'blue', opacity=60)
    s.text(scale_x(400) + 14, 178, 'competitor reference: a few hundred Rs', 15, INK)
    s.text(scale_x(400) + 14, 198, 'a month for basic plans', 15, INK)
    # value row
    s.text(scale_x(560), 228, 'value ceiling: about Rs 1,000+ a month saved', 15, INK)
    s.box(scale_x(1000), 250, scale_x(1200) - scale_x(1000), 40, None, 'green', opacity=65)
    # axis
    s.line([(40, 320), (920, 320)], sw=2)
    for v in (0, 250, 500, 750, 1000):
        s.line([(scale_x(v), 314), (scale_x(v), 326)], color=GREY, sw=2)
        s.text(scale_x(v) - 16, 332, f'{v}', 14, GREY, ff=3)
    # the pick
    s.line([(scale_x(249), 162), (scale_x(249), 320)], color=YEL, sw=4)
    s.text(scale_x(249) - 150, 358, 'pick: about Rs 249, near the reference,', 16, INK)
    s.text(scale_x(249) - 150, 380, 'well under the ceiling (goal: share)', 16, INK)
    s.save('l14-price-anchors')


# 2 ─ monetization map ────────────────────────────────────────────────────────────────────────────────
def d_monetization_map():
    s = Scene()
    title(s, 'Monetization models follow where the value is created',
          'ask who gets the value first, then pick the model that charges for it')
    cols = [
        ('the user', 'pays for access', [
            'subscription', 'freemium', 'fixed price (one-time)', 'in-app add-ons']),
        ('the usage', 'pays per unit', [
            'per seat', 'usage-based', 'outcome-based']),
        ('the transaction', 'a cut of each deal', [
            'take rate', 'bookings, payments']),
        ('the attention', 'pays with attention', [
            'advertising', 'impressions, clicks']),
        ('the ecosystem', 'cheap core, paid rest', [
            'razor-and-blade', 'bundling']),
    ]
    for i, (head, sub, models) in enumerate(cols):
        x = 10 + i * 190
        s.box(x, 96, 180, 58, head, 'purple', fs=17, opacity=60)
        s.text(x + 8, 164, sub, 13, GREY, ff=3)
        for j, m in enumerate(models):
            s.box(x, 196 + j * 52, 180, 40, m, 'pink', fs=15, opacity=45)
    s.box(10, 420, 940, 52, 'B2B and AI products often price per seat, per usage or per outcome',
          'yellow', fs=16, opacity=45)
    s.text(10, 486, 'questions: who gets the value? does it recur? does cost scale with use?', 15, GREY, ff=3)
    s.save('l14-monetization-map')


# 3 ─ price-test ladder ───────────────────────────────────────────────────────────────────────────────
def d_price_test_ladder():
    s = Scene()
    title(s, 'Price-test ladder: cheap reads first, real money last',
          'each rung costs more and risks more of the trust you have built')
    rungs = [
        ('Van Westendorp\nsurvey (cheapest)', 'teal'),
        ('Gabor-Granger\nwould you buy at X?', 'teal'),
        ('conjoint\nbundles and prices', 'teal'),
        ('fake door\nclick a paid plan', 'orange'),
        ('live A/B\nreal users, real money', 'red'),
    ]
    for i, (text, col) in enumerate(rungs):
        x = 40 + i * 185
        y = 340 - i * 64
        s.box(x, y, 165, 56, text, col, fs=15, opacity=60 if col != 'red' else 40)
        if i < len(rungs) - 1:
            s.arrow([(x + 166, y + 28), (x + 183, y + 28 - 64)], color=GREY, sw=2)
    s.text(40, 420, 'bottom rungs: cheap, reversible, safe to try', 17, GREEN)
    s.text(40, 448, 'top rung: a controlled cohort and a readout over a billing cycle', 17, RED)
    s.save('l14-price-test-ladder')


# 4 ─ how to design a pricing test ────────────────────────────────────────────────────────────────────
def d_ab_design():
    s = Scene()
    title(s, 'Designing a pricing test: six steps',
          'the primary metric is revenue per user; guardrails and retention stop a bad win')
    steps = [
        ('1 hypothesis\n"revenue per user up,\nchurn up at most 2 points"', 'orange'),
        ('2 variable\nprice level, framing,\ndiscount, what each tier holds', 'orange'),
        ('3 cohort\nnew users, or a random slice;\nno visible comparison', 'orange'),
        ('4 metrics\nprimary: revenue per user\nguardrails + retention 30-90 days', 'green'),
        ('5 run a full billing cycle\nannual plans and churn lag\nthe first purchase', 'orange'),
        ('6 decide and communicate\nrollback plan, and a plan\nfor existing subscribers', 'green'),
    ]
    pos = [(40, 100), (340, 100), (640, 100), (40, 250), (340, 250), (640, 250)]
    for (text, col), (x, y) in zip(steps, pos):
        s.box(x, y, 280, 100, text, col, fs=15, opacity=60)
    s.arrow([(322, 150), (338, 150)], color=GREY, sw=3)
    s.arrow([(622, 150), (638, 150)], color=GREY, sw=3)
    s.arrow([(780, 202), (780, 226), (180, 226), (180, 248)], color=GREY, sw=3)
    s.arrow([(322, 300), (338, 300)], color=GREY, sw=3)
    s.arrow([(622, 300), (638, 300)], color=GREY, sw=3)
    s.box(40, 380, 880, 52, 'do not call it on conversion alone: read revenue per user with the guardrails',
          'yellow', fs=16, opacity=45)
    s.text(40, 452, 'peeking early and stopping on noise is the most common mistake', 16, RED)
    s.save('l14-ab-design')


# 5 ─ price-test readout (numbers from the lab block: 10,000 visitors) ────────────────────────────────
def d_price_readout():
    s = Scene()
    title(s, 'Same buy rate, higher price: revenue per visitor rises',
          'lab numbers: 10,000 visitors a month; A is the control')
    bars = [
        ('A  8.00', '5.0% buy', 500, 0.400, 'blue'),
        ('B  9.00', '4.5% buy', 450, 0.405, 'orange'),
        ('C  10.00', '4.5% buy', 450, 0.450, 'pink'),
    ]
    base = 340
    for i, (name, buy, buyers, rpv, col) in enumerate(bars):
        x = 120 + i * 260
        h = rpv / 0.45 * 200
        s.box(x, base - h, 150, h, None, col, opacity=70)
        s.text(x + 14, base - h - 30, f'{rpv:.3f}', 20, INK, ff=3)
        s.text(x, base + 12, name, 16, INK, ff=3)
        s.text(x, base + 34, buy, 15, RED if i else GREY, ff=3)
        s.text(x, base + 54, f'{buyers} buyers', 15, GREY, ff=3)
    s.line([(90, base), (900, base)], sw=2)
    s.text(10, 84, 'revenue per visitor (Rs)', 16, GREY)
    s.box(10, 420, 940, 50, 'B: buy rate down 10%, yet revenue per visitor still rises a little',
          'yellow', fs=16, opacity=45)
    s.text(10, 486, 'the buy rate alone calls B a loss; churn is not in this read yet', 15, GREY, ff=3)
    s.save('l14-price-readout')


# 6 ─ take rate on the same volume (numbers from the lab block) ────────────────────────────────────────
def d_take_rate():
    s = Scene()
    title(s, 'Take rate: the same GMV, three different platform revenues',
          'GMV = 20,000 orders x 500 rupees = 10,000,000 a month')
    rows = [
        ('take 2%', 200_000, 'blue'),
        ('take 10%', 1_000_000, 'orange'),
        ('take 20%', 2_000_000, 'red'),
    ]
    for i, (name, rev, col) in enumerate(rows):
        y = 120 + i * 80
        s.text(40, y + 12, name, 18, INK, ff=3)
        w = rev / 2_000_000 * 560
        s.box(170, y, w, 46, None, 'pink', opacity=70)
        s.text(180 + w, y + 13, f'{rev:,} Rs a month', 16, INK, ff=3)
    s.box(40, 370, 880, 50, 'a cut that feels too high loses sellers, and then orders',
          'red', fs=16, opacity=30)
    s.text(40, 440, 'test a change in take rate with a cohort of sellers first', 16, INK)
    s.text(40, 466, 'watch order volume as well as revenue', 16, INK)
    s.save('l14-take-rate')


# 7 ─ big picture ─────────────────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 17 on one page', 'anchor the price, pick the model, then test it safely')
    cols = [
        ('17.1 anchors', 'cost floor, competitor reference, value ceiling', 'what does the goal say?', 'pink'),
        ('17.2 models', 'subscription, freemium, ads, take rate, bundles', 'where is the value created?', 'pink'),
        ('17.3 tests', 'survey, fake door, then a controlled cohort', 'revenue per user and retention?', 'teal'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 316
        s.box(x, 84, 305, 62, head, 'purple', fs=17, opacity=60)
        s.box(x, 158, 305, 110, core, c, fs=16, opacity=40)
        s.box(x, 280, 305, 92, q, 'yellow', fs=16, opacity=60)
    s.box(10, 392, 940, 58, 'a price that clears the floor, sits near the market, and is under the value',
          'green', fs=16, opacity=40)
    s.box(10, 462, 940, 36, 'beyond the notes: a launch checklist, pitfalls in readouts, the take-rate maths',
          'grey', fs=15, opacity=45)
    s.save('l14-big-picture')


for f in [d_price_anchors, d_monetization_map, d_price_test_ladder, d_ab_design, d_price_readout,
          d_take_rate, d_big_picture]:
    f()

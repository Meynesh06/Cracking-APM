# Excalidraw scenes for Chapter 23 (page 20, l20-*). Run: python3 diagrams_l20.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


def node(s, x, y, w, h, text, color, fs=15, opacity=60):
    s.box(x, y, w, h, text, color, fs=fs, opacity=opacity)


def down(s, x, y1, y2, color=GREY):
    s.arrow([(x, y1), (x, y2)], color=color, sw=2)


# 1 ─ the three habits across the sections ───────────────────────────────────────────────────────────
def d_three_habits():
    s = Scene()
    title(s, 'Three sections, one habit',
          'each section shows the same moves on a different kind of case')
    cols = [
        ('23.1 Sigma casebook', 'Uber drivers: RCA, decompose income'),
        ('23.2 XLRI casebook', 'Uber Premier: trips x fare, break-even'),
        ('23.3 Interview reports', 'Google Maps ETA at Just Dial: scope, revert'),
    ]
    for i, (head, ex) in enumerate(cols):
        x = 20 + i * 316
        s.box(x, 96, 296, 44, head, 'purple', fs=16, opacity=55)
        s.text(x + 8, 150, ex, 15, GREY)
    steps = [
        ('1  clarify the goal', 'blue'),
        ('2  structure with the framework', 'orange'),
        ('3  quantify every guess', 'teal'),
        ('4  close: fix, metric, guardrail', 'green'),
    ]
    for i, (t, c) in enumerate(steps):
        x = 20 + i * 236
        s.box(x, 220, 226, 70, t, c, fs=16, opacity=55)
        if i < 3:
            s.arrow([(x + 228, 255), (x + 236, 255)], color=GREY, sw=2)
    s.text(20, 330, 'interviewers push for numbers at every stage', 17, PURPLE)
    s.text(20, 358, 'mitigate first, then fix the root cause', 17, PURPLE)
    s.box(0, 420, 940, 56, 'use the case type to choose the structure: CIRCLES, a driver tree, a journey walk',
          'yellow', fs=16, opacity=60)
    s.save('l20-three-habits')


# 2 ─ Flipkart Hyperlocal journey ─────────────────────────────────────────────────────────────────────
def d_flipkart_journey():
    s = Scene()
    title(s, 'Flipkart Hyperlocal: the journey, and the one step that moved',
          'four steps; pickup-to-delivery is the only one up, about 9 minutes')
    s.text(530, 100, 'pickup to delivery: the only step up', 16, PURPLE)
    node(s, 20, 130, 150, 60, 'acceptance', 'orange', fs=15)
    node(s, 200, 130, 150, 60, 'travel to store', 'orange', fs=15)
    node(s, 380, 130, 120, 60, 'pickup', 'orange', fs=15)
    node(s, 530, 130, 150, 60, 'to landmark', 'green', fs=15)
    node(s, 710, 130, 210, 60, 'landmark to door', 'red', fs=15)
    for x in (170, 350, 500, 680):
        s.arrow([(x, 160), (x + 30, 160)], color=GREY, sw=2)
    for x in (95, 275, 440):
        s.text(x - 14, 204, 'fine', 15, GREEN)
    s.text(568, 204, 'fine', 15, GREEN)
    s.text(720, 204, 'agents wait 5-10 min', 15, RED)
    s.text(720, 224, 'at the apartment gate', 15, RED)
    s.box(0, 260, 420, 56, 'average up 10%: about 9 min on a 90-min promise', 'yellow', fs=15, opacity=60)
    s.box(440, 260, 480, 56, 'check first: gate-security entry for agents at\napartments in these areas', 'red', fs=15, opacity=30)
    s.text(0, 346, 'the fix to test: pre-registered agent entry or digital gate passes', 17, GREEN)
    s.text(0, 374, 'confirm with one cut: gate time by apartment vs the rest of the route', 16, PURPLE)
    s.save('l20-flipkart-journey')


# 3 ─ Uber Drivers RCA tree ────────────────────────────────────────────────────────────────────────────
def d_uber_drivers():
    s = Scene()
    title(s, 'Uber Drivers: a tree from the drop to the late-night fee',
          'each level rules something in or out; the scope rules out releases')
    node(s, 300, 84, 330, 56, 'active drivers -2%\n(Hyderabad only, 2 months)', 'red', fs=15, opacity=40)
    cx = [140, 470, 800]
    kids = [
        ('scope: one city only\nso not a release', 'grey'),
        ('journey: requests and\nacceptance are flat', 'green'),
        ('payment: earnings per\ntrip fell', 'red'),
    ]
    for x, (t, c) in zip(cx, kids):
        s.arrow([(465, 140), (x, 184)], color=GREY, sw=2)
        node(s, x - 110, 184, 220, 56, t, c, fs=14, opacity=50)
    down(s, 800, 240, 286)
    node(s, 690, 286, 220, 56, 'same trips, lower fare;\ntips unchanged', 'orange', fs=14)
    down(s, 800, 342, 386)
    node(s, 660, 386, 280, 56, 'late-night fee removed\n(10 PM-6 AM, "safe city")', 'yellow', fs=14)
    down(s, 800, 442, 486)
    node(s, 660, 486, 280, 46, 'confirm: drop severe at night, small at peak', 'green', fs=14)
    s.text(20, 504, 'fixes: a graded city safety index; night incentives', 15, PURPLE)
    s.text(20, 530, 'bundled after n night rides, tested as experiments', 15, PURPLE)
    s.save('l20-uber-drivers')


# 4 ─ Google Maps ETA: verify, act, prevent ────────────────────────────────────────────────────────────
def d_google_maps_eta():
    s = Scene()
    title(s, 'Google Maps ETA too short: verify, then act, then prevent',
          'scope first; compare predicted and actual times before any rollback')
    steps = [
        ('1 scope', ['all platforms,', 'a few days old,', 'worse at peak'], 'orange'),
        ('2 verify', ['predicted vs actual', 'time, before and after', 'the update'], 'teal'),
        ('3 hypothesise', ['closures: too heavy', 'peak traffic: too light'], 'purple'),
        ('4 act', ['fix the weights', 'tell users the', 'timeline'], 'green'),
        ('5 prevent', ['stronger tests', 'for routing changes', 'user feedback loop'], 'green'),
    ]
    for i, (h, body, c) in enumerate(steps):
        x = 20 + i * 190
        s.box(x, 110, 176, 44, h, c, fs=17, opacity=55)
        for j, line in enumerate(body):
            s.text(x + 4, 166 + j * 20, line, 13, INK)
        if i < 4:
            s.arrow([(x + 178, 132), (x + 190, 132)], color=GREY, sw=2)
    s.box(0, 260, 940, 60, 'one route only? check closures and map errors on that route first',
          'yellow', fs=17, opacity=60)
    s.text(0, 344, 'then a narrow rollback for affected routes, if the data supports it', 17, GREEN)
    s.text(0, 372, 'a global rollback only if the error shows up across regions', 17, RED)
    s.save('l20-google-maps-eta')


# 5 ─ Apple Home anchors and the premium ───────────────────────────────────────────────────────────
def d_apple_home_anchors():
    s = Scene()
    title(s, 'Apple Home: competitor anchors, then a 15% premium',
          'Rs thousands on the scale; the premium lands both Apple variants')
    x0, k = 280, 50          # x of Rs 0 and pixels per Rs 1K
    rows = [
        ('Alexa range', 4, 9, 'grey', 'Rs 4K to 9K'),
        ('Google Home Mini', 5, 5, 'grey', 'Rs 5K'),
        ('Google Home', 10, 10, 'grey', 'Rs 10K'),
        ('Apple Home Mini', 5.75, 5.75, 'pink', 'Rs 5.75K  (+15%)'),
        ('Apple Home', 11.5, 11.5, 'pink', 'Rs 11.5K  (+15%)'),
    ]
    for i, (lab, lo, hi, c, txt) in enumerate(rows):
        y = 120 + i * 52
        s.text(0, y + 6, lab, 16, INK)
        if hi > lo:
            s.box(x0 + lo * k, y, (hi - lo) * k, 30, None, c, opacity=60)
        else:
            s.box(x0, y, lo * k, 30, None, c, opacity=60)
        s.text(x0 + hi * k + 10, y + 6, txt, 15, PINK if c == 'pink' else GREY, ff=3)
    s.line([(x0, 110), (x0, 384)], color=GREY, sw=1)
    s.box(0, 404, 470, 56, 'two variants cover the low and high ends\n(price-sensitive India)', 'yellow', fs=15, opacity=60)
    s.box(490, 404, 450, 56, 'premium, benchmarked to rivals, not below them', 'purple', fs=15, opacity=35)
    s.text(0, 478, 'premium of about 15%: iPhone 12 vs a comparable Google Pixel', 15, GREY)
    s.save('l20-apple-home-anchors')


# 6 ─ Uber Premier: metric tree and break-even table ─────────────────────────────────────────────────
def d_uber_premier():
    s = Scene()
    title(s, 'Uber Premier: double gross bookings without a deeper discount',
          'gross bookings = trips x fare; promotions move trips but cost money')
    node(s, 120, 84, 240, 56, 'gross bookings\n= trips x fare', 'purple', fs=16, opacity=50)
    s.arrow([(200, 140), (120, 196)], color=GREY, sw=2)
    s.arrow([(240, 140), (340, 196)], color=GREY, sw=2)
    node(s, 20, 196, 170, 40, 'trips', 'orange', fs=16)
    node(s, 290, 196, 170, 40, 'fare', 'orange', fs=16)
    kids_t = [('promotions: a cost per trip', 'red'), ('better app experience', 'blue'),
              ('driver availability', 'blue')]
    kids_f = [('dynamic pricing at peak', 'green'), ('paid add-ons, e.g. Wi-Fi', 'green')]
    for i, (t, c) in enumerate(kids_t):
        y = 262 + i * 46
        s.arrow([(105, 236), (105, y)], color=GREY, sw=1)
        node(s, 20, y, 220, 38, t, c, fs=14, opacity=45)
    for i, (t, c) in enumerate(kids_f):
        y = 262 + i * 46
        s.arrow([(375, 236), (375, y)], color=GREY, sw=1)
        node(s, 290, y, 220, 38, t, c, fs=14, opacity=45)
    s.text(20, 412, 'the trap: promotions raise trips but cost money', 16, RED)
    s.text(20, 438, 'so fare growth comes from value-added services', 16, GREEN)
    # break-even table
    s.text(580, 100, 'fare Rs    25% (cap 50)   15% (cap 100)', 14, INK, ff=3)
    rows = [(200, 50, 30.0), (300, 50, 45.0), (334, 50, 50.1), (400, 50, 60.0), (700, 50, 100.0)]
    for i, (f, a, b) in enumerate(rows):
        y = 124 + i * 40
        better = '25% off' if a > b else '15% off'
        c = 'green' if better == '15% off' else 'blue'
        s.box(580, y, 360, 32, f'{f:>4}       {a:>6.2f}         {b:>7.2f}   {better}',
              c, fs=13, ff=3, opacity=40)
    s.box(580, 344, 340, 40, 'break-even: about Rs 333 (the vault\'s figure)', 'yellow', fs=15, opacity=60)
    s.text(580, 396, 'below Rs 333 the 25% offer wins; above it, 15%', 15, PURPLE)
    s.save('l20-uber-premier')


# 7 ─ cheat sheet: case, type, the move that made it strong ─────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 23 on one page: the marquee case and its winning move',
          'nine cases; each row names the move that made the answer strong')
    s.text(0, 84, 'case', 16, GREY)
    s.text(300, 84, 'type', 16, GREY)
    s.text(470, 84, 'the move that made it strong', 16, GREY)
    rows = [
        ('Delhi Metro (23.1)', 'design', 'one persona, justified; a value vs complexity matrix'),
        ('Gen AI in Google apps (23.1)', 'design, GenAI', 'a shortlist of apps, scored before features'),
        ('Flipkart Hyperlocal (23.1)', 'RCA', 'segment, then split the step that moved'),
        ('Uber Drivers (23.1)', 'RCA', 'decompose income; confirm with a time-of-day cut'),
        ('Google Maps ETA (23.1)', 'RCA', 'verify against actuals, then act in two steps'),
        ('Apple Home (23.1)', 'pricing', 'competitor anchors, then a stated premium'),
        ('LinkedIn, XLRI (23.2)', 'improvement', 'rate impact, pick the two High pains'),
        ('Uber Premier (23.2)', 'growth, pricing', 'trips x fare; the break-even between offers'),
        ('Google Pay (23.3)', 'metrics', 'AARRR order; activation as a payment event'),
    ]
    for i, (case, typ, move) in enumerate(rows):
        y = 112 + i * 42
        s.box(0, y, 280, 34, case, 'orange', fs=14, opacity=50)
        s.box(296, y, 150, 34, typ, 'purple', fs=14, opacity=35)
        s.text(470, y + 8, move, 15, GREEN)
    s.box(0, 494, 940, 40, 'clarify, structure, quantify, then close with a fix and a metric',
          'yellow', fs=16, opacity=60)
    s.save('l20-big-picture')


for f in [d_three_habits, d_flipkart_journey, d_uber_drivers, d_google_maps_eta,
          d_apple_home_anchors, d_uber_premier, d_big_picture]:
    f()

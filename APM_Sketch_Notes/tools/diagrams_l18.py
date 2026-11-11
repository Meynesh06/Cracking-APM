# Excalidraw scenes for Chapter 21 (page 18, l18-*). Run: python3 diagrams_l18.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY
from shelp import title, legend
from scene import tree

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


# 1 ─ the five-step loop ─────────────────────────────────────────────────────────────────────────────
def d_five_steps():
    s = Scene()
    title(s, 'The five-step guesstimate loop',
          '10-15 minutes in total; say every step aloud')
    steps = [
        ('1. Clarify', 'pin down the geography,\ntime period, unit and\ndefinition', '1-2 min'),
        ('2. Segment', 'write the equation before\nany numbers; split into\n2-4 segments', '2-3 min'),
        ('3. Assume', 'one number per term,\neach with a reason\n(experience or benchmark)', '2-3 min'),
        ('4. Compute', 'round numbers; track powers\nof ten apart; write every\nintermediate result', '2-3 min'),
        ('5. Sanity-check', 'test it one more way;\nname the most sensitive\nassumption', '1-2 min'),
    ]
    for i, (head, body, t) in enumerate(steps):
        x = i * 196
        s.box(x, 84, 176, 46, head, 'purple', fs=18, opacity=60)
        s.box(x, 134, 176, 130, body, 'orange', fs=15, opacity=45)
        s.box(x + 36, 278, 104, 30, t, 'yellow', fs=15, opacity=70)
        if i < len(steps) - 1:
            s.arrow([(x + 178, 157), (x + 194, 157)], color=ORANGE, sw=3)
    s.box(0, 336, 940, 44, 'validate the structure after step 2, before any numbers',
          'yellow', fs=17, opacity=45)
    s.box(0, 396, 940, 56, 'close in four parts: the rounded answer, a range,\n'
          'the assumption that moves it most, what you would verify',
          'purple', fs=16, opacity=35)
    s.save('l18-five-steps')


# 2 ─ segmentation tree for the gasoline example ───────────────────────────────────────────────────
def d_gas_tree():
    s = Scene()
    title(s, 'Segment the gasoline equation',
          'spend = cars x gallons per car x price, then split each term')
    root = {'t': 'US gasoline spend\na year', 'c': 'purple', 'w': 220, 'k': [
        {'t': 'cars\n250M (vault figure)', 'c': 'teal', 'w': 176, 'k': [
            {'t': 'homes\n130M (340M / 2.5)', 'c': 'blue', 'w': 170},
            {'t': 'cars per home\n2 (assumed)', 'c': 'blue', 'w': 170},
        ]},
        {'t': 'gallons per car\n500 a year', 'c': 'teal', 'w': 176, 'k': [
            {'t': 'fill-up\n10 gallons a week', 'c': 'blue', 'w': 170},
            {'t': 'weeks\n50 a year', 'c': 'blue', 'w': 170},
        ]},
        {'t': 'price\n$3 a gallon', 'c': 'pink', 'w': 170},
    ]}
    tree(s, root, 0, 90, dx=180, dy=118, w=170, h=60, fs=15, edge_fs=14)
    s.box(0, 440, 900, 52, '125B gallons x $3 = about $375B a year (say $350-400B)',
          'yellow', fs=18, opacity=60)
    s.save('l18-gas-tree')


# 3 ─ the sanity-check triangle ─────────────────────────────────────────────────────────────────────
def d_sanity_triangle():
    s = Scene()
    title(s, 'The sanity-check triangle',
          'test the answer at least one independent way')
    s.box(330, 84, 270, 84, 'per-unit check\n$1,500 a car = $30 a week', 'green', fs=16, opacity=50)
    s.box(0, 330, 300, 84, 'cross-check\nEIA: 9M barrels a day = 135-140B gal',
          'teal', fs=14, opacity=50)
    s.box(620, 330, 300, 84, 'anchor check\ncompare with a known total or\na physical limit', 'blue', fs=14,
          opacity=50)
    s.box(360, 232, 210, 60, 'agree within 2-3x\nis fine', 'yellow', fs=16, opacity=60)
    s.arrow([(400, 170), (180, 330)], color=GREY)
    s.arrow([(520, 170), (760, 330)], color=GREY)
    s.arrow([(302, 372), (618, 372)], color=GREY)
    s.arrow([(465, 168), (465, 230)], color=GREY)
    s.box(0, 440, 940, 50, 'name the most sensitive assumption last',
          'purple', fs=16, opacity=35)
    s.save('l18-sanity-triangle')


# 4 ─ benchmark cheat card ───────────────────────────────────────────────────────────────────────────
def d_benchmarks():
    s = Scene()
    title(s, 'Benchmark cheat card: India and the US',
          'round the numbers, quote the year, say they are approximate')
    s.box(0, 84, 230, 36, 'metric', 'purple', fs=16, opacity=60)
    s.box(240, 84, 330, 36, 'India', 'purple', fs=16, opacity=60)
    s.box(580, 84, 360, 36, 'US', 'purple', fs=16, opacity=60)
    rows = [
        ('population', '~1.45 billion (2024-25)', '~340 million (2024-25)', 'teal'),
        ('internet users', '~950 million (~65%)', '~320 million (~93%)', 'teal'),
        ('smartphone users', '~800 million (700-900M)', '~290-300M (~90% of adults)', 'teal'),
        ('households', '~330M (population / 4.4)', '~133 million (CPS)', 'teal'),
        ('people per household', '~4.4 (NFHS-5)', '~2.5 (Census CPS)', 'teal'),
        ('urban share', '~36% (national definition)', '~83%', 'teal'),
        ('vehicles', '~50% of homes have a two-wheeler', '~92% of homes have a vehicle', 'teal'),
        ('UPI payments', '~24B a month, ~800M a day', 'n/a', 'pink'),
    ]
    for i, (m, ind, us, c) in enumerate(rows):
        y = 126 + i * 40
        s.box(0, y, 230, 34, m, c, fs=15, opacity=35)
        s.box(240, y, 330, 34, ind, c, fs=15, opacity=25)
        s.box(580, y, 360, 34, us, c, fs=15, opacity=25)
    s.box(0, 460, 940, 40, 'say "about 1.45 billion, as of 2025" and the source',
          'yellow', fs=16, opacity=55)
    s.save('l18-benchmarks')


# 5 ─ AI cost stack: tokens to dollars ──────────────────────────────────────────────────────────────
def d_ai_cost_stack():
    s = Scene()
    title(s, 'AI cost stack: from tokens to dollars',
          'keep input and output apart; compare with revenue')
    items = [
        ('active users x requests x tokens', 'teal', '5M DAU x 10% = 500K feature users'),
        ('tokens a day, input and output apart', 'teal', '2B a day: 1.5B in, 0.5B out'),
        ('input x $1 + output x $4 per million', 'orange', '1.5B x $1 + 0.5B x $4 (assumed prices)'),
        ('API cost a day', 'pink', '$3,500 a day'),
        ('API cost a month', 'pink', '$3,500 x 30 = $105,000 a month'),
        ('cost per feature user a month', 'yellow', '$105,000 / 500K = $0.21 a user'),
    ]
    for i, (lab, c, note) in enumerate(items):
        y = 84 + i * 68
        s.box(0, y, 500, 50, lab, c, fs=16, opacity=50)
        s.text(520, y + 14, note, 15, GREY, ff=3)
        if i < len(items) - 1:
            s.arrow([(250, y + 52), (250, y + 66)], color=ORANGE, sw=2)
    s.save('l18-ai-cost-stack')


# 6 ─ mental-math tactics ───────────────────────────────────────────────────────────────────────────
def d_mental_math():
    s = Scene()
    title(s, 'Mental-math tactics', 'round early, keep powers of ten apart, write each step')
    tiles = [
        ('Round to friendly numbers', '1.45B -> 1.5B, 365 -> 350', 'one factor up, one down'),
        ('Scientific notation', '2.4 x 1.2 x 2 = 5.76', 'exponents 9 + 2 + 6 = 17'),
        ('Fast division', '300M / 4: halve twice = 75M', '340 / 5: double, then / 10'),
        ('Constants', '86,400 s a day, about 10^5', '8,760 hours a year, about 9,000'),
        ('Indian units', '1 crore = 10M, 1 lakh = 100K', '1.45B = 145 crore'),
        ('Check as you go', 'write the unit next to each number', 'bracket it: a low and a high case'),
    ]
    for i, (head, a, b) in enumerate(tiles):
        x = (i % 3) * 320
        y = 84 + (i // 3) * 170
        s.box(x, y, 300, 150, head + '\n' + a + '\n' + b, 'orange', fs=15, opacity=40)
    s.box(0, 430, 940, 48, 'more than two steps? write them down, not in your head',
          'yellow', fs=17, opacity=55)
    s.save('l18-mental-math')


# 7 ─ chapter on one page ───────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 21 on one page: five ideas, five questions',
          'loop, anchors, four types, AI conversions, mental math')
    cols = [
        ('21.1 Five-step loop', 'clarify, segment, assume,\ncompute, sanity-check', 'where is the most sensitive input?', 'orange'),
        ('21.2 Anchors', 'round benchmarks with a year\nand a source type', 'does a derived figure agree?', 'teal'),
        ('21.3 Four types', 'market, users, storage,\nsupply and capacity', 'which unit, and which peak?', 'teal'),
        ('21.4 AI conversions', 'tokens, prices, FLOPs,\nbytes per dimension', 'what does one call cost?', 'pink'),
        ('21.5 Mental math', 'round, powers of ten,\ncheck as you go', 'does it pass two checks?', 'orange'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 192
        s.box(x, 84, 182, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 182, 110, core, c, fs=15, opacity=45)
        s.box(x, 280, 182, 92, q, 'yellow', fs=15, opacity=60)
    s.box(10, 392, 940, 58, 'a good guesstimate: a structure, stated assumptions, a check',
          'purple', fs=17, opacity=35)
    s.box(10, 462, 940, 36, 'the reasoning is graded more than the final figure', 'green', fs=15,
          opacity=45)
    s.save('l18-big-picture')


for f in [d_five_steps, d_gas_tree, d_sanity_triangle, d_benchmarks, d_ai_cost_stack,
          d_mental_math, d_big_picture]:
    f()

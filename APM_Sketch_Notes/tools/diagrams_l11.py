# Excalidraw scenes for Chapter 14 (page 11, l11-*). Run: python3 diagrams_l11.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)


# 1 ─ RICE formula and factor scales ──────────────────────────────────────────────────────────────
def d_rice_formula():
    s = Scene()
    title(s, 'RICE: four judgments, one comparable score',
          'score = reach x impact x confidence / effort')
    cols = [
        ('REACH', 'how many, per quarter', ['customers or', 'transactions per', 'fixed period']),
        ('IMPACT', 'how much per person', ['3 = massive', '2 = high', '1 = medium', '0.5 = low', '0.25 = minimal']),
        ('CONFIDENCE', 'how sure are we?', ['100% = high', '80% = medium', '50% = low', 'under 50% = moonshot']),
        ('EFFORT', 'team time, all roles', ['person-months across', 'product, design, eng', '0.5 for tiny work']),
    ]
    for i, (head, q, scale) in enumerate(cols):
        x = i * 226
        s.box(x, 100, 214, 66, f'{head}\n{q}', 'purple', fs=16, opacity=55)
        s.box(x, 180, 214, 130, '\n'.join(scale), 'grey', fs=15, opacity=45)
    s.box(0, 332, 892, 56, 'RICE = (Reach x Impact x Confidence) / Effort', 'yellow', fs=20, opacity=70)
    s.text(0, 404, 'reach is breadth, impact is depth: do not double-count', 16, INK)
    s.text(0, 430, 'confidence discounts weak evidence, so the list stays honest', 16, INK)
    s.text(0, 456, 'effort is the denominator: a cheap, moderate idea can win', 16, INK)
    s.save('l11-rice-formula')


# 2 ─ RICE ranking on the worked example ──────────────────────────────────────────────────────────
def d_rice_ranking():
    s = Scene()
    title(s, 'RICE on the food-delivery example: one-tap reorder wins',
          'one quarter; the scores from the vault worked mini-example')
    rows = [
        ('reorder last meal in one tap', 80000, 'green',
         'reach 200,000 x impact 1 x 80% / 2 = 80,000'),
        ('dark mode', 33333, 'grey',
         'reach 500,000 x 0.25 x 80% / 3 = 33,333'),
        ('group ordering for offices', 5000, 'red',
         'reach 20,000 x 2 x 50% / 4 = 5,000'),
    ]
    k = 560 / 80000
    for i, (name, score, c, note) in enumerate(rows):
        y = 120 + i * 92
        s.text(0, y, name, 17, INK)
        w = score * k
        s.box(0, y + 28, w, 34, None, c, opacity=70)
        s.text(w + 12, y + 32, f'{score:,}', 18, INK, ff=3)
        s.text(0, y + 68, note, 14, GREY, ff=3)
    s.box(0, 420, 920, 44, 'the ranking follows impact and effort more than reach', 'yellow', fs=17, opacity=65)
    s.text(0, 478, 'beyond · at 100% confidence group ordering scores 10,000', 15, GREY)
    s.save('l11-rice-ranking')


# 3 ─ value vs effort 2x2 ─────────────────────────────────────────────────────────────────────────
def d_value_effort():
    s = Scene()
    title(s, 'Value vs effort: four quadrants, four decisions',
          'ride-hailing ideas placed on the grid (a simplified RICE)')
    X0, Y0, W, H = 130, 100, 380, 150
    quads = [
        (0, 0, 'quick wins: do first', 'show driver photo on booking', 'green'),
        (1, 0, 'big bets: plan, slice, de-risk', 'in-app wallet with cashback', 'orange'),
        (0, 1, 'fill-ins: do if idle', 'new splash animation', 'grey'),
        (1, 1, 'money pits: avoid', 'build own maps stack', 'red'),
    ]
    for cx, cy, head, idea, c in quads:
        x = X0 + cx * (W + 10)
        y = Y0 + cy * (H + 10)
        s.box(x, y, W, H, None, c, opacity=35)
        s.text(x + 14, y + 12, head, 18, INK)
        s.box(x + 14, y + 56, W - 28, 44, idea, 'blue', fs=16, opacity=60)
    s.text(0, Y0 + 40, 'high value', 16, PURPLE)
    s.text(0, Y0 + H + 10 + 50, 'low value', 16, PURPLE)
    s.text(X0, Y0 + 2 * H + 30, 'low effort', 16, PURPLE)
    s.text(X0 + W + 10, Y0 + 2 * H + 30, 'high effort', 16, PURPLE)
    s.text(0, 462, 'quick visual alignment; weaker than RICE for many items', 16, INK)
    s.save('l11-value-effort')


# 4 ─ Kano: five categories as curves ─────────────────────────────────────────────────────────────
def d_kano():
    s = Scene()
    title(s, 'Kano: five categories, five shapes of satisfaction',
          'satisfaction against how well the feature is built')
    ox, oy, LX, LY = 120, 410, 430, 290
    px = lambda f: ox + f * LX
    py = lambda v: oy - (v + 1) / 2 * LY          # v from -1 (dissatisfied) to +1 (satisfied)
    s.line([(ox, oy), (ox + LX, oy)], color=PURPLE, sw=2)
    s.line([(ox, oy), (ox, oy - LY)], color=PURPLE, sw=2)
    s.line([(ox, py(0)), (ox + LX, py(0))], color=GREY, dashed=True, sw=1)
    s.text(ox + 40, oy + 14, 'how well it is built: not done -> done very well', 14, PURPLE)
    s.text(8, oy - LY - 6, 'satisfied', 14, PURPLE)
    s.text(8, oy - 6, 'dissatisfied', 14, PURPLE)
    N = 24
    fs_ = [i / N for i in range(N + 1)]
    curves = [
        ('expected', BLUE, False, lambda f: -0.9 + 1.0 * f ** 0.3),
        ('performance', TEAL, False, lambda f: -1 + 2 * f),
        ('exciting', GREEN, False, lambda f: -0.05 + 1.05 * f ** 3),
        ('indifferent', GREY, False, lambda f: 0.0),
        ('reverse', RED, True, lambda f: 0.7 - 1.5 * f),
    ]
    for name, col, dash, fn in curves:
        pts = [(px(f), py(fn(f))) for f in fs_]
        s.line(pts, color=col, dashed=dash, sw=3)
    s.text(px(1) - 40, py(0.1) - 26, 'expected', 14, BLUE)
    s.text(px(1) - 110, py(1) - 22, 'exciting', 14, GREEN)
    s.text(px(0.55), py(-0.33) + 6, 'performance', 14, TEAL)
    s.text(px(0.15), py(0) - 24, 'indifferent', 14, GREY)
    s.text(px(0.3), py(0.45) - 4, 'reverse', 14, RED)
    # legend
    lx = 590
    items = [('blue', 'expected: absence hurts'), ('teal', 'performance: more is better'),
             ('green', 'exciting: presence delights'), ('grey', 'indifferent: barely noticed'),
             ('red', 'reverse: some users dislike it')]
    for i, (c, t) in enumerate(items):
        y = 120 + i * 40
        s.box(lx, y + 4, 18, 18, None, c)
        s.text(lx + 28, y, t, 16, INK)
    s.text(lx, 340, 'Kano names in brackets: must-be, one-dimensional,', 14, GREY)
    s.text(lx, 360, 'attractive, indifferent, reverse', 14, GREY)
    s.text(0, 462, 'the shape of each curve, not a score, is the lesson', 16, INK)
    s.save('l11-kano-curves')


# 5 ─ MoSCoW buckets and the 60% rule ─────────────────────────────────────────────────────────────
def d_moscow():
    s = Scene()
    title(s, 'MoSCoW: four buckets and the 60% effort rule',
          'Must-haves take about 60% of effort; the rest is contingency')
    buckets = [
        ('MUST-have', ['essential: without it the', 'product cannot launch'],
         ['e.g. user login'], 'purple'),
        ('SHOULD-have', ['important, but a workaround', 'exists at launch'],
         ['e.g. reset password', '(support resets it by hand', 'at first)'], 'blue'),
        ('COULD-have', ['desirable; can wait for a', 'later timeframe'],
         ['e.g. single sign-on'], 'teal'),
        ("WON'T-have (this time)", ['least critical; kept for', 'future releases, not dropped', 'forever'],
         ['sets expectations'], 'grey'),
    ]
    for i, (head, desc, ex, c) in enumerate(buckets):
        x = i * 235
        s.box(x, 100, 220, 200, None, c, opacity=35)
        s.text(x + 12, 110, head, 16, INK)
        for j, line in enumerate(desc):
            s.text(x + 12, 142 + j * 22, line, 14, INK)
        for j, line in enumerate(ex):
            s.text(x + 12, 226 + j * 20, line, 14, GREY, ff=3)
    s.box(0, 330, 552, 50, 'Must: about 60% of effort at most', 'purple', fs=17, opacity=60)
    s.box(552, 330, 368, 50, 'Should + Could: about 40%, the buffer', 'blue', fs=16, opacity=50)
    s.text(0, 398, 'if nearly everything is a Must, nothing is prioritised', 16, RED)
    s.text(0, 426, 'context changes the bucket: SSO is a Could for an early', 16, INK)
    s.text(0, 450, 'consumer app, a Must for enterprise SaaS (IT buyers)', 16, INK)
    s.save('l11-moscow')


# 6 ─ ICE scores as a small table ─────────────────────────────────────────────────────────────────
def d_ice():
    s = Scene()
    title(s, 'ICE: the average of impact, confidence and ease',
          'onboarding experiments from the vault, each factor scored 1 to 10')
    for x, lab in ((300, 'impact'), (380, 'conf.'), (460, 'ease'), (560, 'average')):
        s.text(x, 92, lab, 15, GREY)
    rows = [
        ('add social login', (7, 8, 6)),
        ('personalised first-week emails', (6, 5, 8)),
        ('redesign the whole onboarding flow', (9, 4, 2)),
    ]
    for i, (name, (imp, conf, ease)) in enumerate(rows):
        y = 120 + i * 70
        s.text(0, y + 14, name, 17, INK)
        for x, v in ((300, imp), (380, conf), (460, ease)):
            s.box(x, y, 60, 50, str(v), 'blue', fs=18, ff=3, opacity=60)
        avg = (imp + conf + ease) / 3
        s.box(560, y, 110, 50, f'{avg:.1f}', 'green' if i == 0 else 'grey', fs=18, ff=3, opacity=65)
    s.box(0, 330, 920, 44, 'ICE = (impact + confidence + ease) / 3   (Sigma convention)', 'yellow', fs=18, opacity=65)
    s.text(0, 396, '- run social login first (7.0)', 16, INK)
    s.text(0, 422, '- score in a group, then discuss the outliers', 16, INK)
    s.text(0, 448, '- keep one metric behind each score', 16, INK)
    s.text(470, 396, '- re-score after each experiment result', 16, INK)
    s.text(470, 422, '- confidence is often a guess: tie it to evidence', 16, RED)
    s.text(470, 448, 'beyond · I x C x E gives 336, 240, 72: same order', 15, GREY)
    s.save('l11-ice')


# 7 ─ which framework when ────────────────────────────────────────────────────────────────────────
def d_which_framework():
    s = Scene()
    title(s, 'Which framework when: match the question you are answering',
          'the decision chooses the framework, not the other way round')
    rows = [
        ('many competing features, need one comparable score', 'RICE'),
        ('quick visual alignment in a workshop', 'value vs effort'),
        ('which features drive satisfaction?', 'Kano'),
        ('what is in or out of this release?', 'MoSCoW'),
        ('fast ranking of growth experiments', 'ICE'),
        ('time-sensitive work where delay has a cost', 'cost of delay (WSJF)'),
    ]
    for i, (q, f) in enumerate(rows):
        y = 100 + i * 52
        s.box(0, y, 470, 42, q, 'blue', fs=15, opacity=50)
        s.arrow([(480, y + 21), (520, y + 21)], color=GREY, sw=2)
        s.box(530, y, 390, 42, f, 'purple', fs=17, opacity=60)
    s.box(0, 416, 920, 40, 'combine: MoSCoW for scope, RICE to order the Should and Could', 'yellow', fs=16, opacity=60)
    s.text(0, 464, 'ICE for weekly growth experiments (illustrative combination)', 15, GREY)
    s.text(0, 490, 'a framework used to hide a preference is a mistake', 15, RED)
    s.save('l11-which-framework')


# 8 ─ big picture cheat sheet ─────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 14 on one page: six tools, one habit',
          'every score shows its weakest assumption')
    cards = [
        ('RICE', 'reach x impact x\nconfidence / effort\nmany items, one score',
         'is the reach real?\nis confidence honest?'),
        ('Value vs effort', 'value and effort on\na 2x2: quick wins,\nbig bets, fill-ins,\npits',
         'can the effort be\nsplit into a slice?'),
        ('Kano', 'expected\nperformance\nexciting\nindifferent, reverse',
         'is it expected,\nor does it delight?'),
        ('MoSCoW', 'Must, Should,\nCould, Won\'t\nMust: <= 60% effort',
         'if we launch without\nit, does it still work?'),
        ('ICE', 'impact, confidence,\nease: 1 to 10 each\naverage for tests',
         'which assumption is\ncheapest to test?'),
        ('Choosing', 'state the decision\nname the framework\nshow weakest input',
         'would the ranking\nchange if one input did?'),
    ]
    for i, (head, body, foot) in enumerate(cards):
        x = 10 + i * 152
        s.box(x, 90, 146, 50, head, 'purple', fs=15, opacity=60)
        s.box(x, 150, 146, 150, body, 'blue', fs=13, opacity=40)
        s.box(x, 310, 146, 80, foot, 'yellow', fs=13, opacity=55)
    s.box(10, 410, 940, 56, 'name the decision, pick a framework, show the inputs, say how you revisit it',
          'green', fs=16, opacity=40)
    s.save('l11-big-picture')


for f in [d_rice_formula, d_rice_ranking, d_value_effort, d_kano, d_moscow, d_ice,
          d_which_framework, d_big_picture]:
    f()

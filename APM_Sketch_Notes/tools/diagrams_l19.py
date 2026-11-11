# Excalidraw scenes for Chapter 22 (page 19, l19-*). Run: python3 diagrams_l19.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


def ladder(s, steps, x=20, y0=100, name_w=300, step_h=40, gap=8, color='orange', out_color=GREY):
    """A step ladder: numbered rungs stepping down; the output of each step is written to the right."""
    for i, (name, out) in enumerate(steps):
        y = y0 + i * (step_h + gap)
        s.box(x + i * 14, y, name_w, step_h, f'{i + 1}. {name}', color, fs=16, opacity=60)
        s.text(x + i * 14 + name_w + 18, y + step_h / 2 - 9, out, 15, out_color)


# 1 ─ which case type is this? ────────────────────────────────────────────────────────────────────
def d_which_case():
    s = Scene()
    title(s, 'Which case type is this?',
          'read the verb in the first sentence of the prompt, then pick its framework')
    rows = [
        ('"design", "build", "a product for"', 'Product design', 'CIRCLES'),
        ('"improve", "critique", "make better"', 'Improvement', 'five-step critique'),
        ('"dropped", "rose", "why did it move"', 'Root cause (RCA)', 'scope, then the journey'),
        ('"measure", "success", "north star"', 'Metrics', 'funnel, north star, guardrails'),
        ('"price", "charge", "what should it cost"', 'Pricing', 'willingness to pay, range'),
        ('"enter", "should we", "which market"', 'Strategy and entry', 'forces, competitors, fit'),
        ('"launch", "roll out", "first 90 days"', 'Go-to-market', 'segment, pilot, channels'),
        ('"brainstorm", "sell me", "as many as"', 'Brainstorming', 'structure, then prioritise'),
    ]
    for i, (prompt, case, fw) in enumerate(rows):
        y = 104 + i * 50
        s.box(0, y, 360, 40, prompt, 'grey', fs=14, opacity=50)
        s.arrow([(366, y + 20), (420, y + 20)], color=ORANGE, sw=2)
        s.box(426, y, 250, 40, case, 'orange', fs=15, opacity=55)
        s.text(690, y + 11, fw, 14, PURPLE)
    s.box(0, 512, 940, 40, 'say the case type out loud, then start the framework',
          'yellow', fs=16, opacity=60)
    s.save('l19-which-case')


# 2 ─ the design ladder (CIRCLES) ─────────────────────────────────────────────────────────────────────
def d_ladder_design():
    s = Scene()
    title(s, 'Product design: the CIRCLES ladder',
          'eight steps; each one ends with an output you can say out loud')
    ladder(s, [
        ('Comprehend', 'restate the prompt; ask platform, geography, goal'),
        ('Identify the user', 'stakeholders, then one primary persona'),
        ('Report needs', 'the persona journey, its pains and jobs'),
        ('Cut', '1-2 pains ranked on frequency, severity, impact'),
        ('List solutions', 'three distinct ideas per chosen pain'),
        ('Evaluate and pick', 'value vs effort or RICE; the build-first one'),
        ('Measure', 'one success metric and two guardrails'),
        ('Summarise', 'persona, pain, solution, metric, risk, MVP cut'),
    ], color='orange')
    s.box(0, 484, 940, 40, 'skip the features until step 5; never skip step 7', 'yellow', fs=16, opacity=60)
    s.save('l19-ladder-design')


# 3 ─ the RCA ladder ─────────────────────────────────────────────────────────────────────────────────
def d_ladder_rca():
    s = Scene()
    title(s, 'Root cause analysis: scope first, then zoom in',
          'a metric moved; split the causes, walk the journey, confirm with one cut')
    ladder(s, [
        ('Define the metric', 'confirm what "active" or "conversion" means'),
        ('Scope it', 'how big, since when, sudden or gradual, where'),
        ('External causes', 'competitors, season, rules, PR, partners'),
        ('Walk the journey', 'one metric per step: which step moved?'),
        ('Zoom in', 'recent change at that step: release, price, policy'),
        ('Confirm with one cut', 'a single data cut beats five guesses'),
        ('Is it actually bad?', 'check the downstream metric'),
        ('Fix and prevent', 'rollback, long-term fix, a test or an alert'),
    ], color='orange')
    s.box(0, 484, 940, 40, 'a city-only drop points away from global releases', 'yellow', fs=16, opacity=60)
    s.save('l19-ladder-rca')


# 4 ─ the metrics ladder ─────────────────────────────────────────────────────────────────────────────
def d_ladder_metrics():
    s = Scene()
    title(s, 'Metrics cases: a goal, a funnel, one north star',
          'supporting metrics explain the north star; guardrails protect the rest')
    ladder(s, [
        ('Clarify the goal', 'product, both sides, which business goal now'),
        ('Map the funnel', 'one metric per stage (AARRR or AARM)'),
        ('Cross out', 'drop the stages the change cannot move'),
        ('Choose one north star', 'delivered value, with a one-line reason'),
        ('Add 2-3 supporting', 'explain the movement in the north star'),
        ('Add guardrails', 'sign-ups, complaints, refunds, latency, cost'),
        ('Read the trade-off', 'which result ships, which result stops'),
        ('Set target and window', '"+5% in 30-day retention over 4 weeks"'),
    ], color='orange')
    s.box(0, 484, 940, 40, 'avoid vanity metrics: total signups without retention', 'red', fs=16, opacity=35)
    s.save('l19-ladder-metrics')


# 5 ─ the pricing ladder ─────────────────────────────────────────────────────────────────────────────
def d_ladder_pricing():
    s = Scene()
    title(s, 'Pricing: willingness to pay first, then the range',
          'cost sets the floor; the substitute and the value set the ceiling')
    ladder(s, [
        ('Clarify', 'buyer, product, new category or a competitive one'),
        ('Willingness to pay', 'value to the customer, or rival price + gap'),
        ('Cost floor', 'unit cost; cost-plus is a sanity check only'),
        ('Pick the strategy', 'penetration, skimming, premium, bundle, freemium'),
        ('Set the range', 'cost or cheapest substitute to value or premium rival'),
        ('Segment', 'tiers by user type or feature set'),
        ('Test', 'A/B price test; surveys are optimistic about price'),
        ('Name the risks', 'churn, anchoring, cannibalisation, regulation'),
    ], color='pink', name_w=300)
    s.box(0, 484, 940, 40, 'the price sits inside the range, and you say why', 'yellow', fs=16, opacity=60)
    s.save('l19-ladder-pricing')


# 6 ─ the Kindle range ──────────────────────────────────────────────────────────────────────────────
def d_pricing_range():
    s = Scene()
    title(s, 'Kindle Fire HD: the range and the price chosen',
          'the closest substitute caps the price; the cost floor sets the bottom')
    px = lambda v: 80 + (v - 150) * (800 / 70)     # $150 .. $220 across 800 px
    base = 260
    s.line([(px(150), base), (px(220), base)], color=GREY, sw=3)
    for v in (150, 175, 200, 220):
        s.line([(px(v), base - 8), (px(v), base + 8)], color=GREY, sw=2)
        s.text(px(v) - 16, base + 14, f'${v}', 15, GREY, ff=3)
    s.box(px(174), base - 16, px(199) - px(174), 32, None, 'green', opacity=55)
    s.text(px(174) + 10, base - 50, 'range: $174 to $199', 17, GREEN)
    s.line([(px(174), base - 16), (px(174), base - 96)], color=PINK, sw=2)
    s.box(px(174) - 150, base - 150, 300, 56, 'cost floor: $174 per unit\n(teardown estimate)', 'pink', fs=15, opacity=45)
    s.line([(px(199), base - 16), (px(199), base - 96)], color=TEAL, sw=2)
    s.box(px(199) - 60, base - 150, 300, 56, 'closest substitute:\nNexus 7 at $199', 'teal', fs=15, opacity=45)
    s.box(px(174) - 10, base + 50, 420, 60, 'chosen: $174, the low end,\nas a loss leader (razor and blade)', 'yellow', fs=16, opacity=60)
    s.text(0, 440, 'Amazon profits from digital content and needs tablet share.', 16, PURPLE)
    s.text(0, 466, 'The cost floor is the bottom; the substitute is the top.', 16, INK)
    s.save('l19-pricing-range')


# 7 ─ big picture: case type -> framework -> chapter ──────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 22 on one page: case type, framework, chapter',
          'eight case types; each has a framework and a chapter that teaches it')
    s.text(0, 84, 'case type', 16, GREY)
    s.text(300, 84, 'framework to reach for', 16, GREY)
    s.text(640, 84, 'where it is taught', 16, GREY)
    rows = [
        ('Product design', 'CIRCLES + measure (8 steps)', 'Chapter 12 (with 11, 14)'),
        ('Improvement', 'five-step critique, zoom levels', 'Chapter 13 (with 11, 14, 15)'),
        ('Root cause (RCA)', 'scope, then walk the journey', 'Chapter 16 (with 15)'),
        ('Metrics', 'north star, funnel, guardrails', 'Chapter 15'),
        ('Pricing', 'willingness to pay, cost floor, range', 'Chapter 17'),
        ('Strategy and entry', 'Five Forces, SWOT, Five Cs', 'Chapter 19 (with 21 for sizing)'),
        ('Go-to-market', 'pre-launch, launch, post-launch', 'Chapter 18'),
        ('Brainstorming', 'structure, then RICE or value vs effort', 'Chapter 14 (with 12)'),
    ]
    for i, (case, fw, ch) in enumerate(rows):
        y = 112 + i * 48
        s.box(0, y, 260, 38, case, 'orange', fs=15, opacity=55)
        s.arrow([(266, y + 19), (290, y + 19)], color=GREY, sw=2)
        s.box(296, y, 320, 38, fw, 'purple', fs=14, opacity=40)
        s.arrow([(622, y + 19), (646, y + 19)], color=GREY, sw=2)
        s.box(652, y, 288, 38, ch, 'zblue', fs=14, opacity=50)
    s.box(0, 500, 940, 40, 'the first step is the same for every type: clarify, then the framework',
          'yellow', fs=16, opacity=60)
    s.save('l19-big-picture')


for f in [d_which_case, d_ladder_design, d_ladder_rca, d_ladder_metrics, d_ladder_pricing,
          d_pricing_range, d_big_picture]:
    f()

# Excalidraw scenes for Chapter 4 (page 1, l1-*). Run: python3 diagrams_l1.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


def panel_head(s, x, y, text, color=PURPLE, fs=20):
    s.text(x, y, text, fs, color)


# 1 ─ deterministic vs probabilistic ──────────────────────────────────────────────────────────────────
def d_deterministic_vs_probabilistic():
    s = Scene()
    title(s, 'Deterministic vs probabilistic',
          'a rule gives one answer every time; a model gives the most likely answer')
    # (sub-title kept under 75 characters)
    # left: deterministic
    panel_head(s, 0, 84, 'deterministic software')
    s.box(0, 120, 130, 66, 'input X', 'blue', fs=18)
    s.arrow([(132, 153), (168, 153)], color=ORANGE, sw=3)
    s.box(170, 120, 150, 66, 'rule written\nby an engineer', 'purple', fs=16, opacity=60)
    s.arrow([(322, 153), (358, 153)], color=ORANGE, sw=3)
    s.box(360, 120, 120, 66, 'output Y\nalways', 'green', fs=16, opacity=55)
    s.box(0, 214, 480, 56, 'a bug is reproducible: change the code and it is gone', 'green', fs=17, opacity=35)
    # divider
    s.line([(500, 84), (500, 280)], color=GREY, sw=1)
    # right: probabilistic
    panel_head(s, 520, 84, 'probabilistic software (AI)')
    s.box(520, 120, 120, 66, 'input X', 'blue', fs=18)
    s.arrow([(642, 153), (668, 153)], color=ORANGE, sw=3)
    s.box(670, 120, 200, 66, 'a model learned\nfrom data', 'teal', fs=16, opacity=60)
    s.arrow([(770, 188), (770, 212)], color=ORANGE, sw=3)
    s.text(520, 214, 'a distribution over outputs:', 16, INK)
    s.box(520, 240, 300, 24, 'A: most likely (shown)', 'yellow', fs=14, opacity=80)
    s.box(520, 268, 200, 24, 'B: plausible', 'grey', fs=14, opacity=60)
    s.box(520, 296, 110, 24, 'C: rare', 'grey', fs=14, opacity=60)
    s.box(830, 240, 130, 80, 'right, wrong\nor partly right', 'red', fs=14, opacity=30)
    # bottom band: what changes for a PM
    s.box(0, 346, 960, 124, None, 'purple', opacity=30)
    s.text(16, 356, 'what changes for a PM', 20, PURPLE)
    s.text(16, 388, 'success is a rate: "works 92% of the time on this task" is the spec', 17, INK)
    s.text(16, 414, 'every output needs an acceptance bar, e.g. "no invented facts"', 17, INK)
    s.text(16, 440, 'some failures are expected at the tail, so design plans for them (see 4.5)', 17, INK)
    s.save('l1-deterministic-vs-probabilistic')


# 2 ─ the data flywheel ───────────────────────────────────────────────────────────────────────────────
def d_flywheel():
    s = Scene()
    title(s, 'The data flywheel: a loop that must be closed and clean',
          'usage gives feedback, feedback improves the model, the product draws users')
    s.box(20, 100, 200, 66, 'more users', 'blue', fs=18)
    s.box(260, 100, 200, 66, 'usage data\nfrom feedback', 'teal', fs=16, opacity=60)
    s.box(260, 300, 200, 66, 'retrain or re-tune,\nthen measure it', 'orange', fs=16, opacity=55)
    s.box(20, 300, 200, 66, 'better product\nattracts more users', 'green', fs=16, opacity=50)
    s.arrow([(222, 133), (256, 133)], color=GREY, sw=3)
    s.arrow([(360, 168), (360, 296)], color=GREY, sw=3)
    s.arrow([(256, 333), (224, 333)], color=GREY, sw=3)
    s.arrow([(120, 298), (120, 170)], color=GREY, sw=3)
    s.text(140, 214, 'closed loop', 18, PURPLE)
    # right panel
    s.text(500, 100, 'the loop only works when', 19, PURPLE)
    lines = ['feedback is a by-product of normal use',
             'the signal is specific to the task',
             'the team retrains or re-tunes and measures',
             'users consented to the data use']
    for i, t in enumerate(lines):
        s.text(516, 130 + i * 26, '+ ' + t, 16, GREEN)
    s.text(500, 254, 'common traps', 19, RED)
    traps = ['feedback bias: only angry users click thumbs-down',
             'logging without labels: data with no ground truth',
             'diminishing returns on raw volume']
    for i, t in enumerate(traps):
        s.text(516, 284 + i * 26, '- ' + t, 16, RED)
    s.box(0, 404, 960, 64, 'interview framing: name the data source, the signal, the label, the loop, and the consent',
          'purple', fs=17, opacity=30)
    s.save('l1-flywheel')


# 3 ─ quality as a distribution ─────────────────────────────────────────────────────────────────────
def d_quality_distribution():
    s = Scene()
    title(s, 'Quality is a distribution, not a bug count',
          'the average can look fine while a segment and the tail fail')
    # histogram
    panel_head(s, 0, 84, 'quality score per output (rubric 1 to 5), illustrative shape', INK, 17)
    base = 400
    heights = [46, 92, 150, 240, 170]
    for i, h in enumerate(heights):
        color = 'red' if i < 2 else 'teal'
        s.box(40 + i * 84, base - h, 70, h, None, color, opacity=70)
        s.text(40 + i * 84 + 26, base + 8, str(i + 1), 16, INK, ff=3)
    s.line([(30, base), (490, base)], color=INK, sw=2)
    # average line (sits near the bulk, so the average looks fine)
    avg_x = 40 + 3 * 84 + 35
    s.line([(avg_x, 150), (avg_x, base)], color=YEL, dashed=True, sw=2)
    s.text(avg_x + 6, 128, 'average: looks fine', 16, YEL)
    s.text(40, 432, 'red = the tail: the worst 1% to 5% drive complaints', 16, RED)
    # right: cuts that matter
    panel_head(s, 540, 84, 'the cuts that matter', PURPLE, 19)
    segs = [('English, short inputs', 'green', 420), ('English, long inputs', 'green', 340),
            ('a second language', 'red', 170), ('new user cohort', 'orange', 260)]
    for i, (lab, c, w) in enumerate(segs):
        y = 124 + i * 46
        s.text(540, y, lab, 15, INK)
        s.box(540, y + 22, w, 20, None, c, opacity=60)
    s.text(540, 318, 'severity weighs failures', 19, PURPLE)
    s.box(540, 350, 200, 40, 'stylistic slip', 'grey', fs=15, opacity=60)
    s.box(760, 350, 200, 40, 'wrong medical, legal\nor payment answer', 'red', fs=14, opacity=50)
    s.box(0, 460, 960, 34, 'define the bar, not the average: >= 95% correct on the golden set, and 0 critical safety failures',
          'yellow', fs=15, opacity=70)
    s.save('l1-quality-distribution')


# 4 ─ latency: time to first token vs tokens per second ───────────────────────────────────────────────
def d_latency():
    s = Scene()
    title(s, 'Latency: time to first token, then tokens per second',
          'a 500-token answer at 50 tokens/s takes about 10 s')

    def px(t):
        return 150 + t * 62

    # row 1: no streaming
    s.text(0, 128, 'no streaming', 18, INK)
    s.text(px(0), 124, 'the user sees nothing until the end', 15, GREY)
    s.box(px(0), 150, px(10.8) - px(0), 50, 'waiting ...', 'grey', fs=16, style='hachure', opacity=70)
    s.box(px(10.8) + 6, 150, 96, 50, 'answer', 'green', fs=15, opacity=55)
    # row 2: streaming
    s.text(0, 240, 'streaming', 18, INK)
    s.text(px(0), 222, 'first token at 0.8 s: time to first token (TTFT)', 15, ORANGE)
    s.box(px(0), 250, px(0.8) - px(0), 50, None, 'orange', opacity=75)
    for i in range(10):
        s.box(px(0.8) + i * 62, 250, 60, 50, '50', 'teal', fs=13, ff=3, opacity=65)
    s.text(px(0.8), 306, 'then about 50 tokens every second (tokens per second)', 15, PURPLE)
    s.box(px(10.8) + 6, 250, 96, 50, 'done', 'green', fs=15, opacity=55)    # axis
    s.line([(px(0), 340), (px(11), 340)], color=GREY, sw=2)
    for t in (0, 2, 4, 6, 8, 10):
        s.line([(px(t), 336), (px(t), 344)], color=GREY, sw=2)
        s.text(px(t) - 8, 350, str(t), 14, GREY, ff=3)
    s.text(px(11) - 8, 350, 's', 14, GREY, ff=3)
    s.box(0, 384, 960, 56, 'streaming does not shorten the 10 s; it moves the first visible word to 0.8 s',
          'yellow', fs=17, opacity=60)
    s.text(0, 462, 'reasoning ("thinking") models add a hidden delay before the first visible token', 16, RED)
    s.save('l1-latency')


# 5 ─ cost per query and capacity ─────────────────────────────────────────────────────────────────────
def d_cost_capacity():
    s = Scene()
    title(s, 'Cost per query and capacity: check both numbers',
          'cost grows with tokens and retries; the peak sizes capacity')
    # left: cost stack
    panel_head(s, 0, 84, 'cost of one query', PINK, 19)
    base = 380
    stack = [('input tokens: prompt + retrieved text', 120, 'pink'),
             ('output tokens: the answer', 70, 'pink'),
             ('retries, agent sub-calls', 36, 'pink')]
    y = base
    for lab, h, c in stack:
        y -= h
        s.box(20, y, 120, h, None, c, opacity=55)
        s.text(160, y + h / 2 - 9, lab, 14, INK)
    s.text(20, base + 8, 'classic software: near-zero', 14, GREY)
    s.text(20, base + 26, 'marginal cost per request', 14, GREY)
    s.box(0, 432, 500, 58, 'monthly cost = queries x (in tokens x in price\n+ out tokens x out price), plus retries',
          'pink', fs=14, opacity=35, ff=3)
    # right: capacity bars
    s.line([(520, 84), (520, 420)], color=GREY, sw=1)
    panel_head(s, 540, 84, 'capacity: queries per second', BLUE, 19)
    bars = [('average', 40, 'blue', 580), ('3x peak', 120, 'blue', 700), ('5x peak', 200, 'red', 820)]
    for lab, h, c, x in bars:
        s.box(x, 380 - h, 80, h, None, c, opacity=60)
        s.text(x + 4, 388, lab, 14, INK)
    s.line([(540, 230), (940, 230)], color=RED, dashed=True, sw=2)
    s.text(540, 208, 'provider rate limit or GPU capacity', 14, RED)
    s.box(540, 430, 400, 40, 'check the peak against the limit before launch', 'yellow', fs=15, opacity=70)
    s.save('l1-cost-capacity')


# 6 ─ graceful failure ladder ────────────────────────────────────────────────────────────────────────
def d_graceful_ladder():
    s = Scene()
    title(s, 'Graceful failure: step down one rung, do not fall off',
          'when unsure, move to a safer rung; the rest of the product keeps working')
    rungs = [
        ('answer, with confidence that matches accuracy', 'green'),
        ('show sources; let the user edit, reject, undo', 'green'),
        ('below a threshold: retry or rephrase', 'orange'),
        ('fall back to a rule-based or manual path', 'orange'),
        ('say "I don\'t know" or hand off to a human', 'orange'),
        ('kill switch: roll back the model or prompt', 'red'),
    ]
    for i, (t, c) in enumerate(rungs):
        y = 100 + i * 56
        s.box(20 + i * 30, y, 440, 44, t, c, fs=15, opacity=50)
    s.text(20, 452, 'a wrong answer with no way out is what users do not forgive', 17, RED)
    # trust layers
    s.text(660, 100, 'trust is built in four layers', 19, PURPLE)
    layers = [('calibration: confidence = accuracy', 'teal'),
              ('transparency: show the source', 'teal'),
              ('control: edit, reject or undo', 'blue'),
              ('track record: good outcomes', 'green')]
    for i, (t, c) in enumerate(layers):
        s.box(660, 136 + i * 62, 300, 50, t, c, fs=14, opacity=50)
    s.save('l1-graceful-ladder')


# 7 ─ precision and recall at two thresholds ─────────────────────────────────────────────────────────
def d_threshold():
    s = Scene()
    title(s, 'Where to put the threshold: precision vs recall',
          'ten transactions scored by a fraud model; the threshold moves the mix')
    px = lambda v: 60 + v * 860
    s.line([(px(0), 262), (px(1), 262)], color=GREY, sw=3)
    for v in (0.0, 0.5, 1.0):
        s.text(px(v) - 10, 272, f'{v:.1f}', 14, GREY, ff=3)
    fraud = [0.95, 0.88, 0.66, 0.31]
    legit = [0.91, 0.74, 0.52, 0.45, 0.22, 0.10]
    for v in fraud:
        s.box(px(v) - 9, 253, 18, 18, None, 'red', shape='ellipse', opacity=90)
    for v in legit:
        s.box(px(v) - 9, 253, 18, 18, None, 'blue', shape='ellipse', opacity=90)
    # thresholds
    for v, lab in ((0.9, 'threshold 0.9'), (0.6, 'threshold 0.6')):
        s.line([(px(v), 170), (px(v), 330)], color=YEL, dashed=True, sw=2)
        s.text(px(v) - 60, 150, lab, 16, YEL)
    # legend
    s.box(60, 100, 16, 16, None, 'red', shape='ellipse', opacity=90)
    s.text(84, 98, 'fraud transaction', 15, INK)
    s.box(260, 100, 16, 16, None, 'blue', shape='ellipse', opacity=90)
    s.text(284, 98, 'genuine payment (a customer)', 15, INK)
    s.text(60, 124, 'blocked = score at or above the threshold', 15, GREY)
    # boxes with the numbers from the calculator run
    s.box(40, 360, 430, 110, 'threshold 0.9: few blocks, many misses\nblocked 2 · fraud caught 1 · wrongly blocked 1\nprecision 0.50 · recall 0.25', 'red', fs=15, opacity=35)
    s.box(500, 360, 430, 110, 'threshold 0.6: more fraud caught, more genuine blocked\nblocked 5 · fraud caught 3 · wrongly blocked 2\nprecision 0.60 · recall 0.75', 'yellow', fs=15, opacity=55)
    s.text(40, 484, 'which error costs more (a blocked genuine payment, or a missed fraud) decides the point', 15, PURPLE)
    s.save('l1-threshold')


# 8 ─ big picture cheat sheet ────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 4 on one page: five ideas, five questions',
          'five ideas from 4.1 to 4.5, each with the question it answers')
    cols = [
        ('4.1 Rate, not yes/no', 'success is a rate with an acceptance bar', 'what is the error budget?', 'teal'),
        ('4.2 Data flywheel', 'a closed, clean feedback loop is the moat', 'what is the signal, label, consent?', 'teal'),
        ('4.3 Quality distribution', 'segments, the worst tail, severity', 'where does it fail, and how badly?', 'teal'),
        ('4.4 Latency and cost', 'time to first token, tokens/s, cost per query', 'what does one answer cost at peak?', 'pink'),
        ('4.5 Trust and failure', 'calibration, transparency, control', 'what does the user do when it is wrong?', 'red'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 192
        s.box(x, 84, 182, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 182, 110, core, c, fs=15, opacity=45)
        s.box(x, 280, 182, 92, q, 'yellow', fs=15, opacity=60)
    s.box(10, 392, 940, 58, 'AI product = a rate + a data loop + a quality distribution + cost and latency + trust',
          'purple', fs=17, opacity=35)
    s.box(10, 462, 940, 36, 'good outcome: calibrated, measured by segment, with a way out', 'green', fs=15, opacity=45)
    s.save('l1-big-picture')


for f in [d_deterministic_vs_probabilistic, d_flywheel, d_quality_distribution, d_latency,
          d_cost_capacity, d_graceful_ladder, d_threshold, d_big_picture]:
    f()

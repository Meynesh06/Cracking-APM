# Excalidraw scenes for Chapter 16 (page 13, l13-*). Run: python3 diagrams_l13.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

PINK = '#9c36b5'   # pink as a text colour (money)


def mono_lines(s, x, y, items, fs=14, gap=20, color=INK):
    for i, t in enumerate(items):
        s.text(x, y + i * gap, t, fs, color, ff=3)


# 1 ─ the RCA sequence ────────────────────────────────────────────────────────────────────────────────
def d_rca_sequence():
    s = Scene()
    title(s, 'The RCA sequence', 'scope, walk the journey, split the causes, then add the AI checks')
    s.box(0, 100, 170, 84, '1 scope\nclarify, verify\nreach and shape', 'purple', fs=16)
    s.box(200, 100, 170, 84, '2 walk the journey\nfirst stage that moved', 'orange', fs=15)
    s.box(400, 100, 170, 84, '3 split the causes\ninternal vs external', 'orange', fs=15)
    s.box(600, 100, 170, 84, '4 AI checks\nmodel, prompt,\ndata, cost', 'teal', fs=15)
    s.box(800, 100, 160, 84, 'converge\none root cause', 'green', fs=16)
    for x in (172, 372, 572, 772):
        s.arrow([(x, 142), (x + 26, 142)], color=GREY, sw=3)
    s.text(0, 226, 'steps 1 to 3 apply to every product', 18, INK)
    s.text(0, 254, 'step 4 is added only when the product is AI', 18, INK)
    s.box(0, 300, 960, 92, None, 'purple', opacity=30)
    s.text(16, 312, 'the close: one most-probable root cause', 19, PURPLE)
    s.text(16, 344, 'with a logical path to it, then solutions ranked', 17, INK)
    s.text(16, 368, 'by impact and effort (the close is not a list of ideas)', 17, INK)
    s.save('l13-rca-sequence')


# 2 ─ scoping checklist ───────────────────────────────────────────────────────────────────────────────
def d_scoping_checklist():
    s = Scene()
    title(s, 'Scoping: one vague sentence becomes one clear problem',
          'four moves, then a restated problem you confirm with the interviewer')
    s.box(0, 120, 180, 150, 'vague prompt\n"DAU dropped\n12% last week"', 'blue', fs=17)
    s.arrow([(182, 195), (220, 195)], color=GREY, sw=3)
    moves = [
        ('clarify key terms', '"not visible": placement, option or bug?'),
        ('verify the metric', 'how measured? did the definition change?'),
        ('scope the reach', 'region, platform, OS, segment: everyone?'),
        ('scope the shape', 'sudden or gradual? absolute or %? baseline?'),
    ]
    for i, (head, q) in enumerate(moves):
        y = 100 + i * 72
        s.box(224, y, 240, 56, head, 'orange', fs=17, opacity=70)
        s.text(484, y + 18, q, 15, INK, ff=3)
    s.arrow([(344, 372), (344, 398)], color=GREY, sw=3)
    s.box(120, 400, 450, 66, 'restated problem, one sentence\nconfirm it before any cause', 'green', fs=16)
    s.text(600, 414, 'check: is the metric per user or overall?', 15, GREY, ff=3)
    s.text(600, 438, 'check: did anything ship around the time?', 15, GREY, ff=3)
    s.text(600, 462, 'check: internal or external users affected?', 15, GREY, ff=3)
    s.save('l13-scoping-checklist')


# 3 ─ walking the journey ─────────────────────────────────────────────────────────────────────────────
def d_journey_walk():
    s = Scene()
    title(s, 'Walk the journey and locate the drop',
          'one linear chain, no branches: stop at the first stage that moved')
    stages = ['open app', 'search', 'view item', 'add to cart', 'pay', 'confirm']
    marks = [('flat', GREEN), ('flat', GREEN), ('flat', GREEN), ('flat', GREEN), ('falls', RED),
             ('not reached', GREY)]
    for i, (name, (m, mc)) in enumerate(zip(stages, marks)):
        x = 20 + i * 160
        col = 'red' if name == 'pay' else 'orange'
        s.box(x, 150, 130, 70, name, col, fs=17, opacity=75 if name != 'pay' else 90)
        s.text(x + 65 - _tw(m, 15, .6) / 2, 122, m, 15, mc, ff=3)
        if i < len(stages) - 1:
            s.arrow([(x + 132, 185), (x + 158, 185)], color=GREY, sw=3)
    s.arrow([(705, 222), (675, 290)], color=RED, sw=3)
    s.text(20, 256, 'the stages before pay are flat', 16, GREEN)
    s.box(430, 292, 150, 84, 'input\npay request\nsent?', 'blue', fs=15, opacity=60)
    s.box(600, 292, 150, 84, 'process\nbackend saved\nit?', 'orange', fs=15, opacity=60)
    s.box(770, 292, 150, 84, 'output\nscreen\nrendered?', 'purple', fs=15, opacity=60)
    s.text(20, 330, 'zoom into pay:', 17, PURPLE)
    s.text(20, 356, 'input, process, output: each has an owner', 15, GREY, ff=3)
    s.text(20, 380, 'and a check, so test them in that order', 15, GREY, ff=3)
    s.box(0, 430, 940, 56, 'a drop in one stage is a lead; the cause sits inside that stage', 'yellow',
          fs=16, opacity=45)
    s.save('l13-journey-walk')


# 4 ─ internal vs external cause tree ─────────────────────────────────────────────────────────────────
def d_cause_tree():
    s = Scene()
    title(s, 'Internal vs external causes', 'name the bucket first: it decides the fix and the timeline')
    s.box(330, 90, 300, 56, 'metric dropped', 'purple', fs=19)
    s.box(20, 190, 300, 50, 'internal: your product, company', 'orange', fs=16)
    s.box(640, 190, 300, 50, 'external: market, users, world', 'blue', fs=16)
    s.arrow([(430, 148), (170, 188)], color=GREY, sw=2)
    s.arrow([(480, 148), (790, 188)], color=GREY, sw=2)
    internal = ['release or bug', 'downtime, latency, errors', 'product or UX change',
                'pricing, cost, marketing pause', 'cannibalised by a free feature']
    external = ['competitor: entrant, discount, free offer', 'substitute: a new category',
                'macro or regulation: tax, policy, strike', 'seasonality: festivals, exams, weather',
                'sentiment: press, backlash, behaviour', 'device or platform: OS breaks a flow']
    for i, t in enumerate(internal):
        s.box(20, 262 + i * 40, 300, 32, t, 'orange', fs=14, opacity=40)
    for i, t in enumerate(external):
        s.box(640, 262 + i * 40, 300, 32, t, 'blue', fs=14, opacity=40)
    s.text(20, 508, 'sudden drop: look inside first', 17, ORANGE)
    s.text(640, 508, 'gradual drop: look outside first', 17, GREEN)
    s.text(20, 536, 'check whether competitors fell too: if yes, the market moved', 15, GREY, ff=3)
    s.save('l13-cause-tree')


# 5 ─ AI-specific RCA tree ────────────────────────────────────────────────────────────────────────────
def d_ai_rca_tree():
    s = Scene()
    title(s, 'AI-specific RCA: four causes, each with a symptom and a check',
          'the product got worse or dearer, and no release shipped on our side')
    s.box(300, 92, 360, 56, 'AI quality or cost moved', 'purple', fs=19)
    cols = [
        ('model change', 'vendor, internal', 'teal', [
            'symptom:', 'style or accuracy', 'or refusals shift', 'with no change here',
            'check:', 'pin the model version', 'compare the golden set', 'before and after the date']),
        ('prompt regression', 'internal', 'teal', [
            'symptom:', 'some inputs get worse', 'after a prompt edit',
            'check:', 'diff prompt history', 'with the metric timeline', 'run evals, old vs new']),
        ('data drift', 'internal or external', 'teal', [
            'symptom:', 'gradual decline, more', '"I don\'t know" answers',
            'check:', 'compare the input mix', 'and retrieved context', 'across time windows']),
        ('cost spike', 'internal', 'pink', [
            'symptom:', 'cost per request rises', 'with usage flat',
            'check:', 'split input, output,', 'retries, calls per task', 'cost per successful task']),
    ]
    for i, (head, sub, col, lines) in enumerate(cols):
        x = 20 + i * 236
        s.arrow([(480, 150), (x + 112, 186)], color=GREY, sw=2)
        s.box(x, 190, 225, 270, None, col, opacity=40)
        s.text(x + 10, 198, head, 18, INK)
        s.text(x + 10, 222, sub, 14, GREY, ff=3)
        for j, t in enumerate(lines):
            is_head = t.endswith(':')
            s.text(x + 10, 252 + j * 22, t, 14, PURPLE if is_head else INK, ff=3)
    s.box(0, 486, 940, 40, 'quality issues need the eval; cost issues need routing, caching or limits',
          'yellow', fs=15, opacity=45)
    s.save('l13-ai-rca-tree')


# 6 ─ diagnosis order ─────────────────────────────────────────────────────────────────────────────────
def d_ai_diagnosis_order():
    s = Scene()
    title(s, 'Diagnosis order for an AI regression', 'stop at the first step that explains the change')
    steps = [
        ('1 verify\nthe measurement', 'orange', ['is the measurement', 'itself broken?']),
        ('2 check vendor\nmodel changes', 'teal', ['version or alias', 'changed on the dates?']),
        ('3 check own\nprompt or data', 'teal', ['your prompt or', 'retrieval changed?', 'data changed?']),
        ('4 check cost per\nsuccessful task', 'pink', ['calls, retries and', 'tokens per task up?']),
        ('5 split quality\nfrom cost', 'green', ['quality: run the eval', 'cost: route, cache,', 'or set limits']),
    ]
    for i, (text, col, notes) in enumerate(steps):
        x = i * 195
        s.box(x, 100, 170, 90, text, col, fs=16, opacity=70)
        if i < len(steps) - 1:
            s.arrow([(x + 172, 145), (x + 193, 145)], color=GREY, sw=3)
        mono_lines(s, x + 4, 210, notes, fs=14, gap=20)
    s.box(0, 330, 940, 56, 'the vendor and your own changes sit in the same window: check both',
          'yellow', fs=16, opacity=45)
    s.text(0, 410, 'a quality drop with no release is not a mystery until the', 17, INK)
    s.text(0, 434, 'model version is pinned and the golden set is re-run', 17, INK)
    s.save('l13-ai-diagnosis-order')


# 7 ─ fishbone (Beyond) ───────────────────────────────────────────────────────────────────────────────
def d_fishbone():
    s = Scene()
    title(s, 'Fishbone (Ishikawa): causes grouped on the bones',
          'beyond the notes: brainstorm into the bones, then test each cause against data')
    s.line([(30, 250), (760, 250)], sw=4)
    s.box(760, 210, 180, 80, 'effect:\ncheckout\nconversion fell', 'red', fs=15, opacity=45)
    top = [
        (40, 'release', ['new build shipped', 'screen moved', 'no Android review']),
        (280, 'UX change', ['button below the fold', 'copy changed', 'extra step added']),
        (520, 'data', ['event name changed', 'SDK version bumped', 'missing days']),
    ]
    bottom = [
        (40, 'pricing and fees', ['fee raised', 'discount ended', 'bundle changed']),
        (280, 'competitor', ['rival offer', 'free trial elsewhere', 'new entrant']),
        (520, 'technology', ['payment API timeout', 'slow page load', 'failed retries']),
    ]
    for x, name, causes in top:
        s.box(x, 70, 210, 130, None, 'orange', opacity=35)
        s.text(x + 10, 78, name, 17, INK)
        mono_lines(s, x + 10, 104, causes, fs=14, gap=22)
        s.line([(x + 105, 200), (x + 150, 250)], color=ORANGE, sw=3)
    for x, name, causes in bottom:
        s.box(x, 300, 210, 130, None, 'blue', opacity=35)
        s.text(x + 10, 308, name, 17, INK)
        mono_lines(s, x + 10, 334, causes, fs=14, gap=22)
        s.line([(x + 105, 300), (x + 150, 250)], color=BLUE, sw=3)
    s.text(20, 450, 'the head is the effect; each bone holds a category', 16, GREY)
    s.text(20, 476, 'causes that cannot be tested are noted, not ranked', 16, GREY)
    s.save('l13-fishbone')


# 8 ─ big picture ─────────────────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 16 on one page', 'scope, walk, split, then the AI checks: one root cause to close')
    cols = [
        ('16.1 scope', 'verify the metric, then reach and shape', 'what changed, where, and when?', 'purple'),
        ('16.2 walk the journey', 'one linear chain, the first stage that moved', 'which stage holds the break?', 'orange'),
        ('16.3 split the causes', 'internal (releases, bugs) vs external (market)', 'sudden or gradual?', 'orange'),
        ('16.4 AI checks', 'model, prompt, data drift, cost per task', 'what does the eval say?', 'teal'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 236
        s.box(x, 84, 225, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 225, 110, core, c, fs=15, opacity=45)
        s.box(x, 280, 225, 92, q, 'yellow', fs=15, opacity=60)
    s.box(10, 392, 940, 58, 'one most-probable root cause, with a logical path to it',
          'green', fs=17, opacity=40)
    s.box(10, 462, 940, 36, 'beyond the notes: 5 Whys, the fishbone, the pitfalls of anchoring',
          'grey', fs=15, opacity=45)
    s.save('l13-big-picture')


for f in [d_rca_sequence, d_scoping_checklist, d_journey_walk, d_cause_tree, d_ai_rca_tree,
          d_ai_diagnosis_order, d_fishbone, d_big_picture]:
    f()

# Excalidraw scenes for Chapter 8 (page 5, l5-*). Run: python3 diagrams_l5.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'


# 1 ─ golden set, rubric and scorers ──────────────────────────────────────────────────────────────────
def d_golden_rubric_judge():
    s = Scene()
    title(s, 'Offline eval: a golden set, a rubric, and a scorer',
          'same inputs and same scoring every time, so versions compare fairly')
    s.box(0, 96, 240, 74, 'rubric\nfactual accuracy 0-2, completeness 0-2\ntone 0-1, with anchor examples',
          'purple', fs=14, opacity=50)
    s.box(0, 220, 240, 74, 'golden dataset\nreal queries, edge cases,\nknown failures, adversarial', 'teal',
          fs=14, opacity=45)
    s.arrow([(120, 172), (120, 214)], color=ORANGE, sw=3)
    s.box(280, 220, 200, 74, 'run the system\non the same inputs', 'orange', fs=15, opacity=45)
    s.arrow([(242, 257), (276, 257)], color=ORANGE, sw=3)
    s.box(520, 220, 150, 74, 'outputs\nto score', 'teal', fs=15, opacity=45)
    s.arrow([(482, 257), (516, 257)], color=ORANGE, sw=3)
    s.box(720, 96, 240, 62, 'rule checks\ncheap; good for extraction', 'teal', fs=14, opacity=40)
    s.box(720, 176, 240, 62, 'reference similarity\nweak for open-ended text', 'grey', fs=14, opacity=60)
    s.box(720, 256, 240, 62, 'LLM-as-judge\nscales; has known biases', 'teal', fs=14, opacity=70)
    for y in (127, 207, 287):
        s.arrow([(672, 257), (716, y)], color=GREY, sw=2)
    s.box(720, 360, 240, 62, 'human raters\nlabel a sample', 'blue', fs=14, opacity=45)
    s.arrow([(840, 356), (840, 322)], color=ORANGE, sw=3)
    s.text(560, 340, 'calibrate: agreement\nwith the judge', 15, ORANGE)
    s.box(0, 370, 500, 52, 'biases: position, longer answers, its own style, prompt wording', 'red', fs=14,
          opacity=30)
    s.box(0, 440, 960, 44, 'trust an automated judge only after it agrees with humans on what matters',
          'yellow', fs=16, opacity=60)
    s.save('l5-golden-rubric-judge')


# 2 ─ human labelling loop ────────────────────────────────────────────────────────────────────────────
def d_human_loop():
    s = Scene()
    title(s, 'Human labelling loop: sample, tag, measure, fix, repeat',
          'humans are the ground truth the judge and the metrics are checked against')
    steps = [
        ('1 Stratify', 'oversample high-stakes,\nnew, borderline, negative', 'orange'),
        ('2 Rate or tag', 'pairwise, 1-5 rubric,\nor error tags', 'blue'),
        ('3 Measure', 'inter-rater agreement;\naudit each rater', 'orange'),
        ('4 Calibrate', 'compare judge with\nhuman labels', 'teal'),
        ('5 Tighten', 'sharpen rubric and guidelines;\nre-label', 'orange'),
    ]
    for i, (a, b, c) in enumerate(steps):
        x = 10 + i * 190
        s.box(x, 110, 170, 110, f'{a}\n{b}', c, fs=14, opacity=45)
        if i < 4:
            s.arrow([(x + 172, 165), (x + 188, 165)], color=GREY, sw=2)
    s.arrow([(850, 222), (850, 264), (95, 264), (95, 224)], color=GREY, sw=2)
    s.text(300, 272, 'every release, not just once: keep a random slice for an honest estimate', 15, ORANGE)
    s.text(0, 316, 'error tags say what to fix:', 17, PURPLE)
    tags = ['hallucination', 'wrong tone', 'missed step', 'stale fact']
    for i, t in enumerate(tags):
        s.box(i * 236, 346, 220, 42, t, 'red', fs=15, opacity=35)
    s.box(0, 410, 960, 60, 'a single average score hides which fix to make; the tag list does not',
          'yellow', fs=16, opacity=60)
    s.save('l5-human-loop')


# 3 ─ online metric funnel ────────────────────────────────────────────────────────────────────────────
def d_metric_funnel():
    s = Scene()
    title(s, 'Online metrics: from shown to kept, and retained',
          'what users do with the output is the strongest live signal')
    stages = [
        ('outputs shown to users', 960, 'teal'),
        ('accepted (acceptance rate)', 800, 'teal'),
        ('accepted without big edits (edit rate)', 640, 'teal'),
        ('task completed (task success)', 500, 'orange'),
        ('AI users still active (retention)', 380, 'green'),
    ]
    for i, (lab, w, c) in enumerate(stages):
        y = 96 + i * 70
        x = (960 - w) / 2
        s.box(x, y, w, 54, lab, c, fs=16, opacity=45)
    s.text(0, 448, 'high acceptance with high edit rate is a hidden cost, not a win', 16, RED)
    s.text(0, 478, 'compare with a holdout or matched cohort; segment by task and language', 16, GREY)
    s.save('l5-metric-funnel')


# 4 ─ guardrail thresholds ────────────────────────────────────────────────────────────────────────────
def d_guardrails():
    s = Scene()
    title(s, 'Guardrail metrics: a threshold per metric, set before launch',
          'a gain on quality never buys a breach of these lines')
    s.text(0, 84, 'guardrail', 16, GREY)
    s.text(320, 84, 'threshold, set before launch', 16, GREY)
    s.text(700, 84, 'if breached', 16, GREY)
    rows = [
        ('harmful output rate', 'under 0.1% on the safety set', 'stop, fix, re-run the suite'),
        ('p95 latency', 'under 4 seconds', 'check the model and routing'),
        ('cost per task', 'under INR 2 (example)', 'route easy cases to a smaller model'),
        ('refusal rate', 'both sides tracked: not too high, not too low', 'tune the filter, review examples'),
        ('factual error rate (high stakes)', 'watched online in sensitive domains', 'add a check, or limit scope'),
        ('complaints and human escalations', 'rate per 1,000 sessions (example)', 'read the sample, find the cause'),
    ]
    for i, (m, t, a) in enumerate(rows):
        y = 112 + i * 56
        s.box(0, y, 290, 46, m, 'pink' if 'cost' in m else 'grey', fs=15, opacity=50)
        s.box(310, y, 360, 46, t, 'green', fs=14, opacity=30)
        s.box(690, y, 270, 46, a, 'red', fs=14, opacity=30)
    s.box(0, 460, 960, 36, 'no threshold means a dashboard nobody acts on', 'yellow', fs=16, opacity=60)
    s.save('l5-guardrails')


# 5 ─ regression gate and rollout ────────────────────────────────────────────────────────────────────
def d_regression_gate():
    s = Scene()
    title(s, 'Regression gate: compare each category, not the average',
          'baseline (grey bar) against the candidate (teal bar), per category')
    cats = [('factual accuracy', 80, 84), ('format', 95, 96), ('safety', 99, 99),
            ('tone', 90, 96), ('long answers', 70, 64)]
    for i, (c, b, n) in enumerate(cats):
        y = 110 + i * 46
        s.text(0, y + 2, c, 15, INK)
        s.box(180, y, b * 4, 16, None, 'grey', opacity=70)
        s.text(180 + b * 4 + 6, y - 1, f'{b}', 13, GREY, ff=3)
        s.box(180, y + 20, n * 4, 16, None, 'teal', opacity=60)
        s.text(180 + n * 4 + 6, y + 19, f'{n}', 13, INK, ff=3)
        d = n - b
        if d < -2:
            s.text(600, y + 6, f'{d:+d}: breach', 15, RED, ff=3)
        else:
            s.text(600, y + 6, f'{d:+d}', 15, GREEN if d >= 0 else INK, ff=3)
    s.box(700, 110, 260, 150, 'gate: no category may drop more than 2 points, and no new severe failure',
          'yellow', fs=14, opacity=55)
    s.text(700, 272, 'a one-point average gain can hide a six-point loss', 15, RED)
    for i, lab in enumerate(['shadow run\nno user sees it', 'canary 1-5%\nold version as fallback',
                             'staged rollout\nkill switch ready']):
        x = 10 + i * 320
        s.box(x, 360, 270, 58, lab, 'orange', fs=14, opacity=45)
        if i < 2:
            s.arrow([(x + 272, 389), (x + 316, 389)], color=GREY, sw=2)
    s.box(0, 440, 960, 44, 'every prompt or model change is a release: run the same suite, then compare',
          'purple', fs=16, opacity=35)
    s.save('l5-regression-gate')


# 6 ─ layered evaluation pipeline ───────────────────────────────────────────────────────────────────
def d_eval_pipeline():
    s = Scene()
    title(s, 'Evaluation in layers: no single number is enough',
          'offline, human review, release gate, online behaviour, guardrails')
    chain = [
        ('offline evals\nbefore launch', 'teal'),
        ('human review\nground truth', 'blue'),
        ('release gate\nregression suite', 'orange'),
        ('online metrics\nwhat users do', 'teal'),
        ('guardrails\nharm, latency, cost', 'red'),
    ]
    for i, (t, c) in enumerate(chain):
        x = 10 + i * 192
        s.box(x, 110, 170, 74, t, c, fs=15, opacity=45)
        if i < 4:
            s.arrow([(x + 172, 147), (x + 188, 147)], color=GREY, sw=2)
    s.arrow([(780, 186), (780, 240), (95, 240), (95, 188)], color=ORANGE, sw=2)
    s.text(200, 248, 'failures found in production become new regression cases the same week', 15, ORANGE)
    s.text(0, 300, 'what each layer answers', 18, PURPLE)
    rows = ['offline: does the new version score at least as well on the fixed set?',
            'human: do the labels agree with the judge, and what is failing?',
            'gate: can this change ship, given the per-category deltas?',
            'online: did users accept, edit, finish and come back?',
            'guardrails: did harm, latency or cost cross a line?']
    for i, t in enumerate(rows):
        s.text(20, 332 + i * 26, '- ' + t, 15, INK)
    s.save('l5-eval-pipeline')


# 7 ─ big picture cheat sheet ─────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 8 on one page: five layers, five questions',
          'five ideas from 8.1 to 8.5, each with the question it answers')
    cols = [
        ('8.1 Offline evals', 'golden set, rubric,\nLLM-as-judge, calibrated\nbefore it is trusted', 'does the set reflect\nreal users and tails?', 'teal'),
        ('8.2 Human labels', 'ground truth, error tags,\ninter-rater agreement,\nguidelines and privacy', 'where do humans and\nthe judge disagree?', 'blue'),
        ('8.3 Online metrics', 'acceptance, edit rate,\ntask success, retention\nvs a control', 'did users trust it\nand finish the task?', 'teal'),
        ('8.4 Guardrails', 'harm rate, latency,\ncost per task, refusals,\ncomplaints', 'what must not get worse,\nand what is the line?', 'red'),
        ('8.5 Regression', 'the same suite on every\nprompt or model change,\nper-category deltas', 'did one fix break three\nother cases?', 'orange'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 192
        s.box(x, 84, 182, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 182, 110, core, c, fs=13, opacity=45)
        s.box(x, 280, 182, 92, q, 'yellow', fs=14, opacity=60)
    s.box(10, 392, 940, 58, 'AI evals = offline + human + online + guardrails + a release gate on every change',
          'purple', fs=16, opacity=35)
    s.box(10, 462, 940, 36, 'good outcome: a change ships only when the suite, the metrics and the lines agree',
          'green', fs=15, opacity=45)
    s.save('l5-big-picture')


for f in [d_golden_rubric_judge, d_human_loop, d_metric_funnel, d_guardrails,
          d_regression_gate, d_eval_pipeline, d_big_picture]:
    f()

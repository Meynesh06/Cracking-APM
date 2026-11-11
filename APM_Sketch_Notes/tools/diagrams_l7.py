# Excalidraw scenes for Chapter 10 (page 7, l7-*). Run: python3 diagrams_l7.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)


def lines(s, x, y, items, color=INK, fs=15, dy=22, ff=5):
    for i, t in enumerate(items):
        s.text(x, y + i * dy, t, fs, color, ff=ff)


# 1 ─ rollout ladder with gates ───────────────────────────────────────────────────────────────────────
def d_rollout_ladder():
    s = Scene()
    title(s, 'Rollout ladder: widen the ring only when the gate passes',
          'write the gates down before the first step')
    steps = [
        ('shadow mode: live traffic, users see nothing', 'grey'),
        ('internal dogfood: employees on real tasks', 'orange'),
        ('closed beta / allowlist: a few hundred users', 'orange'),
        ('percentage ramp: 1%, 5%, 25%, 50%, 100%', 'orange'),
        ('general availability, kill switch still wired in', 'green'),
    ]
    for i, (t, c) in enumerate(steps):
        y = 100 + i * 58
        s.box(20, y, 420, 46, t, c, fs=14, opacity=50)
        if i < len(steps) - 1:
            s.arrow([(230, y + 46), (230, y + 58)], color=GREY, sw=2)
    s.box(480, 100, 460, 230, None, 'purple', opacity=30)
    s.text(496, 112, 'gates between steps (write them first)', 16, PURPLE)
    lines(s, 496, 146, [
        'quality: eval score and thumbs-down or edit rate',
        '   vs the control, within a set threshold',
        'guardrails: harmful-output rate, p95 latency,',
        '   cost per task, all inside budget',
        'business: task success or retention not regressing',
        '',
        'hold at each step; keep the control group running',
    ], fs=15, dy=24)
    s.box(20, 400, 920, 62,
          'kill switch: a flag turns the AI path off in minutes\n'
          'no redeploy; it falls back to a safe state; test it before launch',
          'red', fs=15, opacity=35)
    s.save('l7-rollout-ladder')


# 2 ─ kill switch vs rollback ─────────────────────────────────────────────────────────────────────────
def d_kill_vs_rollback():
    s = Scene()
    title(s, 'Kill switch vs rollback: two different tools',
          'the kill switch stops the AI path; rollback swaps the version')
    s.box(20, 96, 460, 210,
          'kill switch\nturns the AI path off, in minutes\nno redeploy\n'
          'falls back to: the old non-AI flow, a cached\nanswer, or "temporarily unavailable"\n'
          'use for any incident',
          'red', fs=15, opacity=35)
    s.box(500, 96, 440, 210,
          'rollback\nreturns to the previous model, prompt or index\nthe feature stays on\n'
          'use when the new version regressed and\nthe old one was fine',
          'orange', fs=15, opacity=45)
    s.box(20, 326, 920, 84,
          'version all four, so each one can roll back on its own:\n'
          'the model, the prompt, the retrieval index, the data pipeline',
          'teal', fs=15, opacity=40)
    s.box(20, 424, 920, 40, 'who owns the switch at 2 a.m.? is the runbook written?',
          'yellow', fs=16, opacity=60)
    s.text(20, 488, 'a switch never flipped in staging is a hope, not a control', 16, RED)
    s.save('l7-kill-vs-rollback')


# 3 ─ three kinds of drift ────────────────────────────────────────────────────────────────────────────
def d_drift_types():
    s = Scene()
    title(s, 'Three kinds of silent change, three monitors',
          'each needs its own monitor and its own alert baseline')
    cols = [
        ('data drift\nthe world changes', 'teal',
         'new user segments, seasonality,\nnew app version, new languages',
         'input length, language mix, topics,\nempty or malformed inputs', 20),
        ('concept drift\nthe right answer changes', 'orange',
         'new fraud patterns, policy rules,\nnew product names',
         'outcomes against a fresh labelled\nsample, not the old eval set', 340),
        ('vendor drift\nthe model changes', 'red',
         'alias updated, model retrained,\nsafety tuning changed',
         'golden eval on each new version;\ncost and latency per version', 660),
    ]
    for head, c, what, mon, x in cols:
        s.box(x, 96, 280, 58, head, c, fs=15, opacity=50)
        s.box(x, 164, 280, 80, what, c, fs=14, opacity=25)
        s.box(x, 254, 280, 80, mon, 'green', fs=14, opacity=40)
        s.arrow([(x + 140, 222), (x + 140, 252)], color=GREY, sw=2)
    s.text(20, 352, 'what changes (top) and the monitor that catches it (bottom)', 15, GREY)
    s.box(20, 386, 920, 46, 'alert on change from a baseline, not fixed numbers alone',
          'yellow', fs=16, opacity=60)
    s.text(20, 452, 'a feature can get worse on a Tuesday with no line of code changed', 16, RED)
    s.save('l7-drift-types')


# 4 ─ vendor model update playbook ────────────────────────────────────────────────────────────────────
def d_vendor_playbook():
    s = Scene()
    title(s, 'Vendor model update: treat it as a release',
          'a floating alias can change underneath you; a pinned version cannot')
    s.box(20, 96, 460, 50, 'floating alias ("latest"): changes underneath you', 'red', fs=15, opacity=40)
    s.box(500, 96, 440, 50, 'pinned dated version: changes only when you move', 'green', fs=15, opacity=40)
    steps = [
        '1 pin the current\nversion in use',
        '2 regression run on\nthe new version',
        '3 go / no-go gate:\nquality, safety, cost',
        '4 tell support and\nsales the timeline',
        '5 switch traffic, watch\nthe dashboard',
    ]
    for i, t in enumerate(steps):
        x = 20 + i * 190
        s.box(x, 180, 180, 96, t, 'orange', fs=14, opacity=50)
        if i < len(steps) - 1:
            s.arrow([(x + 180, 228), (x + 190, 228)], color=GREY, sw=2)
    s.box(20, 318, 920, 40, 'gate: quality, safety and cost thresholds, set in advance',
          'green', fs=15, opacity=40)
    s.box(20, 372, 920, 40, 'run the golden eval on each candidate before traffic moves',
          'teal', fs=15, opacity=40)
    s.box(20, 426, 920, 62,
          'track the provider\'s deprecation and changelog notices as product events\n'
          'budget for a forced migration each year',
          'purple', fs=15, opacity=35)
    s.save('l7-vendor-playbook')


# 5 ─ first monitoring dashboard ──────────────────────────────────────────────────────────────────────
def d_dashboard():
    s = Scene()
    title(s, 'First monitoring dashboard: what to watch',
          'four panels, each one answers a different question')
    panels = [
        ('quality proxies\nthumbs-down rate\nedit or regenerate rate\nescalation to a human rate', 'teal', 20, 96),
        ('input health\ntoken length distribution\nlanguage share\nretrieval hit rate (RAG)', 'teal', 500, 96),
        ('cost and latency per model version\nso a silent switch to a bigger model shows', 'pink', 20, 262),
        ('ownership\nwho gets paged when quality drops\nwho decides: retune, switch or roll back', 'purple', 500, 262),
    ]
    for t, c, x, y in panels:
        s.box(x, y, 460, 150, t, c, fs=15, opacity=40)
    s.box(20, 430, 920, 46, 'alerts: set on change from a baseline, not fixed numbers',
          'yellow', fs=16, opacity=60)
    s.save('l7-dashboard')


# 6 ─ the feedback loop ───────────────────────────────────────────────────────────────────────────────
def d_feedback_loop():
    s = Scene()
    title(s, 'The feedback loop, designed on purpose',
          'react, learn, change, and close the loop where you can')
    flow = [
        ('users react', 'blue', 20),
        ('signals: explicit,\nimplicit, expert', 'teal', 255),
        ('triage queue with\nan owner and a time', 'orange', 490),
        ('product changes;\nclose the loop visibly', 'green', 725),
    ]
    for t, c, x in flow:
        s.box(x, 96, 210, 64, t, c, fs=14, opacity=50)
    for x in (230, 465, 700):
        s.arrow([(x, 128), (x + 25, 128)], color=GREY, sw=2)
    cols = [
        ('explicit (sparse, clear)\nthumbs up or down\nreport a problem, star ratings\ncorrections typed by the user', 20),
        ('implicit (abundant, noisy)\nedits to an AI draft, copy or accept\nregenerate clicks, abandonment\nescalation to a human', 330),
        ('expert (trained reviewers)\nlabels on sampled outputs\nsee Chapter 8.2', 640),
    ]
    for t, x in cols:
        s.box(x, 186, 300, 150, t, 'teal', fs=14, opacity=35)
    s.box(20, 354, 920, 40, 'use both signals, and check that they agree',
          'yellow', fs=16, opacity=60)
    s.box(20, 406, 920, 74,
          'pitfalls: heavy and angry users over-represent;\n'
          'weight by segment. A thumbs-down may mean tone,\n'
          'not a wrong answer. Feedback is not ground truth.',
          'red', fs=15, opacity=35)
    s.save('l7-feedback-loop')


# 7 ─ consent for three uses ──────────────────────────────────────────────────────────────────────────
def d_consent_uses():
    s = Scene()
    title(s, 'Consent for three uses: default to the narrowest',
          'ask for each use separately; never train on prompts without opt-in')
    s.box(20, 96, 560, 56, 'a. improve the product for this user (narrowest, default)',
          'green', fs=15, opacity=45)
    s.box(20, 166, 560, 56, 'b. evaluation and analytics (its own consent)',
          'orange', fs=15, opacity=45)
    s.box(20, 236, 560, 56, 'c. training or fine-tuning models (clear opt-in only)',
          'red', fs=15, opacity=40)
    s.box(620, 96, 320, 196,
          'honour withdrawal and deletion\n'
          'retention covers derived data:\n'
          'embeddings and logs, not only\nthe main store\n'
          'India DPDP: clear notice, consent,\nrights to withdraw and to erasure',
          'teal', fs=14, opacity=35)
    s.box(20, 316, 560, 56, 'not collected by default: full customer PII (redact first)',
          'grey', fs=15, opacity=50)
    s.box(20, 392, 920, 52, 'each use needs its own consent and its own retention rule',
          'yellow', fs=16, opacity=60)
    s.box(20, 462, 920, 42, 'support example: sent as is, edited (store the diff), or discarded',
          'blue', fs=15, opacity=40)
    s.save('l7-consent-uses')


# 8 ─ big picture cheat sheet ─────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 10 on one page: launch is the start of learning',
          'three areas, three questions')
    cols = [
        ('10.1 Rollouts and kill switches', 'gated rings, a tested off-switch, rollback',
         'what gate lets us widen the ring?', 'orange'),
        ('10.2 Drift and vendor updates', 'data, concept and vendor drift; pinned versions',
         'what changed: the world, the answer, the model?', 'teal'),
        ('10.3 Feedback and consent', 'explicit, implicit and expert signals; narrowest use',
         'what may we learn from, and with consent?', 'teal'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 20 + i * 316
        s.box(x, 84, 300, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 300, 110, core, c, fs=15, opacity=45)
        s.box(x, 280, 300, 92, q, 'yellow', fs=15, opacity=60)
    s.box(20, 392, 920, 58, 'AI launch = the start of learning: rings, monitors, and a consented loop',
          'purple', fs=17, opacity=35)
    s.box(20, 462, 920, 36, 'good outcome: gated, watched by segment and version, with a switch',
          'green', fs=15, opacity=45)
    s.save('l7-big-picture')


for f in [d_rollout_ladder, d_kill_vs_rollback, d_drift_types, d_vendor_playbook,
          d_dashboard, d_feedback_loop, d_consent_uses, d_big_picture]:
    f()

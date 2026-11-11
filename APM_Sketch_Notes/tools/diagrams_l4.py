# Excalidraw scenes for Chapter 7 (page 4, l4-*). Run: python3 diagrams_l4.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'


# 1 ─ use-case scoring grid ───────────────────────────────────────────────────────────────────────────
def d_use_case_grid():
    s = Scene()
    title(s, 'Use-case scoring grid: multiply four scores, each 1 to 3',
          'a 1 on any factor drags the product down; 81 is the top score')
    names = ['frequency\nof the task', 'pain\ntoday', 'error\ntolerance', 'data\navailable']
    for i, n in enumerate(names):
        x = i * 200
        s.box(x, 96, 160, 64, n, 'purple', fs=16, opacity=55)
        if i < 3:
            s.text(x + 170, 112, 'x', 26, INK)
    s.text(766, 112, '=', 26, INK)
    s.box(790, 96, 170, 64, 'score\n1 to 81', 'yellow', fs=18, opacity=70)
    s.text(0, 190, 'illustrative scores, one per factor:', 16, GREY)
    s.box(0, 220, 560, 44, 'draft replies in a support tool   3 x 3 x 3 x 3 = 81', 'green', fs=15,
          opacity=45, ff=3)
    s.box(0, 274, 560, 44, 'loan approval decisions         2 x 3 x 1 x 2 = 12', 'red', fs=15,
          opacity=40, ff=3)
    s.box(0, 328, 560, 44, 'monthly tax filing               1 x 2 x 1 x 2 = 4', 'grey', fs=15,
          opacity=60, ff=3)
    s.text(600, 224, 'same draft replies, but error tolerance is 1:', 16, INK)
    s.text(600, 252, '3 x 3 x 1 x 3 = 27, down from 81', 16, RED, ff=3)
    s.text(600, 300, 'a wrong answer costs a lot in loans,', 16, INK)
    s.text(600, 326, 'so the error tolerance score stays low', 16, INK)
    s.box(0, 400, 960, 50, 'first bets: high frequency, painful, error-tolerant tasks, with data',
          'purple', fs=17, opacity=30)
    s.text(0, 470, 'the scores are judgement calls: agree them with the team', 16, GREY)
    s.save('l4-use-case-grid')


# 2 ─ confidence signals spectrum ─────────────────────────────────────────────────────────────────────
def d_confidence_spectrum():
    s = Scene()
    title(s, 'Confidence signals: from fake precision to honest cues',
          'show a signal only when it changes what the user does')
    s.box(0, 100, 280, 120, 'raw score: "92% confident"\nlooks precise, often misleading\nto users',
          'red', fs=15, opacity=35)
    s.box(340, 100, 280, 120, '"based on 3 sources"\n"I could not find this\nin your files"',
          'teal', fs=15, opacity=45)
    s.box(680, 100, 280, 120, 'abstain, or ask a clarifying\nquestion when confidence is low\nrather than guess',
          'green', fs=14, opacity=40)
    s.arrow([(0, 252), (940, 252)], color=ORANGE, sw=3)
    s.text(0, 228, 'less fake precision, more evidence and honesty', 16, GREY)
    s.box(0, 290, 960, 50, 'test first: is the score calibrated against eval data?', 'yellow', fs=17,
          opacity=70)
    s.text(0, 360, 'if it is not calibrated, replace it with evidence cues, or remove it', 16, INK)
    s.text(0, 394, 'over-trust and under-trust both hurt; the goal is calibrated trust', 16, GREY)
    s.save('l4-confidence-spectrum')


# 3 ─ hallucination and recovery layers ───────────────────────────────────────────────────────────────
def d_recovery_layers():
    s = Scene()
    title(s, 'Design the failure path as carefully as the success path',
          'five layers, each one a product decision, then the error classes')
    rows = [
        ('1 Prevent', 'ground answers in retrieved sources (RAG)\nconstrain outputs to known schemas; abstain if unsourced'),
        ('2 Detect', 'run checks before output reaches the user\ncitation checks, schema checks, rules, a second model as judge'),
        ('3 Signal', 'tell users when the answer is uncertain,\nunsourced or partial'),
        ('4 Recover', 'offer a fast path: edit, ask again, escalate to a human,\nor open the source'),
        ('5 Learn', 'log user corrections and reports as labelled data for evals'),
    ]
    for i, (lab, txt) in enumerate(rows):
        y = 96 + i * 66
        s.box(0, y, 170, 58, lab, 'orange', fs=17, opacity=55)
        s.box(180, y, 780, 58, txt, 'orange', fs=15, opacity=18)
    s.text(0, 428, 'error classes to design for: what the user sees, what the system does, what is logged',
           15, GREY)
    errs = ['factual error', 'refusal or\nover-refusal', 'incomplete or\ntruncated',
            'latency timeout\nor tool failure', 'harmful or\noff-brand']
    for i, e in enumerate(errs):
        s.box(i * 192, 452, 182, 58, e, 'red', fs=14, opacity=35)
    s.save('l4-recovery-layers')


# 4 ─ human-in-the-loop placements ────────────────────────────────────────────────────────────────────
def d_hitl_placements():
    s = Scene()
    title(s, 'Where the human sits: five placements in the workflow',
          'pick each one from how costly and reversible a wrong output is')
    s.text(0, 80, 'pattern', 16, GREY)
    s.text(216, 80, 'human role', 16, GREY)
    s.text(562, 80, 'when to use', 16, GREY)
    rows = [
        ('Suggest', 'chooses to accept', 'low-stakes, high-volume\n(text completion)', 'blue'),
        ('Review before send', 'approves each output', 'customer-facing messages,\nlegal or medical text', 'blue'),
        ('Exception handling', 'reviews only flagged cases', 'high volume, with a reliable\nrisk classifier', 'blue'),
        ('Sample audit', 'spot-checks a percentage', 'mature features with\nstable quality', 'blue'),
        ('Escalation', 'takes over when the AI cannot resolve', 'support, complex or\nemotional cases', 'blue'),
    ]
    for i, (p, role, when, c) in enumerate(rows):
        y = 110 + i * 62
        s.box(0, y, 200, 52, p, 'purple', fs=16, opacity=55)
        s.box(216, y, 330, 52, role, c, fs=15, opacity=30)
        s.box(562, y, 380, 52, when, 'grey', fs=14, opacity=40)
    s.box(0, 430, 960, 40, 'rubber-stamping: if people approve almost everything, the review is not working',
          'red', fs=16, opacity=35)
    s.box(0, 478, 960, 36, 'review less where the error rate is low and stable; keep it where errors cost',
          'green', fs=16, opacity=40)
    s.save('l4-hitl-placements')


# 5 ─ onboarding and expectation ladder ───────────────────────────────────────────────────────────────
def d_onboarding_ladder():
    s = Scene()
    title(s, 'Onboarding: set expectations before the first answer',
          'five things to teach, then measure what changed')
    s.box(0, 80, 940, 34, 'first run: a guided task with a known-good example, not an empty box',
          'yellow', fs=15, opacity=55)
    steps = [
        ('1 Capability', 'what it does well', 'with 2-3 examples'),
        ('2 Limits', 'what it cannot do', 'said plainly'),
        ('3 Verification', 'how to check it', 'sources, edit first'),
        ('4 Data', 'what is kept', 'training use, opt-out'),
        ('5 Control', 'how to turn it off', 'or change behaviour'),
    ]
    for i, (a, b, c) in enumerate(steps):
        h = 110 + i * 40
        s.box(20 + i * 184, 400 - h, 176, h, f'{a}\n{b}\n{c}', 'blue', fs=14, opacity=40)
    s.box(0, 430, 960, 40, 'measure: activation, week-1 repeat use, "this was wrong" reports, by cohort',
          'green', fs=16, opacity=40)
    s.save('l4-onboarding-ladder')


# 6 ─ states an AI feature must draw (Beyond) ─────────────────────────────────────────────────────────
def d_ui_states():
    s = Scene()
    title(s, 'Beyond: eight states an AI feature needs on screen',
          'the failure and waiting states are part of the feature, not a bug list')
    states = [
        ('waiting for first token', 'show progress, not a blank box', 'orange'),
        ('streaming', 'allow stop and regenerate', 'orange'),
        ('done, with sources', 'citations open the source', 'green'),
        ('low confidence', '"not sure" path, ask again', 'teal'),
        ('no source found', 'abstain; route to a human', 'teal'),
        ('error or timeout', 'retry; the rest still works', 'red'),
        ('refused or off-scope', 'say what it can do instead', 'red'),
        ('handed to a human', 'carry the context over', 'green'),
    ]
    for i, (a, b, c) in enumerate(states):
        x = (i % 4) * 236
        y = 100 + (i // 4) * 110
        s.box(x, y, 226, 84, f'{a}\n{b}', c, fs=14, opacity=40)
    s.box(0, 330, 960, 46, 'Beyond the notes: add a state for each one before the design review',
          'yellow', fs=16, opacity=60)
    s.save('l4-ui-states')


# 7 ─ big picture cheat sheet ─────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 7 on one page: five ideas, five questions',
          'five ideas from 7.1 to 7.5, each with the question it answers')
    cols = [
        ('7.1 Pick the use case', 'AI where a good\ndraft saves effort;\nerrors are cheap\nto catch', 'where does AI beat\nthe current flow?', 'teal'),
        ('7.2 Control and signals', 'control, sources\nand honest signals\nthat change what\nthe user does', 'can users steer it\nand check it?', 'teal'),
        ('7.3 Errors and recovery', 'design for wrong\nanswers: prevent,\ndetect, signal,\nrecover, learn', 'what does the user\ndo when it is wrong?', 'red'),
        ('7.4 Human in the loop', 'decide where a\nperson reviews,\napproves or\noverrides', 'who reviews, and how\nmuch time do they have?', 'blue'),
        ('7.5 Expectations', 'teach the limits\nbefore the first\nanswer, then\nmeasure', 'does the user know\nwhat it cannot do?', 'blue'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 192
        s.box(x, 84, 182, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 182, 110, core, c, fs=14, opacity=45)
        s.box(x, 280, 182, 92, q, 'yellow', fs=14, opacity=60)
    s.box(10, 392, 940, 58, 'AI UX = use-case choice + control + honest signals + failure path + review + onboarding',
          'purple', fs=16, opacity=35)
    s.box(10, 462, 940, 36, 'good outcome: users know when to trust the output, and when not to', 'green',
          fs=15, opacity=45)
    s.save('l4-big-picture')


for f in [d_use_case_grid, d_confidence_spectrum, d_recovery_layers, d_hitl_placements,
          d_onboarding_ladder, d_ui_states, d_big_picture]:
    f()

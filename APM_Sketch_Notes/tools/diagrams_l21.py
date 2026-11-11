# Excalidraw scenes for Chapter 24 (page 21, l21-*). Run: python3 diagrams_l21.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


def head(s, x, y, text, color=PURPLE, fs=19):
    s.text(x, y, text, fs, color)


# 1 ─ 24.1 the doubt solver loop ────────────────────────────────────────────────────────────────────
def d_exam_doubt_loop():
    s = Scene()
    title(s, '24.1 The doubt solver: retrieve, cite or say "not sure"',
          'every answer comes from the owned corpus, or the bot admits it has none')
    s.box(20, 100, 200, 66, 'student doubt\n(text, photo or voice)', 'blue', fs=16)
    s.box(270, 100, 210, 66, 'retrieve from the owned\nor licensed corpus', 'teal', fs=16, opacity=60)
    s.box(530, 100, 170, 66, 'strong match?', 'yellow', fs=17, opacity=70)
    s.box(740, 100, 200, 66, 'answer with a citation;\nattempt first, then hint', 'green', fs=14, opacity=55)
    s.box(470, 230, 260, 66, 'say "not sure", show the\nclosest solved example', 'orange', fs=14, opacity=55)
    s.box(740, 350, 200, 66, 'mistake log\n(every wrong answer)', 'teal', fs=15, opacity=60)
    s.box(330, 350, 340, 66, 'daily quiz from the mistake log\n(spaced repetition)', 'orange', fs=15, opacity=55)
    s.arrow([(222, 133), (266, 133)], color=GREY, sw=3)
    s.arrow([(482, 133), (526, 133)], color=GREY, sw=3)
    s.arrow([(702, 133), (736, 133)], color=GREEN, sw=3)
    s.text(706, 106, 'yes', 15, GREEN)
    s.arrow([(615, 168), (615, 226)], color=ORANGE, sw=3)
    s.text(622, 190, 'no', 15, ORANGE)
    s.arrow([(840, 168), (840, 346)], color=GREY, sw=3)
    s.arrow([(736, 383), (674, 383)], color=GREY, sw=3)
    s.box(0, 448, 960, 44, 'guardrails: cited answers only, weekly expert sample, golden-set gate',
          'red', fs=16, opacity=30)
    s.text(20, 318, 'attempt first: the student tries before the hint, and the hint before the full solution', 15, INK)
    s.save('l21-exam-doubt-loop')


# 2 ─ 24.2 the phase plan for the navigation app ─────────────────────────────────────────────────────
def d_nav_phases():
    s = Scene()
    title(s, '24.2 Navigation: reuse data first, the car last',
          'four waves, ordered by value, risk and how much attention they take')
    s.text(20, 84, 'phone in hand: planning and search', 16, GREY)
    s.text(740, 84, 'eyes on the road', 16, RED)
    cols = [
        ('1 review summaries', 'summarise reviews\nalready in the app', 'green', 'cheap, frequent,\nlow risk, cached'),
        ('2 conversational search', 'words become filters\nand ranked places', 'green', 'small model parses,\nbig model rarely'),
        ('3 itineraries', 'multi-stop drafts the\nuser edits first', 'orange', 'user confirms each\nstop first'),
        ('4 in-drive voice', 'short spoken answers,\nno screen needed', 'red', 'ships last, after\nsearch is proven'),
    ]
    for i, (name, what, c, why) in enumerate(cols):
        x = 20 + i * 240
        s.box(x, 120, 210, 210, None, c, opacity=35)
        s.text(x + 12, 132, name, 18, INK)
        s.text(x + 12, 176, what, 15, INK, ff=3)
        s.text(x + 12, 254, why, 14, GREY, ff=3)
        if i < 3:
            s.arrow([(x + 212, 225), (x + 238, 225)], color=GREY, sw=3)
    s.box(20, 352, 920, 44, 'any route change needs a one-word confirmation from the driver',
          'yellow', fs=17, opacity=60)
    s.box(20, 408, 920, 44, 'in the car: the screen stays idle while the vehicle moves (guardrail)',
          'red', fs=17, opacity=30)
    s.text(20, 470, 'value and risk rise together: the phase order follows the safety bar', 16, PURPLE)
    s.save('l21-nav-phases')


# 3 ─ 24.3 the metric tree for the resume reviewer ──────────────────────────────────────────────────
def d_resume_metric_tree():
    s = Scene()
    title(s, '24.3 Resume reviewer: one North Star, guardrails as a veto',
          'leading indicators move the North Star; guardrails can stop a launch')
    s.box(250, 88, 460, 62, 'North Star: interview callbacks per reviewed\nresume within 30 days, compared by cohort',
          'yellow', fs=15, opacity=65)
    leads = [
        'activation: upload,\nthen view feedback',
        'suggestion acceptance\n(paired with rated quality)',
        'edit-after-accept\nrate',
        're-review within\nseven days',
        'NPS',
    ]
    for i, t in enumerate(leads):
        x = 10 + i * 190
        s.arrow([(480, 150), (x + 90, 196)], color=GREY, sw=2)
        s.box(x, 200, 180, 70, t, 'green', fs=14, opacity=50)
    s.text(10, 286, 'leading indicators: they move first, and can mislead alone', 15, GREEN)
    s.box(10, 318, 940, 30, 'guardrails: a veto, not a trade-off', 'red', fs=16, opacity=35)
    guards = ['zero invented\nclaims', 'PII leakage\nincidents', 'score gap across\ngender, college tier',
              'p95 latency', 'cost per review']
    for i, t in enumerate(guards):
        x = 10 + i * 190
        s.box(x, 360, 180, 58, t, 'red', fs=14, opacity=40)
    s.text(10, 436, 'acceptance up, callbacks flat: the suggestions please but do not help', 15, ORANGE)
    s.text(10, 462, 'callbacks up, fabrication up: stop and fix before anything ships', 15, RED)
    s.save('l21-resume-metric-tree')


# 4 ─ 24.4 the RCA tree for hallucination complaints ────────────────────────────────────────────────
def d_hallucination_rca():
    s = Scene()
    title(s, '24.4 Hallucination complaints: verify, narrow, then fix',
          'the first step is the rate; the signature of the cause picks the fix')
    steps = [
        '1 verify: complaints per 1,000 convs',
        '2 segment: intent, language, versions',
        '3 timeline: deploys, prompts, KB, vendor',
        '4 reproduce: replay old vs new config',
        '5 fix: mitigate first, root cause next',
    ]
    for i, t in enumerate(steps):
        y = 96 + i * 66
        s.box(20, y, 390, 50, t, 'orange', fs=14, opacity=55)
        if i < 4:
            s.arrow([(215, y + 50), (215, y + 66)], color=GREY, sw=2)
    s.line([(424, 120), (424, 404)], color=GREY, sw=2)
    s.text(440, 92, 'cause signatures (step 4 decides)', 16, PURPLE)
    causes = [
        ('vendor model update: spike across intents', 'red'),
        ('prompt regression: spike after a prompt edit', 'red'),
        ('stale knowledge base: one policy intent', 'red'),
        ('retrieval miss: right answer not retrieved', 'teal'),
        ('new intent with no content behind it', 'teal'),
        ('cost-driven change: smaller model, less text', 'pink'),
    ]
    for i, (t, c) in enumerate(causes):
        y = 118 + i * 48
        s.box(440, y, 500, 40, t, c, fs=14, opacity=40)
    s.text(440, 412, 'mitigate in 24-48 hours: roll back or gate the intent', 15, GREEN)
    s.save('l21-hallucination-rca')


# 5 ─ 24.5 the dispute assistant: free alerts, success fee ──────────────────────────────────────────
def d_dispute_success_fee():
    s = Scene()
    title(s, '24.5 Dispute assistant: free alerts, paid only on wins',
          'the fee is charged only when money comes back, with a floor for small tickets')
    s.box(20, 100, 300, 58, 'free: deadline alerts and checklist', 'green', fs=16, opacity=55)
    s.box(20, 178, 300, 58, 'paid: success fee on won disputes', 'pink', fs=16, opacity=40)
    s.box(20, 256, 300, 58, 'minimum per dispute for small tickets', 'pink', fs=16, opacity=40)
    s.box(20, 334, 300, 58, 'volume plan: lower % for large merchants', 'pink', fs=16, opacity=40)
    s.text(360, 100, 'unit economics must clear first', 19, PURPLE)
    s.box(360, 136, 580, 70, '(model cost + human QA) per contested dispute\n'
          '< fee x win rate x average disputed amount', 'purple', fs=15, opacity=30)
    s.box(360, 236, 280, 62, 'Rs 500 dispute: margin +31\n(placeholder costs and win rate)', 'green', fs=14, opacity=50)
    s.box(660, 236, 280, 62, 'Rs 100 dispute: margin -9\nthe same 25% fee loses money', 'red', fs=14, opacity=40)
    s.text(360, 318, 'break-even win rate: 15% on Rs 500, 76% on Rs 100', 16, RED)
    s.text(360, 344, 'so low-win reason codes are not auto-contested', 16, INK)
    s.box(0, 418, 960, 56, 'the merchant pays only when money comes back: fee follows the outcome',
          'yellow', fs=17, opacity=60)
    s.save('l21-dispute-success-fee')


# 6 ─ 24.6 the copilot flow with the autonomy ladder ────────────────────────────────────────────────
def d_support_copilot_flow():
    s = Scene()
    title(s, '24.6 Support copilot: the agent confirms every action',
          'facts come from live systems; the model phrases them and cites the clause')
    steps = [
        (20, 150, 'ticket opens', 'blue'),
        (200, 170, 'live shipment summary\nfrom the API', 'teal'),
        (400, 170, 'policy-grounded draft\nwith the clause cited', 'teal'),
        (600, 150, 'agent edits\nor accepts', 'orange'),
        (780, 160, 'confirmed action\nwith an undo', 'green'),
    ]
    for x, w, t, c in steps:
        s.box(x, 100, w, 62, t, c, fs=14, opacity=55)
    for (x, w, _, _), (nx, _, _, _) in zip(steps, steps[1:]):
        s.arrow([(x + w, 131), (nx, 131)], color=GREY, sw=3)
    s.box(400, 196, 190, 56, 'low retrieval confidence:\n"no matching policy found"', 'red', fs=13, opacity=40)
    s.arrow([(495, 162), (495, 192)], color=RED, sw=2)
    s.text(20, 278, 'autonomy grows one action type at a time', 18, PURPLE)
    s.box(20, 306, 280, 62, '1 summary and suggested replies', 'green', fs=15, opacity=50)
    s.box(330, 306, 280, 62, '2 claim intake auto-filled, agent reviews', 'orange', fs=14, opacity=50)
    s.box(640, 306, 280, 62, '3 autonomous actions: last, per type', 'red', fs=14, opacity=40)
    s.arrow([(302, 337), (326, 337)], color=GREY, sw=3)
    s.arrow([(612, 337), (636, 337)], color=GREY, sw=3)
    s.box(0, 392, 940, 40, 'facts from live systems, never from the model\'s memory', 'yellow', fs=16, opacity=60)
    s.box(0, 444, 940, 40, 'every rebooking or refund: logged, with an easy undo', 'grey', fs=16, opacity=50)
    s.save('l21-support-copilot-flow')


# 7 ─ 24.8 the cannibalisation decision matrix ─────────────────────────────────────────────────────
def d_cannibalisation_matrix():
    s = Scene()
    title(s, '24.8 Cannibalisation: which shift is a problem?',
          'only a loss of combined margin or retention counts')
    s.text(20, 84, 'what happened', 16, GREY)
    s.text(380, 84, 'is it a problem?', 16, GREY)
    s.text(640, 84, 'what to do', 16, GREY)
    rows = [
        ('users move to a cheaper or free substitute', 'revenue loss: a problem', 'red',
         'options 1 and 3: hand off, or price the AI'),
        ('users move to a higher-value action', 'a win, even if the old action falls', 'green',
         'keep it; measure combined margin'),
        ('engagement moves, revenue does not', 'a monetisation gap to fix', 'yellow',
         'gate, bundle or price an AI tier'),
    ]
    for i, (a, b, c, d) in enumerate(rows):
        y = 108 + i * 66
        s.box(20, y, 340, 56, a, 'blue', fs=14, opacity=45)
        s.box(380, y, 240, 56, b, c, fs=14, opacity=50)
        s.box(640, y, 300, 56, d, 'teal', fs=14, opacity=40)
    s.box(20, 318, 920, 140, None, 'purple', opacity=25)
    s.text(36, 328, 'margin maths for one substituted session', 18, PURPLE)
    s.text(36, 360, 'session: earns Rs 200, costs Rs 120 in expert time: margin Rs 80', 15, INK, ff=3)
    s.text(36, 386, 'AI answer: earns nothing, costs Rs 1 to 3 in inference', 15, INK, ff=3)
    s.text(36, 412, 'net: Rs 81 to 83 lost per substitution, before any gain', 15, RED, ff=3)
    s.text(36, 438, 'retention or the annual plan must win that back', 15, GREEN, ff=3)
    s.box(0, 476, 960, 38, 'recommendation: hand off to the paid core, premium tier for unlimited AI',
          'green', fs=16, opacity=50)
    s.save('l21-cannibalisation-matrix')


# 8 ─ big picture: the AI answer skeleton ──────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'The AI answer skeleton: eight steps, guardrails as a veto',
          'every AI case in this chapter follows the same order')
    steps = [
        ('1 clarify', 'which exam,\ngoal, scope?'),
        ('2 users', 'which segment?\nwhy this one?'),
        ('3 pain points', 'what hurts,\nfor whom?'),
        ('4 solutions', 'what to build\nfirst?'),
        ('5 prioritise', 'why this\norder?'),
        ('6 metrics', 'North Star and\nthe veto?'),
        ('7 risks', 'what fails,\nwhich eval?'),
        ('8 summary', 'one paragraph,\nunder 30 s'),
    ]
    for i, (name, q) in enumerate(steps):
        x = 10 + i * 118
        s.box(x, 100, 110, 64, name, 'orange', fs=14, opacity=55)
        s.text(x + 2, 176, q, 12, GREY, ff=3)
    s.box(10, 226, 936, 40, 'guardrails act as a veto on every metric step', 'red', fs=16, opacity=40)
    s.box(10, 280, 936, 40, 'AI extras: data, evals, failure modes, human in the loop, kill criteria',
          'teal', fs=16, opacity=50)
    s.box(10, 334, 936, 40, 'scope first: one user, one job, before any feature', 'blue', fs=16, opacity=45)
    s.box(10, 388, 936, 40, 'each step must follow from the one before it', 'purple', fs=16, opacity=35)
    s.box(10, 442, 936, 40, 'the North Star sits on the outcome, never on usage', 'yellow', fs=16, opacity=60)
    s.save('l21-big-picture')


for f in [d_exam_doubt_loop, d_nav_phases, d_resume_metric_tree, d_hallucination_rca,
          d_dispute_success_fee, d_support_copilot_flow, d_cannibalisation_matrix, d_big_picture]:
    f()

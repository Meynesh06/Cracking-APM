# Excalidraw scenes for Chapter 25 (page 22, l22-*). Run: python3 diagrams_l22.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)


# 1 ─ 25.1 the 20-minute drill on one bar ────────────────────────────────────────────────────────────
def d_timer_bar():
    s = Scene()
    title(s, '25.1 The 20-minute drill on one clock',
          'nine phases back to back; the core analysis gets the longest slot')
    x0, ppm = 40, 44                     # 44 px per minute, 880 px for 20 minutes
    phases = [(0, 1, 'read and restate'), (1, 3, 'clarify'), (3, 4, 'structure'),
              (4, 10, 'core analysis'), (10, 14, 'answer'), (14, 16, 'metrics'),
              (16, 18, 'risks'), (18, 19, 'summary'), (19, 20, 'self-check')]
    for i, (a, b, name) in enumerate(phases):
        op = 85 if name == 'core analysis' else 55
        s.box(x0 + a * ppm, 120, (b - a) * ppm, 70, str(i + 1), 'orange', fs=17, ff=3, opacity=op)
    for m in (0, 5, 10, 15, 20):
        s.line([(x0 + m * ppm, 194), (x0 + m * ppm, 202)], color=GREY, sw=2)
        s.text(x0 + m * ppm - 12, 208, f'{m}:00', 14, GREY, ff=3)
    s.text(x0, 236, 'the clock never stops: at 20:00 you stop, even mid-sentence', 16, RED)
    cols = [(20, 0), (340, 3), (660, 6)]
    for n, (x, start) in enumerate(cols):
        for j in range(3):
            i = start + j
            a, b, name = phases[i]
            y = 272 + j * 30
            s.text(x, y, f'{i + 1}  {name}', 17, INK)
            s.text(x + 190, y, f'{a}:00-{b}:00', 15, GREY, ff=3)
    s.box(0, 380, 960, 60, 'if short at a checkpoint: skip detail, never skip the next phase', 'yellow', fs=17, opacity=60)
    s.text(0, 456, 'for AI cases, 30 seconds of the risks slot go to evals and data needs', 16, PURPLE)
    s.save('l22-timer-bar')


# 2 ─ 25.1 the two variants: quick drill and follow-up loop ─────────────────────────────────────────
def d_variants():
    s = Scene()
    title(s, '25.1 Variants: the 10-minute drill and the follow-up loop',
          'the quick drill is six phases; follow-ups come after your summary')
    s.text(0, 84, '10-minute quick drill (for daily reps or lateral prompts)', 17, INK)
    segs = [(0, 1, 'restate'), (1, 2, 'clarify'), (2, 3, 'structure'),
            (3, 7, 'core analysis and answer'), (7, 9, 'metrics'), (9, 10, 'summary')]
    for a, b, name in segs:
        s.box(a * 92, 112, (b - a) * 92, 56, name, 'orange', fs=15, opacity=55)
    for m, x in ((0, 0), (5, 460), (10, 900)):
        s.text(x, 180, f'{m}:00', 14, GREY, ff=3)
    s.text(0, 226, 'follow-up drill: real rounds keep going after your summary', 17, INK)
    steps = [
        ('summary spoken, 30-45 s', 'orange'),
        ('interviewer asks a follow-up', 'blue'),
        ('write three follow-ups you would ask', 'orange'),
        ('answer one in 2 minutes', 'green'),
    ]
    for i, (t, c) in enumerate(steps):
        x = 20 + i * 240
        s.box(x, 262, 200, 62, t, c, fs=15, opacity=50)
        if i < 3:
            s.arrow([(x + 202, 293), (x + 238, 293)], color=GREY, sw=3)
    s.text(20, 346, 'quantify: "how often do people use Google Photos?"', 16, INK)
    s.text(20, 372, 'defend a trade-off, or "what if the A/B test showed X?"', 16, INK)
    s.box(0, 414, 960, 48, 'the 20-minute drill trains the core answer; the follow-up drill trains the rest',
          'purple', fs=16, opacity=30)
    s.save('l22-variants')


# 3 ─ 25.2 the peer mock: three roles and 35 minutes ───────────────────────────────────────────────
def d_mock_loop():
    s = Scene()
    title(s, '25.2 The peer mock: three roles, 35 minutes',
          'roles rotate; the observer scores with the rubric, the interviewer does not coach')
    s.box(20, 100, 280, 118, 'interviewer\nreads the prompt, answers clarifying\nquestions from a fact sheet, asks follow-ups',
          'blue', fs=14, opacity=45)
    s.box(340, 100, 280, 118, 'candidate\nthe 20-minute answer, structured\nas in the 25.1 drill', 'orange', fs=14, opacity=50)
    s.box(660, 100, 280, 118, 'observer\nscores with the rubric, notes the\nclock time at each phase', 'purple', fs=14, opacity=40)
    s.arrow([(302, 159), (336, 159)], color=GREY, sw=3)
    s.arrow([(622, 159), (656, 159)], color=GREY, sw=3)
    s.arrow([(800, 222), (800, 250)], color=GREY, sw=2)
    s.arrow([(800, 250), (160, 250)], color=GREY, sw=2)
    s.arrow([(160, 250), (160, 222)], color=GREY, sw=2)
    s.text(380, 254, 'roles rotate', 15, GREY)
    total = 35 * 26
    x = 20
    for lab, mins, c in (('candidate: 20 min', 20, 'orange'), ('follow-ups: 5 min', 5, 'blue'),
                         ('feedback: 10 min', 10, 'green')):
        s.box(x, 290, mins * 26, 50, lab, c, fs=14, opacity=50)
        x += mins * 26
    s.box(0, 360, 960, 46, 'two people only: the interviewer also scores, right after the case', 'yellow', fs=16, opacity=60)
    s.box(0, 416, 960, 46, 'score independently, then compare; one piece of evidence per score', 'green',
          fs=16, opacity=40)
    s.save('l22-mock-loop')


# 4 ─ 25.2 the rubric anchors grid ────────────────────────────────────────────────────────────────────
def d_rubric_anchors():
    s = Scene()
    title(s, '25.2 Rubric anchors: 1, 3 and 5 for each criterion',
          'the same eight criteria every time, so scores can be compared week to week')
    heads = [(220, '1 (weak)', 'red'), (462, '3 (adequate)', 'orange'), (704, '5 (strong)', 'green')]
    for x, t, c in heads:
        s.box(x, 92, 232, 32, t, c, fs=15, opacity=45)
    rows = [
        ('clarify and scope', 'starts answering at once', 'some questions, goal missed',
         'restates goal, 2-3 sharp questions'),
        ('structure', 'no framework, jumps around', 'framework named, buckets overlap',
         'clear MECE buckets, signposted'),
        ('user and segmentation', 'one generic user', 'two segments, weak pain points',
         'segments by need, pains tied'),
        ('solution depth', 'ideas not linked to users', 'good ideas, few trade-offs',
         'linked to pains, MVP chosen'),
        ('prioritisation', 'none, or no reasons given', 'framework applied, reasons thin',
         'framework justified, trade-off'),
        ('metrics and guardrails', 'vague ("engagement")', 'North Star, no guardrail',
         'North Star, guardrails, method'),
        ('AI judgement (AI only)', 'ignores data, evals, failures', 'mentions hallucination or privacy',
         'evals, failure modes, kill criteria'),
        ('communication and time', 'rambles, runs out of time', 'mostly clear, time uneven',
         'concise, spoken summary, on time'),
    ]
    for i, (crit, a, b, c) in enumerate(rows):
        y = 132 + i * 38
        s.box(20, y, 190, 32, crit, 'purple', fs=14, opacity=30)
        for x, t, col in ((220, a, 'red'), (462, b, 'orange'), (704, c, 'green')):
            s.box(x, y, 232, 32, t, col, fs=13, opacity=22)
    s.text(20, 442, 'non-AI cases use seven criteria (out of 35); AI cases add the eighth (out of 40)', 16, PURPLE)
    s.save('l22-rubric-anchors')


# 5 ─ 25.2 the pass line ──────────────────────────────────────────────────────────────────────────────
def d_pass_line():
    s = Scene()
    title(s, '25.2 The bar: 60% of the total, plus two overrides',
          'a total on the line passes; a criterion at 1 still sends you back to the weakest two')
    px = lambda v: 60 + v * 840
    s.line([(px(0), 200), (px(1), 200)], color=GREY, sw=3)
    for v, lab in ((0.0, '0%'), (0.6, '60%'), (1.0, '100%')):
        s.line([(px(v), 194), (px(v), 206)], color=GREY, sw=2)
        s.text(px(v) - 14, 212, lab, 15, GREY, ff=3)
    s.box(px(0), 150, px(0.6) - px(0), 40, 'below the bar', 'red', fs=16, opacity=30)
    s.box(px(0.6), 150, px(1) - px(0.6), 40, 'at the bar and above', 'green', fs=16, opacity=30)
    s.text(px(0.6) - 150, 92, '21 of 35 (non-AI) = 60%', 16, YEL)
    s.text(px(0.6) - 150, 114, '24 of 40 (AI) = 60%', 16, YEL)
    s.line([(px(0.6), 150), (px(0.6), 200)], color=YEL, dashed=True, sw=2)
    s.text(px(0), 240, 'below: the next two sessions focus on the weakest two criteria', 15, RED)
    s.box(60, 290, 840, 44, 'override 1: any criterion at 1 sends you back, even above 60%', 'red', fs=16, opacity=40)
    s.box(60, 346, 840, 44, 'interview-ready: 4+ on every criterion, three mocks in a row', 'green',
          fs=16, opacity=45)
    s.text(60, 412, 'the bar is a floor for each mock, not a target for the whole course', 16, PURPLE)
    s.text(60, 440, 'non-AI mocks: seven criteria, 35 points; AI mocks: eight, 40 points', 15, GREY)
    s.save('l22-pass-line')


# 6 ─ 25.3 the weekly cycle ───────────────────────────────────────────────────────────────────────────
def d_weekly_cycle():
    s = Scene()
    title(s, '25.3 The weekly cycle: drill, review, mock, re-attempt',
          'the same case comes back on Saturday, with only the error log as a checklist')
    days = [
        (20, 'Mon: timed drill on a new case (Chapter 24)', 'orange'),
        (260, 'Tue: review the recording, update the error log', 'teal'),
        (500, 'Thu: peer mock, scored on the rubric', 'purple'),
        (740, "Sat: re-attempt Monday's case from the log", 'green'),
    ]
    for i, (x, t, c) in enumerate(days):
        s.box(x, 110, 200, 116, t, c, fs=15, opacity=45)
        if i < 3:
            s.arrow([(x + 202, 168), (x + 238, 168)], color=GREY, sw=3)
    s.arrow([(840, 228), (840, 262), (120, 262), (120, 230)], color=GREY, sw=2)
    s.text(380, 268, 'next week', 15, GREY)
    s.box(20, 310, 920, 44, 'compare the rubric scores: a better repeat beats a good first try',
          'yellow', fs=16, opacity=60)
    s.box(20, 366, 920, 44, 'error log: after five entries, the most common type is next week\'s focus',
          'teal', fs=16, opacity=40)
    s.text(20, 428, 'a fix column turns each error into a rule for the next drill', 16, PURPLE)
    s.save('l22-weekly-cycle')


# 7 ─ the practice loop on one page ───────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 25 on one page: the practice loop',
          'drill, record, log, mock, re-attempt, with one rubric throughout')
    steps = [
        ('1 timed drill\n(20 minutes)', 'orange'),
        ('2 record and review\n(within 24 hours)', 'teal'),
        ('3 error log: a fix\nfor every error', 'teal'),
        ('4 peer mock on the\nsame rubric', 'purple'),
        ('5 re-attempt after\na week', 'green'),
    ]
    for i, (t, c) in enumerate(steps):
        x = 20 + i * 186
        s.box(x, 100, 170, 70, t, c, fs=14, opacity=50)
        if i < 4:
            s.arrow([(x + 172, 135), (x + 184, 135)], color=GREY, sw=3)
    s.arrow([(850, 172), (850, 220), (105, 220), (105, 172)], color=GREY, sw=2)
    s.text(380, 224, 'repeat every week', 15, GREY)
    s.box(0, 254, 960, 44, 'practise the lowest-scoring criterion on purpose', 'yellow', fs=16, opacity=60)
    s.box(0, 306, 960, 44, 'bar: 60% of the total (21/35 or 24/40), and no criterion at 1',
          'red', fs=16, opacity=35)
    s.box(0, 358, 960, 44, 'interview-ready: 4+ on every criterion across three mocks in a row',
          'green', fs=16, opacity=40)
    s.box(0, 410, 960, 44, 'fixed clock, same rubric, one table: progress shows over weeks',
          'purple', fs=16, opacity=30)
    s.save('l22-big-picture')


for f in [d_timer_bar, d_variants, d_mock_loop, d_rubric_anchors, d_pass_line, d_weekly_cycle, d_big_picture]:
    f()

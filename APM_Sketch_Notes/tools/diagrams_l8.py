# Excalidraw scenes for Chapter 11 (page 8, l8-*). Run: python3 diagrams_l8.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)


def lines(s, x, y, items, fs=16, color=INK, step=24):
    for i, t in enumerate(items):
        s.text(x, y + i * step, t, fs, color)


# 1 ─ from everyone to one persona ──────────────────────────────────────────────────────────────────
def d_segmentation_funnel():
    s = Scene()
    title(s, 'From everyone to one persona',
          'segment the market, then pick one persona and design for them')
    s.box(280, 84, 400, 52, 'all users: "everyone" is not a design target', 'blue', fs=17)
    s.arrow([(480, 136), (480, 166)], color=ORANGE, sw=3)
    segs = ['by goals', 'by usage', 'by context', 'by demographics']
    for i, t in enumerate(segs):
        s.box(20 + i * 236, 170, 220, 56, 'segment\n' + t, 'purple', fs=16, opacity=55)
    s.line([(130, 236), (830, 236)], color=GREY, sw=2)
    s.arrow([(160, 236), (160, 262)], color=ORANGE, sw=3)
    s.arrow([(480, 236), (480, 262)], color=ORANGE, sw=3)
    s.arrow([(800, 236), (800, 262)], color=ORANGE, sw=3)
    s.box(20, 264, 280, 76, 'PRIMARY persona\ndesign for this one first', 'green', fs=16, opacity=50)
    s.box(340, 264, 280, 76, 'SECONDARY persona\nserved if it costs little', 'blue', fs=16, opacity=40)
    s.box(660, 264, 280, 76, 'NEGATIVE persona\nnamed to show scope discipline', 'grey', fs=16, opacity=50)
    s.text(20, 360, 'bases: demographics, usage intensity, goals, context', 16, INK)
    s.text(20, 388, 'weak: a "persona" that is only a usage bucket', 16, RED)
    s.box(0, 430, 940, 52, 'stay with one persona from the first pain point to the final solution',
          'yellow', fs=17, opacity=60)
    s.save('l8-segmentation-funnel')


# 2 ─ a persona card ───────────────────────────────────────────────────────────────────────────────
def d_persona_card():
    s = Scene()
    title(s, 'A persona card: who they are, what they need',
          'one card per answer, and a role for each persona')
    s.box(0, 84, 430, 340, None, 'blue', opacity=25)
    s.text(16, 96, 'persona card (template)', 18, PURPLE)
    lines(s, 16, 134, ['name', 'one-line description', 'behaviour: what they do, and when',
                       'needs and goals: what they want', 'pain points: what gets in the way'],
          fs=16, step=38)
    s.text(16, 322, 'demographics or psychographics, tied to behaviour', 15, INK)
    s.text(16, 348, 'a usage bucket alone is not enough', 15, RED)
    s.text(16, 380, 'a 2x2 or a small table keeps it easy to follow', 15, GREY)
    s.box(470, 84, 470, 96, 'PRIMARY\ndesign for this one first\nhighest value or largest unmet need',
          'green', fs=16, opacity=50)
    s.box(470, 194, 470, 96, 'SECONDARY\nserved if it costs little extra\nmay need convincing',
          'blue', fs=16, opacity=40)
    s.box(470, 304, 470, 96, 'NEGATIVE\nthe person you will not focus on\nnaming them shows scope discipline',
          'grey', fs=16, opacity=50)
    s.box(0, 440, 940, 60, 'no research yet? a proto-persona: Goals, Motivation, Attitudes, Behaviours',
          'purple', fs=16, opacity=30)
    s.save('l8-persona-card')


# 3 ─ jobs to be done ──────────────────────────────────────────────────────────────────────────────
def d_jtbd():
    s = Scene()
    title(s, 'Jobs to be done: the progress the user wants',
          'the product competes with whatever the user would do otherwise')
    s.box(0, 84, 940, 46, 'When [situation], I want to [motivation], so I can [outcome].',
          'purple', fs=18, opacity=40)
    steps = ['1 name the situation', '2 name the job', '3 list the alternatives', '4 judge the product']
    for i, t in enumerate(steps):
        s.box(20 + i * 236, 150, 220, 52, t, 'orange', fs=16, opacity=50)
        if i < 3:
            s.arrow([(240 + i * 236, 176), (256 + i * 236, 176)], color=ORANGE, sw=3)
    s.text(0, 226, 'the milkshake story (Christensen, Competing Against Luck)', 17, PURPLE)
    s.box(0, 258, 220, 86, 'solo commuter\nbuys a shake before 8 am', 'blue', fs=15, opacity=50)
    s.arrow([(224, 301), (260, 301)], color=ORANGE, sw=3)
    s.box(264, 258, 230, 86, 'hired it to stay full and\nmake a long drive less boring',
          'orange', fs=15, opacity=40)
    s.arrow([(498, 301), (534, 301)], color=ORANGE, sw=3)
    s.box(538, 258, 200, 86, 'rivals: bagels, bananas,\nand boredom', 'red', fs=15, opacity=40)
    s.box(742, 258, 198, 86, 'fix: a thicker shake,\nfaster purchase', 'green', fs=15, opacity=50)
    s.box(0, 370, 940, 46, 'the rival was bagels, bananas and boredom, not other shakes',
          'yellow', fs=16, opacity=50)
    s.text(0, 436, 'too abstract? once the job is clear, move on to flows and UI', 16, GREY)
    s.save('l8-jtbd')


# 4 ─ the 5Es journey ──────────────────────────────────────────────────────────────────────────────
def d_5es():
    s = Scene()
    title(s, 'The 5Es: check each stage of the journey',
          'Kindle reader example: the pain sits at Engage and Exit')
    es = [('Entice', 'what gets the\nuser to start?'),
          ('Enter', 'how easy is\nonboarding?'),
          ('Engage', 'is the core task\nrewarding?'),
          ('Exit', 'how do they leave\nor finish?'),
          ('Extend', 'do they come back\nand bring others?')]
    for i, (name, q) in enumerate(es):
        x = i * 188
        s.box(x, 84, 176, 50, name, 'orange', fs=19, opacity=55)
        s.text(x + 4, 144, q.split('\n')[0], 14, GREY)
        s.text(x + 4, 162, q.split('\n')[1], 14, GREY)
    s.text(0, 200, 'Kindle reader who drops off mid-book', 17, PURPLE)
    row = ['sees a\nrecommendation', 'searches, buys\nor borrows',
           'reads, tracks\nprogress, looks up\nmeanings', 'stops reading\n(the problem)',
           'shares reviews\nand ratings']
    colours = ['blue', 'blue', 'red', 'red', 'blue']
    ops = [40, 40, 35, 60, 40]
    for i, t in enumerate(row):
        s.box(i * 188, 230, 176, 84, t, colours[i], fs=14, opacity=ops[i])
    s.box(0, 336, 940, 46, 'so fix re-engagement: progress nudges, chapter summaries',
          'green', fs=16, opacity=45)
    s.text(0, 398, 'common mistake: mapping every stage. "Don\'t forcefit!"', 16, RED)
    s.text(0, 426, 'one persona, 4 to 6 stages, mark the pain at each stage', 16, INK)
    s.save('l8-5es-journey')


# 5 ─ pain points: severity against reach ──────────────────────────────────────────────────────────
def d_pain_grid():
    s = Scene()
    title(s, 'Pain points: severity against reach, then pick 1 to 3',
          'High = blocks the core task, or loses money, data or trust')
    s.text(170, 92, 'many of this persona hit it', 16, PURPLE)
    s.text(510, 92, 'few of this persona hit it', 16, PURPLE)
    rows = [('High', 128), ('Moderate', 224), ('Low', 320)]
    for lab, y in rows:
        s.text(20, y + 30, lab, 18, PURPLE)
    cells = {
        (0, 0): ('red', 60, 'pick first: blocks the core task\nand affects many users'),
        (0, 1): ('yellow', 60, 'rare but severe: can still outrank\ncommon annoyances'),
        (1, 0): ('orange', 50, 'slows the task or frustrates, but\nthe user has a workaround'),
        (1, 1): ('grey', 50, 'lower priority: note it'),
        (2, 0): ('grey', 50, 'cosmetic or rare: note it,\ndo not build for it'),
        (2, 1): ('grey', 50, 'cosmetic or rare: note it,\ndo not build for it'),
    }
    for (r, c), (col, op, t) in cells.items():
        x = 170 + c * 340
        y = rows[r][1]
        s.box(x, y, 330, 86, t, col, fs=15, opacity=op)
    s.box(0, 430, 940, 52, 'give one line of reason per rating: reasoning beats the label',
          'yellow', fs=16, opacity=50)
    s.save('l8-pain-grid')


# 6 ─ five steps from pain points to a fix ─────────────────────────────────────────────────────────
def d_pain_steps():
    s = Scene()
    title(s, 'Five steps from pain points to a chosen fix',
          'the list is long, so prioritize before any solution')
    steps = ['1 pick the\ntarget segment', '2 map the\njourney', '3 list pain\npoints',
             '4 prioritize\nHigh, Moderate, Low', '5 solve the\nchosen ones']
    notes = ['one persona,\nno drift', 'open to finish,\nhow they feel',
             'pain and unmet needs,\ncheck competitors', 'severity, reach,\none line of reason',
             'only the prioritized\nlist']
    for i, t in enumerate(steps):
        x = i * 192
        s.box(x, 110, 172, 80, t, 'orange', fs=16, opacity=50)
        if i < 4:
            s.arrow([(x + 172, 150), (x + 192, 150)], color=ORANGE, sw=3)
        n = notes[i].split('\n')
        s.text(x + 2, 202, n[0], 14, GREY)
        s.text(x + 2, 220, n[1], 14, GREY)
    s.box(0, 268, 940, 176, None, 'purple', opacity=25)
    s.text(16, 280, 'grocery app, persona: working parent who orders weekly', 17, PURPLE)
    lines(s, 16, 314, ['items substituted without asking: High (breaks the core job)',
                       'slot not available at night: High (blocks the order)',
                       'search misses "bhindi": Moderate (workaround: browse)',
                       'app icon looks dated: Low (do not build for it)',
                       'pick the two Highs, and say why'], fs=16, step=24)
    s.save('l8-pain-steps')


# 7 ─ big picture cheat-sheet ──────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 11 on one page: one persona, four tools',
          'each tool answers one question about the user')
    cols = [('11.1 Persona', 'one segment,\none primary persona', 'who do we design for?', 'blue'),
            ('11.2 Jobs to be done', 'the progress sought,\nand the alternative',
             'what job, and what would\nthey do otherwise?', 'purple'),
            ('11.3 Journey and 5Es', 'stages checked through\nfive lenses', 'where in the flow\nis the pain?', 'orange'),
            ('11.4 Pain points', 'rate High, Moderate, Low;\npick 1 to 3', 'which ones do we fix\nfirst, and why?', 'red')]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 236
        s.box(x, 84, 226, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 226, 110, core, c, fs=15, opacity=45)
        s.box(x, 280, 226, 92, q, 'yellow', fs=15, opacity=60)
    s.box(10, 392, 940, 58, 'Keep one persona from the first pain point to the final solution',
          'purple', fs=17, opacity=35)
    s.box(10, 462, 940, 36, 'good answer: one persona, a job, a stage, a ranked pain',
          'green', fs=15, opacity=45)
    s.save('l8-big-picture')


for f in [d_segmentation_funnel, d_persona_card, d_jtbd, d_5es, d_pain_grid, d_pain_steps, d_big_picture]:
    f()

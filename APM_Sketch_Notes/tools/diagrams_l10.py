# Excalidraw scenes for Chapter 13 (page 10, l10-*). Run: python3 diagrams_l10.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)


def lines(s, x, y, items, fs=16, color=INK, step=24):
    for i, t in enumerate(items):
        s.text(x, y + i * step, t, fs, color)


# 1 ─ the five-step critique: five lenses ─────────────────────────────────────────────────────────
def d_five_lenses():
    s = Scene()
    title(s, 'Five-step app critique: five lenses on one app',
          'set the context and goals first, then walk the lenses')
    s.box(0, 84, 940, 42, 'context: why this app  |  goals: business aim, user aim',
          'purple', fs=15, opacity=35)
    lenses = ['1 jobs to be done', '2 personas', '3 user familiarity', '4 inclusivity', '5 zoom in and out']
    qs = [('what is it hired for?', 'without it: what then?'),
          ('who uses it, goals,', 'motivations, scenarios'),
          ('new, intermediate,', 'and expert users'),
          ('vision, hearing, motor', 'or cognitive barriers'),
          ('aesthetic, functional', 'and strategic layers')]
    for i, name in enumerate(lenses):
        x = i * 192
        s.box(x, 146, 176, 60, name, 'purple', fs=15, opacity=55)
        s.text(x + 2, 218, qs[i][0], 14, GREY)
        s.text(x + 2, 236, qs[i][1], 14, GREY)
    s.box(0, 290, 940, 46, 'JTBD gives objective criteria: compare with the alternative',
          'yellow', fs=16, opacity=50)
    s.box(0, 352, 940, 74, None, 'green', opacity=25)
    lines(s, 16, 360, ['finish with 2-3 prioritized improvements',
                       'each tied to a lens, and to a metric',
                       'linked to the goal the interviewer set'], fs=16, step=22)
    s.save('l10-five-lenses')


# 2 ─ user familiarity ─────────────────────────────────────────────────────────────────────────────
def d_familiarity():
    s = Scene()
    title(s, 'User familiarity: new, intermediate and expert users',
          'the same app serves three levels; each needs something different')
    cols = [('new users', ['value proposition', 'sign-up friction', 'onboarding']),
            ('intermediate users', ['how the app guides them', 'where the shortcuts are',
                                    'how it grows with their needs']),
            ('expert users', ['advanced functionality', 'missing power tools',
                              'most relevant in task-heavy apps'])]
    for i, (head, body) in enumerate(cols):
        x = i * 320
        s.box(x, 84, 300, 46, head, 'blue', fs=18, opacity=50)
        s.box(x, 142, 300, 128, None, 'blue', opacity=22)
        lines(s, x + 14, 156, body, fs=15, step=30)
    s.text(0, 290, 'Google Maps, a commuter: the same lens, two levels', 17, PURPLE)
    s.box(0, 322, 460, 52, 'new user: sets home and work', 'blue', fs=16, opacity=40)
    s.box(480, 322, 460, 52, 'expert: wants departure-time alarms', 'blue', fs=16, opacity=40)
    s.box(0, 392, 940, 50, 'task-heavy apps such as Photoshop or Visual Studio: experts',
          'green', fs=15, opacity=35)
    s.save('l10-familiarity')


# 3 ─ inclusivity: four barriers ───────────────────────────────────────────────────────────────────
def d_inclusivity():
    s = Scene()
    title(s, 'Inclusivity: four kinds of barrier to check',
          'accessibility is a user need and a risk, not a nice-to-have')
    items = [('vision', ['low vision,', 'colour blindness,', 'screen glare']),
             ('hearing', ['captions,', 'backup cues,', 'a noisy train station']),
             ('motor', ['tap target size,', 'intricate gestures,', 'using it while walking']),
             ('cognitive', ['memory load,', 'complex operations'])]
    for i, (head, body) in enumerate(items):
        x = i * 240
        s.box(x, 84, 220, 44, head, 'red', fs=18, opacity=45)
        s.box(x, 136, 220, 116, None, 'red', opacity=18)
        lines(s, x + 14, 146, body, fs=15, step=26)
    s.text(0, 270, 'a benchmark when you critique another app', 17, PURPLE)
    s.box(0, 300, 300, 46, 'VoiceOver', 'green', fs=16, opacity=40)
    s.box(320, 300, 300, 46, 'Dynamic Type', 'green', fs=16, opacity=40)
    s.box(640, 300, 300, 46, 'Reduce Motion', 'green', fs=16, opacity=40)
    s.box(0, 370, 940, 60, 'in many places accessibility is the law\na checkout gap can outrank a revenue idea',
          'yellow', fs=15, opacity=50)
    s.save('l10-inclusivity')


# 4 ─ zoom levels: strategy to screen ──────────────────────────────────────────────────────────────
def d_zoom():
    s = Scene()
    title(s, 'Zoom out to strategy, zoom in to one screen',
          'aesthetic is visible; functional and strategic are not')
    s.text(0, 84, 'layer', 15, PURPLE)
    s.text(330, 84, 'Google Maps, the commuter example', 15, PURPLE)
    layers = [('strategic: why it exists', 'purple', 'local search and ads', 'purple'),
              ('functional: how it works', 'orange', 'routing and live traffic', 'orange'),
              ('aesthetic: how it looks', 'blue', 'colour-coded traffic lines', 'red')]
    for i, (lab, col, ex, excol) in enumerate(layers):
        y = 108 + i * 98
        s.box(0, y, 300, 78, lab, col, fs=16, opacity=50)
        s.box(330, y, 610, 78, ex, excol, fs=16, opacity=30 if excol != 'red' else 40)
    s.text(330, 400, 'a colour-blindness risk on the traffic colours', 15, RED)
    s.box(0, 432, 940, 50, 'visible: brand, visual, motion, sound, touch. invisible: strategy, function',
          'yellow', fs=15, opacity=45)
    s.save('l10-zoom')


# 5 ─ favourite product: four steps and Lin's three criteria ───────────────────────────────────────
def d_favourite():
    s = Scene()
    title(s, 'Favourite product: four steps that show depth',
          'name the goal, not the feature; then compare and improve')
    steps = ['1 the problem it solves\n(the user goal)', '2 how it does it, and\nwhat is "neat"',
             '3 compare with the\nalternatives', '4 how you would\nimprove it']
    for i, t in enumerate(steps):
        s.box(i * 240, 84, 220, 66, t, 'orange', fs=15, opacity=50)
    ex = [['Mint.com example:', '"save money by understanding"', '"how you spend it"'],
          ['data advantage, a great', 'interface, a win-win revenue', 'model, cost advantage,', 'emotional pull'],
          ['direct competitors, and', 'indirect substitutes;', 'say why you do not use them'],
          ['expect this as a', 'follow-up; use the', 'five-lens critique']]
    for i, body in enumerate(ex):
        lines(s, i * 240 + 2, 160, body, fs=14, color=GREY, step=19)
    s.text(0, 288, 'Lin, Decode and Conquer: three criteria (Dieter Rams principles)', 17, PURPLE)
    crit = ['usefulness', 'innovation', 'ease of use']
    for i, c in enumerate(crit):
        s.box(i * 320, 316, 300, 44, c, 'purple', fs=17, opacity=50)
    s.box(0, 372, 940, 58, 'show how it meets each criterion, with evidence, and a contrast with peers',
          'purple', fs=15, opacity=30)
    s.box(0, 440, 940, 40, 'honesty is another option; stop after 2-3 minutes', 'green', fs=15, opacity=35)
    s.save('l10-favourite')


# 6 ─ big picture cheat-sheet ──────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 13 on one page: critique and favourite product',
          'both test the user side and the business side at once')
    s.box(0, 84, 460, 44, 'critique (13.1)', 'orange', fs=18, opacity=55)
    s.box(0, 136, 460, 176, None, 'orange', opacity=22)
    lines(s, 16, 150, ['context and goals first (the business aim)',
                       'five lenses: JTBD, personas, familiarity,',
                       'inclusivity, zoom levels',
                       'JTBD: compare with the user\'s alternative',
                       'cover new, intermediate and expert users',
                       'finish with 2-3 improvements, each with a metric'],
          fs=15, step=26)
    s.box(480, 84, 460, 44, 'favourite product (13.2)', 'orange', fs=18, opacity=55)
    s.box(480, 136, 460, 176, None, 'orange', opacity=22)
    lines(s, 496, 150, ['1 the user goal, not the feature',
                        '2 what makes it "neat"',
                        '3 alternatives: direct and indirect',
                        '4 how you would improve it',
                        'Lin: up to three criteria, with evidence',
                        'one example of you using the product'],
          fs=15, step=26)
    s.box(0, 332, 940, 56, 'every improvement: one metric, and the trade-off you accept',
          'yellow', fs=16, opacity=50)
    s.box(0, 402, 940, 56, 'set the context and goals first; ask the business objective',
          'green', fs=16, opacity=40)
    s.save('l10-big-picture')


for f in [d_five_lenses, d_familiarity, d_inclusivity, d_zoom, d_favourite, d_big_picture]:
    f()

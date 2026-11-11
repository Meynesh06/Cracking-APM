# Excalidraw scenes for Chapter 12 (page 9, l9-*). Run: python3 diagrams_l9.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


def lines(s, x, y, items, fs=16, color=INK, step=24):
    for i, t in enumerate(items):
        s.text(x, y + i * step, t, fs, color)


# 1 ─ the seven CIRCLES steps ──────────────────────────────────────────────────────────────────────
def d_circles_steps():
    s = Scene()
    title(s, 'CIRCLES: seven steps, one letter each',
          'say the framework out loud at the start so the interviewer follows')
    steps = [('C', 'Comprehend', "3W's and H,\ngoal, constraints"),
             ('I', 'Identify', 'one persona\ncard'),
             ('R', 'Report', '2-3 user\nstories'),
             ('C', 'Cut', 'one need\nA-C or revenue'),
             ('L', 'List', '3+ solutions\nbrainstorm'),
             ('E', 'Evaluate', 'pros and cons\nper solution'),
             ('S', 'Summarize', 'recommend one\n+ why')]
    for i, (letter, name, tool) in enumerate(steps):
        x = 10 + i * 134
        s.box(x, 84, 124, 80, f'{letter}\n{name}', 'purple', fs=16, opacity=55)
        t = tool.split('\n')
        s.text(x + 2, 178, t[0], 14, GREY)
        s.text(x + 2, 196, t[1], 14, GREY)
    s.box(0, 236, 940, 46, 'Clarify with the 3W\'s and H before you name a persona',
          'blue', fs=16, opacity=40)
    s.box(0, 294, 940, 46, 'Cut tools: Lin\'s A-C matrix, or revenue per point of effort',
          'yellow', fs=16, opacity=45)
    s.box(0, 352, 940, 46, 'Summarize: name it, recap it, say why it beat the others',
          'green', fs=16, opacity=40)
    s.box(0, 410, 940, 46, 'a 15-20 minute answer: spend the time on Cut, List, Evaluate',
          'orange', fs=16, opacity=40)
    s.save('l9-circles-steps')


# 2 ─ Kat, the persona and the user stories ────────────────────────────────────────────────────────
def d_kat_stories():
    s = Scene()
    title(s, 'Report the needs: Kat, the traveling reader',
          'a persona, then user stories written from the template')
    s.box(0, 84, 400, 300, None, 'blue', opacity=25)
    s.text(16, 100, 'Kat, a 55-year-old', 20, INK)
    lines(s, 16, 146, ['travels four times a year', 'carries four books per trip',
                       'wants to discover new books', 'and to write one someday'],
          fs=17, step=34)
    s.box(440, 84, 500, 110, 'USER STORY 1\n"I want recommendations so that I read\nwell-written books in my favourite genres"',
          'purple', fs=15, opacity=35)
    s.box(440, 214, 500, 110, 'USER STORY 2\n"I want to write 500 words a day so that\nI can publish my memoir."',
          'purple', fs=15, opacity=35)
    s.box(0, 410, 940, 58, 'the template: As a <role>, I want <goal> so that <benefit>.',
          'purple', fs=17, opacity=30)
    s.save('l9-kat-stories')


# 3 ─ Lin's A-C matrix and the revenue-per-effort check ────────────────────────────────────────────
def d_kat_matrix():
    s = Scene()
    title(s, 'Cut: Lin\'s A-C matrix, then revenue per point of effort',
          'the matrix grades each story; the quantitative check agrees')
    heads = ['revenue', 'customer\nsatisfaction', 'ease of\nimplementation', 'overall']
    for j, h in enumerate(heads):
        s.box(230 + j * 150, 84, 140, 56, h, 'purple', fs=14, opacity=50)
    rows = [('write a book', 'A', 'green'), ('book discovery', 'C', 'grey')]
    for i, (name, grade, col) in enumerate(rows):
        y = 158 + i * 66
        s.box(20, y, 200, 50, name, 'blue', fs=16, opacity=45)
        for j in range(4):
            s.box(230 + j * 150, y, 140, 50, grade, col, fs=22, opacity=55)
    s.box(20, 298, 440, 52, 'write a book: $500,000 / 8 = $62,500 per point',
          'pink', fs=15, opacity=40)
    s.box(480, 298, 440, 52, 'book discovery: $20,000 / 2 = $10,000 per point',
          'pink', fs=15, opacity=40)
    s.text(20, 358, 'revenue impact / story size = revenue per point of effort', 15, GREY)
    s.box(0, 402, 940, 52, 'priority 1: write a book, on both the grades and the ratio',
          'green', fs=16, opacity=45)
    s.save('l9-kat-matrix')


# 4 ─ three brainstorming methods ──────────────────────────────────────────────────────────────────
def d_brainstorm():
    s = Scene()
    title(s, 'List: three brainstorming methods (Lin)',
          'at least three ideas; Lin: idea 2 or 3 is usually the best')
    cols = [('Reversal', ['flip the situation', 'buyers cannot get to the', 'dealership, so the dealership',
                          'brings the test drive home']),
            ('Attribute', ['list attributes: material, shape,', 'finish, position, then recombine',
                           'example: a plastic laundry hamper', 'mounted on the door']),
            ('Why?', ['challenge the status quo', 'why do coffee cups need handles?',
                      'because they are too hot,', 'so make an insulated mug'])]
    for i, (head, body) in enumerate(cols):
        x = i * 320
        s.box(x, 84, 300, 50, head, 'purple', fs=19, opacity=55)
        s.box(x, 146, 300, 190, None, 'orange', opacity=25)
        lines(s, x + 14, 162, body, fs=15, step=34)
    s.box(0, 360, 940, 52, 'think big; avoid "me too" and lazy "integrate X with Y" ideas',
          'red', fs=16, opacity=30)
    s.text(0, 426, 'Lin: it is fine to hold a solution in mind early and steer toward it', 16, GREY)
    s.save('l9-brainstorm')


# 5 ─ common mistakes ──────────────────────────────────────────────────────────────────────────────
def d_mistakes():
    s = Scene()
    title(s, 'Common mistakes: weak answers fail on structure and context',
          'the three the Sigma casebook names most, then Lin\'s list')
    s.text(0, 84, 'Sigma casebook: the top three', 18, PURPLE)
    sigma = ['1 jumping to features, with no customer',
             '2 rambling, unstructured answers',
             '3 not asking clarifying questions']
    for i, t in enumerate(sigma):
        s.box(0, 112 + i * 56, 300, 46, t, 'red', fs=14, opacity=30)
    s.text(0, 290, 'Sigma also flags:', 16, PURPLE)
    s.box(0, 318, 300, 40, 'abandoning the persona', 'red', fs=14, opacity=30)
    s.box(0, 364, 300, 40, 'off-scope: marketing or partnership ideas', 'red', fs=14, opacity=30)
    s.text(330, 84, 'Lin, Decode and Conquer', 18, PURPLE)
    lin = ['not knowing the product: say so, ask what it does',
           'shallow personas: heavy, normal and low usage only',
           'no constraints, use cases or link to the goal',
           '"me too" and integration ideas',
           'only one idea: aim for at least three',
           'no recommendation in the summary']
    for i, t in enumerate(lin):
        s.box(330, 112 + i * 46, 610, 40, t, 'red', fs=14, opacity=25)
    s.box(0, 416, 940, 84, None, 'green', opacity=25)
    lines(s, 16, 428, ['self-check: goal and product clear? one persona, and why?',
                       'need in a user story? prioritized, and why?',
                       'solutions the persona can use? a trade-off and a metric?'],
          fs=15, step=20)
    s.save('l9-mistakes')


# 6 ─ CIRCLES adapted for AI ───────────────────────────────────────────────────────────────────────
def d_ai_circles():
    s = Scene()
    title(s, 'CIRCLES for AI: keep the skeleton, add the AI checks',
          'general product knowledge, not from the vault sources')
    rows = [('C  Comprehend', 'Is AI the right tool? Deterministic or probabilistic?\n'
                              'What accuracy and latency are acceptable?'),
            ('I  Identify', 'Who sees the output, and who is hit by its errors?\n'
                            'Include the person who reviews or corrects it.'),
            ('R  Report', 'Add a trust story: rely on the answer without checking.\n'
                          'Add a failure-state story.'),
            ('C  Cut', 'Weigh value against data readiness, eval, cost per task.\n'
                       'No way to measure quality ranks lower.'),
            ('L  List', 'Automation level: suggestion, copilot or autonomous.\n'
                        'Include a human-in-the-loop option.'),
            ('E  Evaluate', 'Add quality distribution, hallucination risk, latency,\n'
                            'cost, privacy and fallback behaviour.'),
            ('S  Summarize', 'Add the launch plan (staged rollout, kill switch)\n'
                             'and the eval plan (golden set, online metrics).')]
    s.text(0, 84, 'standard step', 15, PURPLE)
    s.text(130, 84, 'the AI addition', 15, PURPLE)
    for i, (step, add) in enumerate(rows):
        y = 108 + i * 52
        s.box(0, y, 120, 46, step, 'purple', fs=13, opacity=50)
        a = add.split('\n')
        s.box(130, y, 520, 46, None, 'teal', opacity=35)
        s.text(140, y + 4, a[0], 14, INK)
        s.text(140, y + 23, a[1], 14, INK)
    s.text(670, 84, 'three questions for any AI answer', 15, PURPLE)
    qs = ['1. What happens when the\nmodel is wrong, and how does\nthe user recover?',
          '2. What data does it need,\nand do we have the right to\nuse it?',
          '3. What does it cost per task,\nand does the price fit\nthe value?']
    for i, q in enumerate(qs):
        s.box(670, 112 + i * 104, 270, 92, q, 'yellow', fs=14, opacity=55)
    s.box(0, 470, 940, 40, 'AI adds quality, data, failure and cost checks', 'teal', fs=16, opacity=35)
    s.save('l9-ai-circles')


# 7 ─ big picture ──────────────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 12 on one page: the CIRCLES skeleton',
          'seven steps, one persona, one prioritized need, then the AI checks')
    letters = [('C', 'Comprehend'), ('I', 'Identify'), ('R', 'Report'), ('C', 'Cut'),
               ('L', 'List'), ('E', 'Evaluate'), ('S', 'Summarize')]
    for i, (l, n) in enumerate(letters):
        s.box(10 + i * 134, 84, 124, 66, f'{l}\n{n}', 'purple', fs=15, opacity=55)
    s.box(0, 170, 940, 56, 'say the framework out loud; clarify with the 3W\'s and H',
          'blue', fs=16, opacity=40)
    s.box(0, 236, 940, 56, 'one persona, kept until the final solution', 'blue', fs=16, opacity=40)
    s.box(0, 302, 940, 56, 'prioritize one need: A-C matrix or revenue per point of effort',
          'yellow', fs=16, opacity=50)
    s.box(0, 368, 940, 56, 'three or more solutions; pros and cons; recommend one',
          'orange', fs=16, opacity=40)
    s.box(0, 434, 940, 50, 'AI: add failure recovery, data needs and cost per task',
          'teal', fs=15, opacity=40)
    s.save('l9-big-picture')


for f in [d_circles_steps, d_kat_stories, d_kat_matrix, d_brainstorm, d_mistakes, d_ai_circles,
          d_big_picture]:
    f()

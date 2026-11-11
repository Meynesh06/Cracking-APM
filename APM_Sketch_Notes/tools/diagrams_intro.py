# Excalidraw scenes for the introduction (l0-*). Run: python3 diagrams_intro.py ../diagrams/src
# lchk.sh only renders diagrams_lN.py, so the intro is rendered by hand:
#   cd tools && python3 diagrams_intro.py ../diagrams/src && node render-diagrams.mjs ../diagrams/src ../diagrams/out l0-
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


def d_big_idea():
    s = Scene()
    title(s, 'The whole prep in one picture',
          'four parts, one answer pattern: clarify, structure out loud, reason with numbers, close on a metric')
    parts = [
        ('Part II · AI products', 'chapters 4-10', 'how AI features differ, and how to judge them'),
        ('Part III · toolkit', 'chapters 11-20', 'users, design, critique, priorities, metrics, root cause, pricing, launch, strategy, execution'),
        ('Part IV · estimation', 'chapter 21', 'guesstimates from first principles'),
        ('Part V · case practice', 'chapters 22-25', 'case types, worked examples, AI case bank, practice protocol'),
    ]
    xs = [20, 262, 504, 746]
    for x, (name, ch, what) in zip(xs, parts):
        s.box(x, 84, 216, 178, f'{name}\n{ch}\n\n{what}', 'purple', fs=16, opacity=60)
    for x in xs[:-1]:
        s.arrow([(x + 220, 170), (x + 258, 170)], color=ORANGE, sw=3)
    s.text(20, 300, 'the answer you say out loud, in four steps', 19, PURPLE)
    steps = ['clarify the goal\nand the user', 'structure: a\nframework, out loud', 'reason with numbers\n(guesstimate, unit economics)', 'close on a metric\nand a trade-off']
    for i, t in enumerate(steps):
        x = 20 + i * 245
        s.box(x, 332, 220, 74, t, 'orange', fs=16, opacity=55)
        if i < 3:
            s.arrow([(x + 222, 369), (x + 243, 369)], color=ORANGE, sw=3)
    s.box(20, 430, 940, 48, 'Clarify first, structure out loud, and always close with the metric.', 'green', fs=18, opacity=45)
    s.save('l0-big-idea')


def d_colour_key():
    s = Scene()
    title(s, 'Colour key', 'the same colours mean the same things on every page')
    items = [
        ('blue', 'users, customers, personas'),
        ('purple', 'titles, frameworks and their structure (CIRCLES steps, Porter\'s forces)'),
        ('orange', 'process steps, flows, actions over time (journeys, rollouts, pipelines)'),
        ('green', 'good outcome, success metric, the chosen option, a pass'),
        ('red', 'risk, failure, pain point, guardrail breach, a rejected option'),
        ('yellow', 'the highlighted number, key insight or answer'),
        ('grey', 'out of scope, deprioritized, inactive'),
        ('teal', 'data, models and AI system parts (LLM, retriever, eval set, embeddings)'),
        ('pink', 'money: pricing, revenue, cost, margin'),
    ]
    for i, (c, t) in enumerate(items):
        y = 84 + i * 46
        s.box(0, y, 44, 32, None, c, opacity=85)
        s.text(60, y + 5, f'{c}', 18, INK)
        s.text(160, y + 5, t, 17, INK)
    s.save('l0-colour-key')


def d_parts_map():
    s = Scene()
    title(s, 'Parts II to V and their chapters', 'chapters 4 to 25 of Crack the APM Role; page numbers run 1 to 22')
    cols = [
        ('Part II · AI products', 'purple', 'Ch 4-10', [
            'Ch4 AI products differ', 'Ch5 AI tech literacy', 'Ch6 AI strategy, economics',
            'Ch7 Designing AI experiences', 'Ch8 Evaluating AI products',
            'Ch9 Responsible AI, risk', 'Ch10 Launching AI features']),
        ('Part III · toolkit', 'purple', 'Ch 11-20', [
            'Ch11 Understanding users', 'Ch12 Design with CIRCLES', 'Ch13 Improvement, critique',
            'Ch14 Prioritization', 'Ch15 Metrics', 'Ch16 Root cause analysis',
            'Ch17 Pricing, monetization', 'Ch18 Go-to-market, launch',
            'Ch19 Strategy, market entry', 'Ch20 Roadmaps, PRDs, Agile']),
        ('Part IV · estimation', 'purple', 'Ch 21', [
            'Ch21 Guesstimates']),
        ('Part V · case practice', 'purple', 'Ch 22-25', [
            'Ch22 Case types', 'Ch23 Worked examples', 'Ch24 AI case bank', 'Ch25 Practice protocol']),
    ]
    for i, (head, c, rng, items) in enumerate(cols):
        x = i * 250
        s.box(x, 84, 236, 52, f'{head}\n{rng}', c, fs=15, opacity=60)
        for j, it in enumerate(items):
            s.box(x, 150 + j * 30, 236, 26, it, 'purple', fs=14, opacity=25)
    s.text(0, 470, 'Parts II and III build the judgement; Parts IV and V put it to work.', 16, GREY)
    s.save('l0-parts-map')


for f in [d_big_idea, d_colour_key, d_parts_map]:
    f()

# Excalidraw scenes for Chapter 20 (page 17, l17-*). Run: python3 diagrams_l17.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)


# 1 ─ theme-based roadmap: Current, Near term, Future ─────────────────────────────────────────────
def d_roadmap():
    s = Scene()
    title(s, 'Theme-based roadmap: Current, Near term, Future',
          'themes with no fixed dates; each theme ties to an OKR')
    cols = [
        (20, 'CURRENT', 'orange', 60,
         'detailed cards\nideas, customer feedback,\nuser stories being built now'),
        (340, 'NEAR TERM', 'orange', 35,
         'partly detailed cards\nwhat comes next, after\nthe current work'),
        (660, 'FUTURE', 'blue', 30,
         'thin cards that need more\nresearch; they get detailed\nas they move left'),
    ]
    for x, head, c, op, body in cols:
        s.box(x, 96, 280, 44, head, c, fs=18, opacity=60)
        s.box(x, 150, 280, 150, body, c, fs=15, opacity=op)
    s.box(20, 318, 920, 40, 'theme example: "reduce first-order drop-off" (no release date attached)',
          'purple', fs=16, opacity=40)
    s.text(20, 378, 'a release roadmap commits to features and dates: brittle when priorities change',
           15, RED)
    s.box(20, 412, 920, 34, 'the roadmap answers: what are we doing, why, and how does it tie to our OKRs?',
          'yellow', fs=15, opacity=60)
    s.box(20, 458, 920, 30, 'a roadmap that is a release plan in disguise is the common mistake', 'grey', fs=14, opacity=45)
    s.save('l17-roadmap')


# 2 ─ OKRs: one objective, two to four key results ────────────────────────────────────────────────
def d_okr():
    s = Scene()
    title(s, 'OKRs: one objective, measurable key results',
          'the vault example: first-time sellers on a marketplace')
    s.box(160, 96, 640, 60, 'Objective: make first-time sellers successful\n(qualitative and inspiring)',
          'purple', fs=17, opacity=55)
    s.arrow([(360, 156), (260, 200)], color=GREY, sw=2)
    s.arrow([(700, 156), (800, 200)], color=GREY, sw=2)
    s.box(20, 200, 440, 80, 'KR 1: raise first-listing completion\nfrom 40% to 60%', 'green', fs=16, opacity=50)
    s.box(500, 200, 440, 80, 'KR 2: cut median time-to-first-sale\nto 7 days', 'green', fs=16, opacity=50)
    s.box(20, 298, 920, 40, 'formula: "I will [objective] as measured by [key results]"', 'yellow', fs=16, opacity=50)
    s.box(20, 352, 920, 52, 'grading (Google): each KR scored 0.0 to 1.0\n'
          'aspirational: about 0.6-0.7 is success; committed: expect 1.0',
          'blue', fs=14, opacity=35)
    s.box(20, 418, 440, 60, 'outputs are not key results:\n"ship the new home screen" is not one', 'red', fs=14, opacity=40)
    s.box(500, 418, 440, 60, 'keep them few: a team with five\nobjectives has none', 'grey', fs=14, opacity=45)
    s.save('l17-okr')


# 3 ─ the PRD skeleton: ten sections in one story ──────────────────────────────────────────────────
def d_prd_chain():
    s = Scene()
    title(s, 'The PRD: ten sections, one connected story',
          'each section leads to the next; read it from problem to metric')
    row1 = ['1 problem\ndefinition', '2 market research\nand opportunity', '3 user research\nmethods, insights',
            '4 personas and\nuse cases', '5 prioritised\nuse case']
    row2 = ['6 proposed\nsolution', '7 solution\nprioritisation', '8 UX design\nwireframes or\nprototypes',
            '9 roadmap\nphases, milestones', '10 metrics\nNorth Star, AARRR,\nguardrails']
    for i, t in enumerate(row1):
        s.box(34 + i * 180, 100, 172, 80, t, 'purple', fs=14, opacity=50)
    for i, t in enumerate(row2):
        c = 'green' if i == 4 else 'purple'
        s.box(34 + i * 180, 240, 172, 96 if i == 2 or i == 4 else 80, t, c, fs=14, opacity=50)
    s.text(34, 200, 'sections 6-10 continue on the second row (read left to right, top to bottom)', 14, GREY)
    s.box(20, 366, 920, 46, 'the same line runs from the problem to the metric: each link should be checkable',
          'yellow', fs=15, opacity=60)
    s.box(20, 424, 920, 60, 'long research lives in linked documents: a PRD is a living, shared document,\n'
          'not a dump of everything the team knows', 'grey', fs=14, opacity=40)
    s.save('l17-prd-chain')


# 4 ─ user story and acceptance criteria ───────────────────────────────────────────────────────────
def d_user_story():
    s = Scene()
    title(s, 'A user story and its acceptance criteria',
          'the "so that" ties the work to a real need; criteria say done')
    s.box(20, 96, 920, 66, 'As a commuter, I want to save a payment card,\nso that I can pay in one tap next time.',
          'blue', fs=17, opacity=45)
    s.text(20, 176, 'acceptance criteria (Given / When / Then):', 16, PURPLE)
    crit = [
        'Given I have added a card, when I select "Save", then it is in my wallet.',
        'Given the card is saved, when I open checkout, then it is pre-selected.',
        'Given the card is invalid, when I try to save it, then I see an error and nothing is stored.',
    ]
    for i, t in enumerate(crit):
        s.box(20, 204 + i * 50, 920, 42, t, 'teal', fs=14, opacity=40)
    s.text(20, 368, 'INVEST: a good story is', 16, PURPLE)
    chips = ['I independent', 'N negotiable', 'V valuable', 'E estimable', 'S small: fits a sprint', 'T testable']
    for i, t in enumerate(chips):
        s.box(20 + i * 156, 396, 146, 46, t, 'purple', fs=13, opacity=50)
    s.box(20, 458, 920, 30, 'a story without a benefit is a feature request', 'red', fs=15, opacity=40)
    s.save('l17-user-story')


# 5 ─ the Scrum loop ───────────────────────────────────────────────────────────────────────────────
def d_scrum_loop():
    s = Scene()
    title(s, 'The Scrum loop: roles, artifacts, events',
          'Scrum Guide 2020 names: accountabilities, artifacts and commitments')
    arts = [('product backlog', 'commits to a product goal'), ('sprint backlog', 'commits to a sprint goal'),
            ('increment', 'commits to a definition of done')]
    for i, (h, b) in enumerate(arts):
        s.box(20 + i * 310, 96, 290, 62, h + '\n' + b, 'purple', fs=15, opacity=50)
    events = [('Sprint planning', 'up to 8 h for a 1-month sprint'),
              ('Daily Scrum', '15 minutes, for the developers'),
              ('Sprint review', 'inspect with stakeholders'),
              ('Retrospective', 'improve how the team works')]
    for i, (h, b) in enumerate(events):
        x = 20 + i * 232
        s.box(x, 200, 210, 80, h + '\n' + b, 'orange', fs=14, opacity=50)
        if i < 3:
            s.arrow([(x + 212, 240), (x + 230, 240)], color=ORANGE, sw=2)
    s.arrow([(806, 282), (806, 310), (125, 310), (125, 282)], color=GREY, sw=2)
    s.text(330, 316, 'the next sprint starts again', 14, GREY)
    roles = [('Product Owner', 'orders the backlog, often the PM'),
             ('Scrum Master', 'coaches the team, removes blockers'),
             ('Developers', 'build the increment')]
    for i, (h, b) in enumerate(roles):
        s.box(20 + i * 310, 346, 290, 66, h + '\n' + b, 'blue', fs=15, opacity=45)
    s.box(20, 424, 920, 40, 'sprint: one month or less, commonly 2 weeks; it contains all other events',
          'yellow', fs=15, opacity=55)
    s.box(20, 472, 920, 22, 'a Scrum master is not a project manager', 'grey', fs=13, opacity=40)
    s.save('l17-scrum-loop')


# 6 ─ AI PRD additions ─────────────────────────────────────────────────────────────────────────────
def d_ai_prd():
    s = Scene()
    title(s, 'AI PRD additions: five sections a normal PRD skips',
          'a standard PRD assumes the same input gives the same output')
    s.box(340, 210, 280, 80, 'standard PRD\nproblem to metric', 'purple', fs=18)
    s.box(300, 96, 360, 74, '1 eval criteria: the quality bar\nrubric, thresholds, golden set, judge',
          'teal', fs=15, opacity=45)
    s.box(20, 190, 260, 100, '2 failure modes\nhallucination, wrong tool call,\nrefusal, leakage, unsafe content',
          'teal', fs=13, opacity=45)
    s.box(680, 190, 260, 100, '3 data requirements\ntraining, retrieval corpus,\nuser context, consent, labels',
          'teal', fs=13, opacity=45)
    s.box(60, 350, 390, 74, '4 performance and cost budgets\nlatency target, cost per task, margin',
          'teal', fs=14, opacity=45)
    s.box(510, 350, 390, 74, '5 launch and monitoring\nrollout stages, kill switch, drift checks',
          'teal', fs=14, opacity=45)
    s.arrow([(480, 170), (480, 208)], color=GREY, sw=2)
    s.arrow([(280, 240), (338, 240)], color=GREY, sw=2)
    s.arrow([(680, 240), (622, 240)], color=GREY, sw=2)
    s.arrow([(255, 350), (400, 292)], color=GREY, sw=2)
    s.arrow([(705, 350), (560, 292)], color=GREY, sw=2)
    s.box(20, 446, 920, 36, 'interview tip: name the failure mode you worry about most, then show the PRD change',
          'yellow', fs=15, opacity=60)
    s.save('l17-ai-prd')


# 7 ─ chapter 20 on one page ───────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 20 on one page: plan, document, run, judge',
          'from the roadmap down to the AI PRD')
    cols = [
        ('20.1 Roadmap, OKR', 'a theme-based roadmap\nwith measurable goals', 'what are we doing, and why?', 'orange'),
        ('20.2 PRD', 'ten sections that\nfollow one story', 'can a reader trace problem to metric?', 'purple'),
        ('20.3 Stories', 'who, what and why,\nthen testable criteria', 'can QA test every line?', 'blue'),
        ('20.4 Agile, Scrum', 'roles, artifacts and\nevents of the loop', 'who orders the backlog?', 'orange'),
        ('20.5 AI PRD', 'eval, failure modes,\ndata, cost and launch', 'how do we judge a range?', 'teal'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 192
        s.box(x, 84, 182, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 182, 110, core, c, fs=15, opacity=45)
        s.box(x, 280, 182, 92, q, 'yellow', fs=15, opacity=60)
    s.box(10, 392, 940, 58, 'execution = plan, document, run the work, and judge AI quality', 'purple', fs=17, opacity=35)
    s.box(10, 462, 940, 36, 'Agile does not drop the PRD: the document and the criteria still exist',
          'green', fs=15, opacity=45)
    s.save('l17-big-picture')


for f in [d_roadmap, d_okr, d_prd_chain, d_user_story, d_scrum_loop, d_ai_prd, d_big_picture]:
    f()

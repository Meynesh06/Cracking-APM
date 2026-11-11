# Excalidraw scenes for Chapter 6 (page 3, l3-*). Run: python3 diagrams_l3.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


# 1 ─ build, host or call an API ─────────────────────────────────────────────────────────────────────
def d_build_buy_api():
    s = Scene()
    title(s, 'Build, host or call an API: start with the API',
          'move down the stack only when cost, control or data demand it')
    heads = ['build: train your own', 'host an open-weight model', 'API access']
    what = ['pretrain or heavily train a model',
            'fine-tune and run an open-weight\nmodel on your own infra or cloud',
            'call a hosted model, directly or\nvia Azure, AWS or Google Cloud']
    pros = ['full control and a possible moat',
            'lower marginal cost at steady volume;\ndata stays in your VPC; no surprise\ndeprecations',
            'fastest; best-in-class quality;\nno infra; prices tend to fall']
    cons = ['very expensive; needs scarce talent\nand data',
            'you own serving, scaling, evals,\nupgrades; behind the frontier on\nthe hardest tasks',
            'vendor model changes, deprecations;\ndata-handling terms, rate limits,\nless control']
    for i, x in enumerate((0, 330, 660)):
        s.box(x, 84, 300, 44, heads[i], 'purple', fs=18)
        s.box(x, 138, 300, 58, what[i], 'teal', fs=14, opacity=50)
        s.box(x, 204, 300, 78, pros[i], 'green', fs=14, opacity=40)
        s.box(x, 290, 300, 78, cons[i], 'red', fs=14, opacity=35)
    s.text(0, 384, 'decision factors', 18, PURPLE)
    factors = ['differentiation', 'data sensitivity', 'volume and unit cost', 'quality bar', 'team capability']
    for i, t in enumerate(factors):
        s.box(i * 195, 412, 180, 40, t, 'teal', fs=14, opacity=40)
    s.box(0, 470, 960, 56, 'prototype on an API, measure with evals, then route\n'
          'narrow, high-volume tasks to a smaller or open model', 'yellow', fs=15, opacity=60)
    s.save('l3-build-buy-api')


# 2 ─ cost per successful task: the chain of the vault's worked example ──────────────────────────────
def d_cost_per_task():
    s = Scene()
    title(s, 'Cost per successful task: the vault worked example',
          'illustrative prices; the chain multiplies, then divides')
    s.box(0, 110, 250, 100, 'cost per call  = $0.0046\n3,000 in x $1/M = $0.0030\n400 out x $4/M = $0.0016',
          'pink', fs=13, ff=3, opacity=35)
    s.box(290, 110, 220, 100, 'x 1.3 calls per task\nretries and a safety check', 'orange', fs=14, opacity=50)
    s.box(550, 110, 210, 100, '/ 0.80 success rate\nfailed tries still cost money', 'orange', fs=14, opacity=50)
    s.box(800, 110, 160, 100, '$0.0075\nper successful\ntask', 'yellow', fs=16, opacity=70)
    for x1, x2 in ((250, 290), (510, 550), (760, 800)):
        s.arrow([(x1 + 2, 160), (x2 - 2, 160)], color=ORANGE, sw=3)
    s.text(0, 236, 'where the cost hides', 18, PURPLE)
    hidden = ['longer context:\nmore input tokens', 'reasoning and agents:\nmore calls per task',
              'output length:\npriced higher', 'retries and fallbacks:\nhidden cost']
    for i, t in enumerate(hidden):
        s.box(i * 245, 262, 225, 62, t, 'red', fs=14, opacity=35)
    s.box(0, 342, 960, 56, 'the vault rounds the per-call cost to $0.005 first: ~$0.008\n'
          'unrounded, the arithmetic gives $0.0075: keep full precision', 'grey', fs=15, opacity=50)
    s.box(0, 416, 960, 64, 'cost per paying user = tasks per month x cost per task\n'
          'gross margin = (revenue - cost to serve) / revenue', 'purple', fs=15, ff=3, opacity=30)
    s.save('l3-cost-per-task')


# 3 ─ gross margin under changes: the sensitivity table as bars ─────────────────────────────────────
def d_margin_sensitivity():
    s = Scene()
    title(s, 'Gross margin on one Rs 499 plan: five illustrative cases',
          'Rs 4 per summary, 30 summaries a month, unless stated')
    rows = [('base case', 'COGS: Rs 4 x 30 = Rs 120', 'pink', 0.76, '76%'),
            ('tokens per task x2', 'COGS: Rs 8 x 30 = Rs 240', 'orange', 0.52, '52%'),
            ('price per token -50%', 'COGS: Rs 2 x 30 = Rs 60', 'green', 0.88, '88%'),
            ('adoption x2', 'COGS: Rs 4 x 60 = Rs 240', 'orange', 0.52, '52%'),
            ('power user, 120 summaries', 'COGS: Rs 4 x 120 = Rs 480', 'red', 0.04, '4%')]
    for i, (lab, sub, c, m, txt) in enumerate(rows):
        y = 110 + i * 66
        s.text(0, y + 2, lab, 16, INK)
        s.text(0, y + 24, sub, 14, GREY, ff=3)
        w = m * 560
        s.box(330, y, w, 40, None, c, opacity=70)
        s.text(330 + w + 10, y + 8, txt, 18, INK, ff=3)
    s.box(0, 438, 960, 40, 'the margin moves most with usage, not with the average user',
          'yellow', fs=15, opacity=60)
    s.text(0, 486, 'check the 95th-percentile user, not the average', 16, PURPLE)
    s.save('l3-margin-sensitivity')


# 4 ─ six pricing models ─────────────────────────────────────────────────────────────────────────────
def d_pricing_models():
    s = Scene()
    title(s, 'Six ways to charge for AI, each tied to cost or value',
          'price on the metric that moves with value and with cost')
    cards = [
        ('per seat\ncharges: users per month\ngood when: value tracks headcount\n'
         'risk: heavy users cost more than\nthe seat price; light users underpay'),
        ('usage-based\ncharges: tokens, requests,\ndocuments, minutes\n'
         'good when: cost tracks usage closely\nrisk: hard to budget; churn when\nbills spike'),
        ('outcome-based\ncharges: a successful task or\nresolution\n'
         'good when: the outcome is measurable\nrisk: needs trustworthy attribution;\nrevenue volatile'),
        ('credits\ncharges: prepaid credits spent on\ndifferent AI actions\n'
         'good when: many features with\ndifferent costs\nrisk: opaque to buyers;\ncredit inflation'),
        ('bundled\ncharges: included in a higher plan\nor suite\n'
         'good when: drives upgrades; raises\nperceived value\nrisk: hides AI cost; hard to\nprice-discriminate'),
        ('hybrid\ncharges: seat fee + usage credits\n'
         'good when: most enterprise AI deals\nrisk: more complex to explain'),
    ]
    for i, t in enumerate(cards):
        x = (i % 3) * 330
        y = 84 + (i // 3) * 198
        s.box(x, y, 300, 180, t, 'pink', fs=14, opacity=30)
    s.box(0, 480, 960, 56, 'price on the metric closest to value and cost\n'
          'include a usage allowance; charge overage above it', 'yellow', fs=15, opacity=60)
    s.save('l3-pricing-models')


# 5 ─ defensibility: a wrapper is not a moat ───────────────────────────────────────────────────────────
def d_moats():
    s = Scene()
    title(s, 'Defensibility: a wrapper around a model is not a moat',
          'what a customer would miss if the vendor vanished')
    s.box(0, 84, 300, 120, 'model quality is commoditising:\ncapability becomes cheap and common\n'
          'so a wrapper is not a moat', 'red', fs=14, opacity=30)
    s.box(0, 222, 300, 128, 'test: remove the model vendor.\nWhat is left that a customer would\n'
          'miss? If only the prompt, the moat\nis weak.', 'yellow', fs=14, opacity=50)
    moats = [
        (330, 84, 'proprietary data\nunique, consented, labelled data\nused to improve outcomes', 'teal'),
        (660, 84, 'distribution\nan existing user base or channel\n(messaging app, checkout)', 'blue'),
        (330, 186, 'workflow integration\nsits in the system of record\nremoving it breaks daily work', 'orange'),
        (660, 186, 'switching costs\ndata gravity, retrained teams,\nintegrations and contracts', 'purple'),
        (330, 288, 'trust and brand\nslow to copy in regulated or\nhigh-stakes domains', 'green'),
        (660, 288, 'cost position\na lower cost per task lets you\nprice below rivals and earn margin', 'pink'),
    ]
    for x, y, t, c in moats:
        s.box(x, y, 300, 92, t, c, fs=14, opacity=40)
    s.box(0, 400, 960, 40, 'Bloomberg: data and the Terminal workflow, not the model',
          'purple', fs=15, opacity=30)
    s.box(0, 448, 960, 40, 'distribution slows rivals; it does not stop a better workflow',
          'grey', fs=15, opacity=50)
    s.save('l3-moats')


# 6 ─ the autonomy spectrum: copilot, automation, agent ──────────────────────────────────────────────
def d_autonomy():
    s = Scene()
    title(s, 'Copilot, automation, agent: one dial, three postures',
          'more AI action alone: more value, more risk, more evals')
    s.text(40, 66, 'autonomy rises from left to right', 15, GREY)
    s.arrow([(40, 100), (930, 100)], color=ORANGE, sw=3)
    stations = [
        (40, 'green', 'copilot (assistive)\nwho: a human; AI suggests\nexample: drafts, code completion,\n'
                      'suggested replies\nrisk: low; the human checks'),
        (340, 'orange', 'automation (rules + AI)\nwho: AI runs one bounded step\n'
                        'example: auto-tags and routes\ntickets and claims\nrisk: medium; errors repeat\nat scale, '
                        'easy to reverse'),
        (640, 'red', 'autonomous agent\nwho: AI plans and executes steps\n'
                     'example: books, files, resolves\nend to end, with tools\n'
                     'risk: high; wrong actions have\nreal consequences'),
    ]
    for x, c, t in stations:
        s.box(x, 118, 280, 196, t, c, fs=14, opacity=40)
    s.text(0, 326, 'decision rule: start at the lowest autonomy that works', 17, PURPLE)
    s.box(0, 354, 960, 36, 'earn the right: log accept and edit rates, widen scope', 'green', fs=15, opacity=40)
    s.box(0, 398, 960, 36, 'approval gates on every irreversible step (payments, emails)', 'yellow', fs=15, opacity=60)
    s.box(0, 442, 960, 36, 'analogy: Waymo runs driverless robotaxis in limited areas', 'teal', fs=15, opacity=40)
    s.box(0, 486, 960, 36, 'moving right: from acceptance and edit rate to task success', 'grey', fs=15, opacity=50)
    s.save('l3-autonomy-spectrum')


# 7 ─ big picture cheat sheet ───────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 6 on one page: price and design against cost',
          'model cost is a variable cost of goods sold, from day one')
    cols = [
        ('6.1 build, buy or API',
         'start with an API to learn\nmove down the stack only if\ncost, control or data push\nroute narrow, high-volume\ntasks to a smaller model',
         'would you build, host or\ncall an API? why?', 'teal'),
        ('6.2 unit economics',
         'cost per successful task,\nnot cost per call\ntokens x calls + retries\ngross margin: revenue minus\ncost to serve\ntest tokens, price and use',
         'is it profitable at the\n95th-percentile user?', 'pink'),
        ('6.3-6.4 pricing and moats',
         'six pricing models; a mix\nis common\nprice on value and cost\nmoats: data, distribution,\nworkflow, switching costs',
         'what does the user pay for,\nand what can rivals copy?', 'pink'),
        ('6.5 autonomy',
         'copilot: a human decides\nautomation: bounded steps\nagent: plans and acts\nmore autonomy, more risk\nearn the right; gate the\nirreversible steps',
         'what does an error cost,\nand who approves the action?', 'orange'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 240
        s.box(x, 84, 230, 56, head, 'purple', fs=15, opacity=60)
        s.box(x, 150, 230, 186, core, c, fs=14, opacity=40)
        s.box(x, 346, 230, 60, q, 'yellow', fs=14, opacity=60)
    s.box(10, 420, 940, 40, 'good outcome: a margin that holds at peak usage, with a moat',
          'green', fs=15, opacity=40)
    s.box(10, 470, 940, 36, 'the question for every AI feature: what does one task cost?',
          'purple', fs=15, opacity=30)
    s.save('l3-big-picture')


for f in [d_build_buy_api, d_cost_per_task, d_margin_sensitivity, d_pricing_models,
          d_moats, d_autonomy, d_big_picture]:
    f()

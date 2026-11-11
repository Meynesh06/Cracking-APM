# Excalidraw scenes for Chapter 15 (page 12, l12-*). Run: python3 diagrams_l12.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)


# 1 ─ North Star with input and guardrail metrics ─────────────────────────────────────────────────
def d_north_star():
    s = Scene()
    title(s, 'North Star: one value metric, inputs below, guardrails beside',
          'food delivery: orders delivered on time and as ordered, per week')
    s.text(0, 84, 'rejected candidates', 17, INK)
    s.box(0, 112, 230, 62, 'revenue: lags the value, company-centric', 'grey', fs=14, opacity=50)
    s.box(0, 186, 230, 62, 'orders placed: counts late or wrong orders', 'grey', fs=14, opacity=50)
    s.box(260, 100, 660, 70, 'orders delivered on time and as ordered per week',
          'green', fs=20, opacity=55)
    s.text(260, 84, 'the North Star (value to the customer)', 16, GREEN)
    for x, lab in ((260, 'active restaurants\nper locality'),
                   (480, 'delivery partner\navailability at peak'),
                   (700, 'search-to-order\nconversion')):
        s.arrow([(x + 100, 172), (x + 100, 206)], color=GREY, sw=2)
        s.box(x, 208, 200, 70, lab, 'orange', fs=16, opacity=55)
    s.text(260, 292, 'input metrics: what teams own', 15, ORANGE)
    s.text(260, 318, 'guardrails: must not get worse', 15, RED)
    s.box(260, 344, 320, 56, 'cancellation rate', 'red', fs=17, opacity=40)
    s.box(600, 344, 320, 56, 'delivery partner earnings per hour', 'red', fs=16, opacity=40)
    s.box(0, 420, 920, 44, 'value delivered to customers, not revenue or a vanity count',
          'yellow', fs=17, opacity=65)
    s.save('l12-north-star')


# 2 ─ AARRR as five stages with a metric each ─────────────────────────────────────────────────────
def d_aarrr():
    s = Scene()
    title(s, 'AARRR: five stages, one metric that gates each',
          'UPI payments app mini-example from the vault')
    stages = [
        ('Acquisition', 'how are people\ndiscovering us?', 'installs by channel'),
        ('Activation', 'do they do the\naction that shows value?', 'first successful\npayment within 7 days'),
        ('Retention', 'do activated users\ncome back?', 'monthly transacting\nusers'),
        ('Referral', 'do users recommend\nus?', 'invites that lead to\na first payment'),
        ('Revenue', 'will users pay?', 'merchant fees, lending\nand insurance cross-sell'),
    ]
    for i, (name, q, metric) in enumerate(stages):
        x = i * 188
        s.box(x, 100, 170, 56, name, 'orange', fs=18, opacity=60)
        if i < 4:
            s.arrow([(x + 172, 128), (x + 186, 128)], color=GREY, sw=2)
        s.text(x + 4, 172, q, 14, INK)
        s.text(x + 4, 226, 'metric:', 14, GREY, ff=3)
        s.box(x, 248, 170, 96, metric, 'teal', fs=14, opacity=50)
    s.box(0, 372, 920, 44, 'if cashback installs activate but do not retain,', 'yellow', fs=17, opacity=60)
    s.text(0, 424, 'the problem is the offer attracting deal-seekers, not the funnel', 16, INK)
    s.text(0, 452, 'AARRR assumes a funnel-shaped journey: pair it with network metrics', 15, GREY)
    s.text(0, 474, 'when value is collaborative (see the funnel and marketplace page)', 15, GREY)
    s.save('l12-aarrr')


# 3 ─ HEART with Goals, Signals and Metrics ───────────────────────────────────────────────────────
def d_heart():
    s = Scene()
    title(s, 'HEART: five dimensions, each with a goal, signal and metric',
          'Goals-Signals-Metrics: keep three or four dimensions')
    for x, lab in ((0, 'dimension'), (180, 'goal'), (430, 'signal'), (680, 'metric')):
        s.text(x + 6, 88, lab, 15, GREY)
    rows = [
        ('Happiness', 'users find it pleasant', 'positive survey responses', 'CSAT, NPS'),
        ('Engagement', 'users use it often', 'actions per session', 'sessions per user per week'),
        ('Adoption', 'new users start using it', 'first-time use of feature', '% of new users who try it'),
        ('Retention', 'users keep returning', 'repeat usage', 'churn rate, D30 retention'),
        ('Task success', 'users complete the job', 'completion without errors',
         'completion rate, time-on-task,\nerror rate'),
    ]
    for i, (dim, goal, sig, met) in enumerate(rows):
        y = 112 + i * 60
        s.box(0, y, 166, 50, dim, 'purple', fs=16, opacity=55)
        s.box(180, y, 236, 50, goal, 'blue', fs=14, opacity=40)
        s.box(430, y, 236, 50, sig, 'orange', fs=14, opacity=40)
        s.box(680, y, 240, 50, met, 'teal', fs=14, opacity=40)
    s.box(0, 430, 920, 40, 'mini-example: WhatsApp disappearing messages skip Retention',
          'yellow', fs=17, opacity=60)
    s.text(0, 478, 'Task success is the most diagnostic: if it is low, fix the flow first', 15, GREY)
    s.save('l12-heart')


# 4 ─ marketplace: supply, match, demand ──────────────────────────────────────────────────────────
def d_marketplace():
    s = Scene()
    title(s, 'Marketplace metrics: supply, demand, and the match between them',
          'watch the balance: too much demand starves supply, and the reverse')
    s.box(0, 110, 260, 176, None, 'blue', opacity=35)
    s.text(14, 122, 'supply side', 18, INK)
    s.text(14, 154, 'active suppliers', 15, INK)
    s.text(14, 178, '(drivers, sellers, hosts)', 14, GREY)
    s.text(14, 210, 'supply utilisation', 15, INK)
    s.text(14, 240, 'earnings per supplier', 15, INK)
    s.box(330, 110, 300, 176, None, 'teal', opacity=40)
    s.text(344, 122, 'match / liquidity', 18, INK)
    s.text(344, 160, 'fill rate', 16, INK)
    s.text(344, 190, 'time-to-match', 16, INK)
    s.text(344, 220, 'search-to-booking rate', 16, INK)
    s.box(660, 110, 260, 176, None, 'blue', opacity=35)
    s.text(674, 122, 'demand side', 18, INK)
    s.text(674, 154, 'active buyers', 15, INK)
    s.text(674, 184, 'orders per buyer', 15, INK)
    s.text(674, 214, 'repeat rate', 15, INK)
    s.arrow([(262, 198), (328, 198)], color=GREY, sw=2, start='arrow')
    s.arrow([(632, 198), (658, 198)], color=GREY, sw=2, start='arrow')
    s.box(0, 316, 920, 52, 'economics: GMV, take rate (platform revenue / GMV), contribution margin per order',
          'pink', fs=16, opacity=40)
    s.text(0, 388, 'the reverse: too much supply starves suppliers of work', 16, RED)
    s.text(0, 414, 'too much demand: waits rise and buyers churn', 16, RED)
    s.text(0, 448, 'Uber / Ola: driver utilisation and rider wait time (ETA) are the balance pair;', 15, INK)
    s.text(0, 472, 'surge pricing pulls supply in when demand outruns it', 15, INK)
    s.save('l12-marketplace')


# 5 ─ funnel bars from the run-block numbers ──────────────────────────────────────────────────────
def d_funnel():
    s = Scene()
    title(s, 'Funnel: find the biggest leak first',
          'illustrative numbers from the run block, 100,000 visits to start')
    steps = [
        ('visit', 100000, '100.0% of visits', 'blue'),
        ('sign-up', 12000, '12.0% of visits; 12.0% step conversion', 'red'),
        ('first order', 5400, '45.0% of sign-ups', 'blue'),
        ('second order', 2160, '40.0% of first orders', 'blue'),
    ]
    k = 600 / 100000
    for i, (name, n, note, c) in enumerate(steps):
        y = 120 + i * 74
        s.text(0, y + 10, name, 17, INK)
        w = max(8, n * k)
        s.box(150, y, w, 42, None, c, opacity=65)
        s.text(150 + w + 12, y + 10, f'{n:,}', 17, INK, ff=3)
        s.text(150, y + 48, note, 14, GREY, ff=3)
    s.box(0, 430, 920, 40, 'the biggest drop between two steps is the first place to look',
          'yellow', fs=17, opacity=60)
    s.text(0, 480, 'segment by source, device and cohort before deciding the cause', 15, GREY)
    s.save('l12-funnel')


# 6 ─ primary metric vs guardrail ─────────────────────────────────────────────────────────────────
def d_guardrail():
    s = Scene()
    title(s, 'Guardrails: the primary metric may rise, the guardrail must hold',
          'the vault example: conversion up 4%, cancellations up 3%')
    X = 380
    s.line([(X, 110), (X, 330)], color=INK, sw=2)
    s.text(X - 60, 340, '0', 14, GREY, ff=3)
    s.text(0, 150, 'primary: what you optimise', 16, GREEN)
    s.box(X, 130, 240, 56, 'conversion +4%', 'green', fs=18, opacity=60)
    s.text(0, 262, 'guardrail: what you must not break', 16, RED)
    s.box(X, 242, 180, 56, 'cancellations +3%', 'red', fs=18, opacity=50)
    s.text(X, 306, 'a bigger number on the primary does not clear the guardrail', 15, GREY)
    types = [('experience', ['complaints, crash rate,', 'latency'], 'teal'),
             ('business', ['refund rate, cancellations,', 'margin'], 'blue'),
             ('trust and safety', ['harmful content, fraud,', 'opt-outs'], 'purple'),
             ('negative', ['errors, churn,', 'rage clicks'], 'orange')]
    for i, (h, body, c) in enumerate(types):
        x = i * 232
        s.box(x, 370, 220, 84, None, c, opacity=35)
        s.text(x + 10, 378, h, 16, INK)
        for j, line in enumerate(body):
            s.text(x + 10, 404 + j * 18, line, 13, INK, ff=3)
    s.box(0, 462, 920, 40, 'compare net revenue after cancellations, not gross conversion',
          'yellow', fs=17, opacity=60)
    s.save('l12-guardrail')


# 7 ─ metric tree: revenue fell 10 percent ────────────────────────────────────────────────────────
def d_metric_tree():
    s = Scene()
    title(s, 'Metric tree: revenue fell 10%, orders flat, so AOV fell',
          'walk the branches; grey branches did not move')
    s.text(0, 84, 'diagnosing a drop', 17, PURPLE)
    steps = ['1 verify the metric is real', '2 quantify: size, speed, window',
             '3 segment: geo, platform, cohort', '4 walk the tree to the moved branch',
             '5 map to causes: internal or external', '6 test the cheapest hypothesis']
    for i, t in enumerate(steps):
        s.text(0, 116 + i * 30, t, 15, INK)
    s.box(400, 100, 220, 50, 'revenue: -10%', 'red', fs=18, opacity=50)
    s.arrow([(510, 150), (470, 196)], color=GREY, sw=2)
    s.arrow([(510, 150), (720, 196)], color=GREY, sw=2)
    s.box(380, 198, 180, 50, 'orders: flat', 'grey', fs=17, opacity=50)
    s.box(600, 198, 240, 50, 'average order value: -10%', 'red', fs=16, opacity=50)
    s.arrow([(700, 248), (650, 296)], color=GREY, sw=2)
    s.arrow([(720, 248), (820, 296)], color=GREY, sw=2)
    s.box(560, 298, 180, 50, 'items per order: flat', 'grey', fs=15, opacity=50)
    s.box(760, 298, 160, 50, 'price per item: fell', 'red', fs=15, opacity=50)
    s.arrow([(840, 348), (840, 394)], color=GREY, sw=2)
    s.box(740, 396, 200, 60, 'grocery share of orders\njumped after a promo', 'yellow', fs=14, opacity=60)
    s.text(380, 470, 'a mix shift to cheaper baskets: not a product bug', 15, INK)
    s.save('l12-metric-tree')


# 8 ─ big picture cheat sheet ─────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 15 on one page: six lenses, one question each',
          'every metric answer names a primary, a reason and a guardrail')
    cards = [
        ('North Star', 'value delivered\nto customers', 'is the value real\nand over time?'),
        ('AARRR', 'five lifecycle\nstages, one metric each', 'where do users\nleak?'),
        ('HEART', 'goal, signal and\nmetric per dimension', 'is the experience\ngood?'),
        ('Funnel, marketplace,\nretention', 'steps, two sides,\ncohort curves', 'where, and does\nvalue stick?'),
        ('Guardrails', 'experience, business,\ntrust, negative', 'what must not\nbreak?'),
        ('Metric trees', 'split a number into\ndrivers; walk them', 'which branch\nmoved?'),
    ]
    for i, (head, body, foot) in enumerate(cards):
        x = 10 + i * 152
        s.box(x, 90, 146, 62, head, 'purple', fs=14, opacity=60)
        s.box(x, 162, 146, 118, body, 'teal', fs=13, opacity=40)
        s.box(x, 290, 146, 84, foot, 'yellow', fs=13, opacity=55)
    s.box(10, 400, 940, 56, 'name the primary metric, its reason, and at least one guardrail',
          'green', fs=16, opacity=40)
    s.text(10, 470, 'diagnose a drop: verify, quantify, segment, walk the tree, test', 15, GREY)
    s.save('l12-big-picture')


for f in [d_north_star, d_aarrr, d_heart, d_marketplace, d_funnel, d_guardrail,
          d_metric_tree, d_big_picture]:
    f()

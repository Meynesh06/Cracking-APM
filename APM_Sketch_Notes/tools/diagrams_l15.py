# Excalidraw scenes for Chapter 18 (page 15, l15-*). Run: python3 diagrams_l15.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'
PINK = '#9c36b5'


def mono_lines(s, x, y, items, fs=14, gap=20, color=INK):
    for i, t in enumerate(items):
        s.text(x, y + i * gap, t, fs, color, ff=3)


# 1 ─ launch timeline ─────────────────────────────────────────────────────────────────────────────────
def d_launch_timeline():
    s = Scene()
    title(s, 'Launch as a sequence: pre-launch, launch, post-launch',
          'the six GTM stages are spread across the three phases')
    phases = [
        (10, 'pre-launch', [
            'define the ICP', 'research competitors', 'develop messaging',
            'set funnel targets', 'support, docs, pricing', 'launch criteria + rollback']),
        (330, 'launch', [
            'release: pilot, region or all', 'run the channel tactics',
            'watch errors, latency, conversion', 'war room or on-call rota']),
        (650, 'post-launch', [
            'feedback loop across teams', 'triage bugs and adoption gaps',
            'iterate (Spotify: Tweak It)', 'review at fixed checkpoints']),
    ]
    for x, head, steps in phases:
        s.box(x, 92, 300, 44, head, 'purple', fs=19, opacity=60)
        for j, t in enumerate(steps):
            s.box(x, 152 + j * 44, 300, 36, t, 'orange', fs=15, opacity=55)
    s.arrow([(312, 114), (326, 114)], color=GREY, sw=3)
    s.arrow([(632, 114), (646, 114)], color=GREY, sw=3)
    s.line([(10, 430), (950, 430)], sw=3)
    for x, lab in [(160, 'week 1'), (480, 'week 4'), (800, 'quarter end')]:
        s.line([(x, 422), (x, 438)], color=INK, sw=2)
        s.text(x - 30, 446, lab, 16, PURPLE, ff=3)
    s.text(10, 476, 'checkpoints: review metrics against the targets set before launch', 16, GREY, ff=3)
    s.save('l15-launch-timeline')


# 2 ─ product-led vs sales-led ────────────────────────────────────────────────────────────────────────
def d_led_compare():
    s = Scene()
    title(s, 'Product-led vs sales-led: who moves the user forward?',
          'the buyer discovers and pays differently, so the GTM differs')
    s.text(10, 90, 'product-led: the product sells itself (Calendly, Slack)', 19, PURPLE)
    flow_p = ['find it', 'try the free tier', 'invite the team', 'upgrade to paid seats']
    for i, t in enumerate(flow_p):
        x = 10 + i * 236
        s.box(x, 128, 210, 60, t, 'blue' if i in (0, 3) else 'orange', fs=16, opacity=55)
        if i < 3:
            s.arrow([(x + 212, 158), (x + 234, 158)], color=GREY, sw=3)
    s.text(10, 200, 'no sales call needed; the user is the buyer or the champion', 15, GREY, ff=3)
    s.line([(10, 236), (950, 236)], color=GREY, sw=1)
    s.text(10, 256, 'sales-led: marketing makes leads, salespeople convert them', 19, PURPLE)
    flow_s = ['marketing makes a lead', 'sales talks to the lead', 'demo and proposal', 'contract and paid seats']
    for i, t in enumerate(flow_s):
        x = 10 + i * 236
        s.box(x, 294, 210, 60, t, 'blue' if i in (0, 3) else 'orange', fs=16, opacity=55)
        if i < 3:
            s.arrow([(x + 212, 324), (x + 234, 324)], color=GREY, sw=3)
    s.text(10, 366, 'slower and costlier per customer, good for high-value deals', 15, GREY, ff=3)
    s.box(10, 412, 940, 52, 'choose by how the buyer discovers and pays for the product',
          'yellow', fs=17, opacity=45)
    s.save('l15-led-compare')


# 3 ─ phased rollout ladder ───────────────────────────────────────────────────────────────────────────
def d_rollout_ladder():
    s = Scene()
    title(s, 'Phased rollout: widen only when the gate passes',
          'MVP and pilot first; each widening step has its own gate and a kill switch')
    steps = ['MVP', 'pilot', '1%', '10%', '50%', '100%']
    for i, t in enumerate(steps):
        x = 40 + i * 148
        col = 'teal' if i == 0 else ('orange' if i == 1 else 'green')
        s.box(x, 110, 120, 60, t, col, fs=19, opacity=55)
        if i < len(steps) - 1:
            s.arrow([(x + 122, 140), (x + 146, 140)], color=GREY, sw=3)
    gates = [('learn, not', 'complete'), ('time-bound,', 'clear success'), ('gate: error', 'rate'),
             ('gate: task', 'success'), ('gate: ', 'retention'), ('gate: support', 'load')]
    for i, (l1, l2) in enumerate(gates):
        s.text(40 + i * 148, 180, l1, 13, GREY, ff=3)
        s.text(40 + i * 148, 198, l2, 13, GREY, ff=3)
    s.text(40, 230, 'define every gate before the rollout starts', 17, PURPLE)
    s.box(40, 270, 880, 56, 'kill switch: roll back without a new release', 'red', fs=17, opacity=45)
    s.text(40, 352, 'early adopters or a well-instrumented region go first', 16, INK)
    s.text(40, 378, 'slower widening costs time, but a bad launch costs more', 16, INK)
    s.text(40, 404, 'problems that show up only at scale are costly to fix', 16, INK)
    s.save('l15-rollout-ladder')


# 4 ─ distribution channels ───────────────────────────────────────────────────────────────────────────
def d_channels():
    s = Scene()
    title(s, 'Distribution channels: reach against cost and control',
          'pick the channel the ICP already uses; check its cost against lifetime value')
    tiles = [
        ('organic / product-led', 'green', 'low cost, word of mouth', 'slow to scale'),
        ('paid acquisition', 'pink', 'fast and measurable', 'expensive: CAC can exceed LTV'),
        ('sales-led', 'orange', 'good for high-value B2B', 'slow, expensive per customer'),
        ('partners / integrations', 'blue', 'access to an existing base', 'revenue share, dependency'),
        ('bundles, telco, OEM', 'blue', 'reach at scale, new markets', 'thin margins, long talks'),
        ('marketplaces, app stores', 'pink', 'built-in discovery', 'platform fees, policy risk'),
    ]
    for i, (name, col, strength, cost) in enumerate(tiles):
        x = 20 + (i % 3) * 312
        y = 100 + (i // 3) * 150
        s.box(x, y, 300, 130, None, col, opacity=40)
        s.text(x + 12, y + 10, name, 17, INK)
        s.text(x + 12, y + 46, 'strength: ' + strength, 13, INK, ff=3)
        s.text(x + 12, y + 74, 'cost: ' + cost, 13, PINK if col == 'pink' else INK, ff=3)
    s.text(40, 418, 'questions: where does the ICP spend time?', 16, INK)
    s.text(40, 442, 'what is CAC against LTV? who owns the customer?', 16, INK)
    s.text(40, 466, 'can we measure this channel well enough to judge it?', 16, INK)
    s.save('l15-channels')


# 5 ─ launch success criteria ─────────────────────────────────────────────────────────────────────────
def d_success_criteria():
    s = Scene()
    title(s, 'Launch success criteria: four parts, written before launch',
          'example: in-app savings goal (target 8%, stop below 3%)')
    cards = [
        ('1 primary metric', 'green', ['one number that shows', 'the problem is solved', 'e.g. activation rate']),
        ('2 target, threshold', 'yellow', ['the success level', 'the stop or rethink level', 'e.g. target 8%, stop <3%']),
        ('3 guardrails', 'red', ['must not get worse', 'crash rate, latency', 'support, churn, cost']),
        ('4 time window', 'blue', ['when you check it', 'week 1: health', 'day 30 and day 90']),
    ]
    for i, (head, col, lines) in enumerate(cards):
        x = 20 + i * 236
        s.box(x, 96, 225, 230, None, col, opacity=35)
        s.text(x + 10, 106, head, 17, INK)
        mono_lines(s, x + 12, 146, lines, fs=14, gap=26)
    s.box(20, 348, 920, 56, 'keep the set small: one primary metric and a few guardrails',
          'purple', fs=17, opacity=35)
    s.box(20, 422, 920, 46, 'write all four down before the first user sees the product',
          'yellow', fs=16, opacity=45)
    s.save('l15-success-criteria')


# 6 ─ launch gate (numbers from the lab block) ────────────────────────────────────────────────────────
def d_launch_gate():
    s = Scene()
    title(s, 'The launch gate: guardrail first, then the primary metric',
          'beyond the notes: the decision rules of the lab block, in order')
    rows = [
        ('crash rise over the 2% limit?', 'red', 'yes: pause, roll back with the kill switch', 'red'),
        ('activation at or above the 8% target?', 'green', 'yes: widen to the next rollout step', 'green'),
        ('activation below the 3% stop line?', 'orange', 'yes: stop and rethink the feature', 'red'),
    ]
    for i, (q, col, out, ocol) in enumerate(rows):
        y = 92 + i * 88
        s.box(20, y, 380, 56, q, col, fs=15, opacity=45)
        s.box(470, y, 470, 56, out, ocol, fs=15, opacity=35)
        s.arrow([(402, y + 28), (466, y + 28)], color=GREY, sw=2)
        s.arrow([(210, y + 58), (210, y + 86)], color=GREY, sw=2)
        s.text(218, y + 62, 'no', 14, GREY, ff=3)
    s.box(20, 356, 920, 52, 'otherwise: hold between the stop line and the target, read more data',
          'yellow', fs=16, opacity=45)
    s.text(20, 432, 'activation 8.5%, crash +3.0%  ->  pause', 16, RED, ff=3)
    s.text(20, 456, 'activation 8.5%, crash +0.5%  ->  widen', 16, GREEN, ff=3)
    s.text(20, 480, 'activation 5.0%, crash +0.0%  ->  hold', 16, ORANGE, ff=3)
    s.text(20, 504, 'activation 2.0%, crash +0.0%  ->  stop', 16, RED, ff=3)
    s.save('l15-launch-gate')


# 7 ─ big picture ─────────────────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 18 on one page', 'plan the phases, gate the rollout, pick the channels, write the criteria first')
    cols = [
        ('18.1 timeline', 'pre, launch, post; six GTM stages', 'which phase, which checkpoint?', 'orange'),
        ('18.2 de-risk', 'MVP, pilot, phased rollout, kill switch', 'what gate opens the next step?', 'orange'),
        ('18.3 channels', 'organic, paid, sales, partners, bundles', 'where does the ICP already spend time?', 'blue'),
        ('18.4 success', 'primary, target, guardrails, window', 'what would stop this launch?', 'green'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 236
        s.box(x, 84, 225, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 225, 110, core, c, fs=15, opacity=45)
        s.box(x, 280, 225, 92, q, 'yellow', fs=15, opacity=60)
    s.box(10, 392, 940, 58, 'one plan: ICP, a gated rollout, channels that pay back, criteria written first',
          'green', fs=16, opacity=40)
    s.box(10, 462, 940, 36, 'beyond the notes: a launch-day checklist, pitfalls, the launch gate',
          'grey', fs=15, opacity=45)
    s.save('l15-big-picture')


for f in [d_launch_timeline, d_led_compare, d_rollout_ladder, d_channels, d_success_criteria,
          d_launch_gate, d_big_picture]:
    f()

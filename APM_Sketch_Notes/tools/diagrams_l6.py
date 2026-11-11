# Excalidraw scenes for Chapter 9 (page 6, l6-*). Run: python3 diagrams_l6.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)


def lines(s, x, y, items, color=INK, fs=15, dy=22, ff=5):
    for i, t in enumerate(items):
        s.text(x, y + i * dy, t, fs, color, ff=ff)


# 1 ─ where bias enters ───────────────────────────────────────────────────────────────────────────────
def d_bias_sources():
    s = Scene()
    title(s, 'Where bias enters an AI product',
          'six entry points, and each one needs its own test')
    cells = [
        ('historical data\npast hiring or lending decisions', 20, 100),
        ('representation\ngroups, languages, skin tones', 330, 100),
        ('labels\nannotator bias, proxy labels', 640, 100),
        ('objective\nsingle average metric\nhides minority groups', 20, 204),
        ('evaluation set\nwithout your groups hides it', 330, 204),
        ('product design\ndefaults, prompts, UI choices', 640, 204),
    ]
    for t, x, y in cells:
        s.box(x, y, 300, 86, t, 'red', fs=14, opacity=35)
    s.box(20, 312, 920, 36, 'fairness is measured by segment, and it is a design decision',
          'purple', fs=16, opacity=35)
    s.text(20, 364, 'practical steps', 19, PURPLE)
    steps = [
        '1 identify affected\ngroups: language and\nregion for Indian users',
        '2 build an eval set\nwith those groups,\nreport per segment',
        '3 gap threshold that\nblocks launch (any\ngroup within X points)',
        '4 user error reports,\nreviewed by segment',
        '5 document known\nlimits in the model\ncard or product docs',
    ]
    for i, t in enumerate(steps):
        s.box(10 + i * 190, 396, 182, 92, t, 'orange', fs=14, opacity=50)
    s.box(10, 506, 940, 36, 'Indian context: test Hinglish, Indian languages and accents',
          'teal', fs=15, opacity=40)
    s.save('l6-bias-sources')


# 2 ─ fairness is not one number ──────────────────────────────────────────────────────────────────────
def d_fairness_conflict():
    s = Scene()
    title(s, 'Fairness is not one number',
          'the definitions conflict, so choosing one is a values decision')
    defs = [
        ('equal error rates\nfalse positive rate parity', 20),
        ('equal positive outcomes\ndemographic parity\nwrong if base rates differ', 335),
        ('calibration\na score means the same\nfor every group', 650),
    ]
    for t, x in defs:
        s.box(x, 96, 290, 100, t, 'purple', fs=15, opacity=50)
    s.box(20, 222, 920, 96,
          'when base rates differ, a model generally cannot\nmeet calibration and equal error rates at once\nin general (the COMPAS debate, 2016)',
          'red', fs=15, opacity=35)
    s.box(20, 336, 920, 36, 'choosing a definition is a values decision, not technical',
          'yellow', fs=16, opacity=60)
    s.box(20, 390, 920, 84,
          'generative AI adds representational harms: stereotyped images,\n'
          'unequal quality across languages, toxic outputs about groups.\n'
          'test prompts across groups and languages, not just accuracy.',
          'teal', fs=15, opacity=35)
    s.box(20, 492, 920, 60,
          'pick by the harm. In lending, unequal false rejections\n'
          'often matter more, so error-rate parity is often the priority.',
          'green', fs=15, opacity=35)
    s.save('l6-fairness-conflict')


# 3 ─ DPDP timeline ───────────────────────────────────────────────────────────────────────────────────
def d_dpdp_timeline():
    s = Scene()
    title(s, 'DPDP Act 2023 and Rules 2025: the phased timeline',
          'status as of November 2026; most duties apply from 13 May 2027')
    s.line([(30, 232), (930, 232)], color=GREY, sw=3)
    cols = [
        ('11 Aug 2023', 'Presidential assent\non the Act.', 'orange'),
        ('13 Nov 2025', 'DPDP Rules, 2025 notified.\nDefinitions and Data\nProtection Board provisions\nin force.', 'orange'),
        ('13 Nov 2026', 'Consent Manager\nregistration (Rule 4).', 'orange'),
        ('13 May 2027', 'Substantive duties:\nnotice, consent, security,\nbreach reports, retention,\nchildren, rights, SDF duties', 'yellow'),
    ]
    for i, (date, body, c) in enumerate(cols):
        x0 = 20 + i * 236
        s.text(x0, 180, date, 18, PURPLE)
        s.box(x0 + 98, 224, 16, 16, None, c, shape='ellipse', opacity=100)
        s.box(x0, 262, 224, 136, body, c, fs=14, opacity=45)
    s.box(20, 420, 940, 62,
          'January 2026: MeitY consulted on cutting 18 months to 12.\n'
          'No amendment seen in the reports found; 13 May 2027 stands.',
          'purple', fs=15, opacity=35)
    s.text(20, 498, 'check for a Gazette amendment before quoting a date', 15, RED)
    s.save('l6-dpdp-timeline')


# 4 ─ EU AI Act risk pyramid ──────────────────────────────────────────────────────────────────────────
def d_eu_pyramid():
    s = Scene()
    title(s, 'EU AI Act: four risk tiers',
          'classify the product first; the tier sets the duties')
    tiers = [
        ('unacceptable: prohibited\nsocial scoring, untargeted face scraping', 'red', 340),
        ('high-risk: duties before the product ships\nAnnex III: CV screening, credit scoring', 'orange', 480),
        ('transparency (Article 50)\ntell users it is AI; label AI content and deepfakes', 'yellow', 620),
        ('minimal risk: no new obligations\nspam filters, most recommendation features', 'green', 760),
    ]
    for i, (t, c, w) in enumerate(tiers):
        s.box(480 - w / 2, 96 + i * 78, w, 66, t, c, fs=14, opacity=45)
    lines(s, 40, 412, [
        'GPAI models: documentation, copyright policy,',
        'and a summary of the training content.',
        'Systemic risk (above 10^25 FLOPs, presumed): evaluations,',
        'adversarial testing, incident reporting, cybersecurity.',
        'Fines: up to EUR 35 million or 7% of global turnover',
        '(prohibited); EUR 15 million or 3% for most other breaches.',
    ], fs=15, dy=24)
    s.save('l6-eu-pyramid')


# 5 ─ EU AI Act timeline with the Digital Omnibus ─────────────────────────────────────────────────────
def d_eu_timeline():
    s = Scene()
    title(s, 'EU AI Act timeline, with the Digital Omnibus changes',
          'as of November 2026: some duties apply now, high-risk duties moved')
    rows = [
        ('1 Aug 2024', 'Act entered into force', '', 'grey'),
        ('2 Feb 2025', 'Prohibited practices and AI literacy duties', '', 'green'),
        ('2 Aug 2025', 'GPAI model obligations, governance, penalties',
         'models already on the market: until 2 Aug 2027', 'green'),
        ('2 Aug 2026', 'Commission enforcement powers over GPAI providers',
         'Article 50 transparency duties generally', 'green'),
        ('2 Dec 2026', 'Grace period ends for marking AI-generated content',
         'Digital Omnibus: new ban on non-consensual intimate images', 'orange'),
        ('2 Dec 2027', 'High-risk duties, Annex III systems (was 2 Aug 2026)',
         'deferred by the Digital Omnibus', 'red'),
        ('2 Aug 2028', 'High-risk duties, AI in Annex I regulated products',
         '(was 2 Aug 2027)', 'red'),
    ]
    for i, (date, l1, l2, c) in enumerate(rows):
        y = 96 + i * 52
        s.text(20, y + 12, date, 16, PURPLE, ff=3)
        body = l1 + ('\n' + l2 if l2 else '')
        s.box(190, y, 760, 46, body, c, fs=14, opacity=45)
    s.box(20, 466, 930, 84,
          'Digital Omnibus on AI: proposed Nov 2025; deal 7 May 2026\n'
          'Parliament 16 June; Council 29 June 2026; Official Journal\n'
          'obligations deferred, not removed. Confirm against EUR-Lex.',
          'purple', fs=15, opacity=35)
    s.save('l6-eu-timeline')


# 6 ─ safety layers of defence ────────────────────────────────────────────────────────────────────────
def d_safety_layers():
    s = Scene()
    title(s, 'Safety: five layers of defence',
          'the content policy is written first; the layers enforce it')
    layers = [
        ('1 model training: refuse or safely complete risky requests', 'teal'),
        ('2 input filters: classify prompts by policy category', 'teal'),
        ('3 output filters: check responses before display', 'teal'),
        ('4 product design: limit tools, rate limits, account signals', 'orange'),
        ('5 human review and escalation: borderline, high severity', 'blue'),
    ]
    for i, (t, c) in enumerate(layers):
        s.box(40, 96 + i * 66, 540, 54, t, c, fs=15, opacity=45)
    s.box(620, 96, 320, 252,
          'misuse: a user deliberately\nseeks harm, e.g. jailbreaks\n\n'
          'failure: a normal request\ngets bad behaviour, e.g. a\nwrong medical dosage\n\n'
          'both need controls; the controls differ',
          'purple', fs=14, opacity=35)
    s.box(20, 436, 920, 46, 'red-team before launch and on a schedule; turn findings into tests',
          'red', fs=15, opacity=35)
    s.box(20, 494, 920, 46, 'tiered replies: crisis resources for self-harm; decline and offer an alternative',
          'green', fs=15, opacity=35)
    s.text(20, 552, 'a policy with examples of allowed and disallowed requests', 15, GREY)
    s.save('l6-safety-layers')


# 7 ─ explainability and disclosure ───────────────────────────────────────────────────────────────────
def d_disclosure_ladder():
    s = Scene()
    title(s, 'Explainability and disclosure: depth matches the stakes',
          'what the user needs to decide whether to trust or contest')
    s.text(20, 92, 'disclosure answers', 19, PURPLE)
    s.text(500, 92, 'explanation depth (the ladder)', 19, PURPLE)
    disc = [
        'Is this AI?\nlabel AI content and AI-driven decisions',
        'What data did it use?\nsay when personal data personalises',
        'Is a human in the loop?\nsay when one is, or is not',
    ]
    for i, t in enumerate(disc):
        s.box(20, 126 + i * 76, 420, 62, t, 'teal', fs=14, opacity=45)
    rungs = [
        ('consumers: one-line reason\n"recommended because you watched X"', 'green', 440),
        ('loan officer: detailed factor list\nthe top factors in the decision', 'orange', 400),
        ('auditors: full logs\nevery input, output and version', 'purple', 360),
    ]
    for i, (t, c, w) in enumerate(rungs):
        s.box(500 + (440 - w) / 2, 126 + i * 76, w, 62, t, c, fs=14, opacity=45)
    s.box(20, 368, 920, 56,
          'post-hoc rationales can mislead: do not present a generated\n'
          'rationale as the real cause unless it has been validated',
          'red', fs=15, opacity=35)
    s.box(20, 440, 920, 40, 'PM check: what would a user need to trust or contest this?',
          'yellow', fs=16, opacity=60)
    s.save('l6-disclosure-ladder')


# 8 ─ big picture cheat sheet ─────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 9 on one page: five areas, five questions',
          'responsible AI is designed in, measured and disclosed')
    cols = [
        ('9.1 Bias and fairness', 'segment metrics, a gap gate, a chosen definition',
         'who is worse off, and by how much?', 'teal'),
        ('9.2 Privacy (DPDP)', 'notice, consent, purpose, retention, 72-hour breach',
         'what do we hold, why, and until when?', 'teal'),
        ('9.3 Safety and misuse', 'content policy, layered filters, red-teaming',
         'what will we refuse, and how do we know?', 'red'),
        ('9.4 Explainability', 'say when AI is involved, and why this output',
         'what does the user need to trust or contest?', 'teal'),
        ('9.5 Regulation', 'map the tier and the role, then the dates',
         'which tier, which duties, which dates?', 'orange'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 192
        s.box(x, 84, 182, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 182, 110, core, c, fs=15, opacity=45)
        s.box(x, 280, 182, 92, q, 'yellow', fs=15, opacity=60)
    s.box(10, 392, 940, 58, 'a responsible AI product = requirements with owners, metrics and gates',
          'purple', fs=17, opacity=35)
    s.box(10, 462, 940, 36, 'good outcome: classified, measured by segment, disclosed', 'green',
          fs=15, opacity=45)
    s.save('l6-big-picture')


for f in [d_bias_sources, d_fairness_conflict, d_dpdp_timeline, d_eu_pyramid,
          d_eu_timeline, d_safety_layers, d_disclosure_ladder, d_big_picture]:
    f()

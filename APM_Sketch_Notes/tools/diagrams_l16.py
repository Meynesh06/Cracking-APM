# Excalidraw scenes for Chapter 19 (page 16, l16-*). Run: python3 diagrams_l16.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


# 1 ─ Porter's five forces ─────────────────────────────────────────────────────────────────────────
def d_five_forces():
    s = Scene()
    title(s, "Porter's five forces: pressure on industry profit",
          'the industry as a whole, not one company')
    s.box(330, 218, 300, 80, 'industry profit\nhow much it can sustain', 'purple', fs=18)
    s.box(280, 96, 400, 74, 'rivalry among existing players\nmany similar players: prices and margins fall',
          'purple', fs=15, opacity=60)
    s.box(20, 200, 270, 96, 'buyer power\nfew buyers, big shares of revenue\ncan demand lower prices',
          'purple', fs=14, opacity=60)
    s.box(670, 200, 270, 96, 'supplier power\nfew suppliers, or one critical part\nleverage over cost and timing',
          'purple', fs=14, opacity=60)
    s.box(20, 344, 440, 80, 'threat of new entrants\nlow capital, easy access to distribution\nbarriers: patents, scale, brand, licences',
          'purple', fs=14, opacity=60)
    s.box(500, 344, 440, 80, 'threat of substitutes\na different product meets the same need\nit caps the price you can charge',
          'purple', fs=14, opacity=60)
    s.arrow([(480, 170), (480, 216)], color=RED, sw=3)
    s.arrow([(290, 248), (328, 248)], color=RED, sw=3)
    s.arrow([(670, 248), (632, 248)], color=RED, sw=3)
    s.arrow([(240, 344), (380, 300)], color=RED, sw=3)
    s.arrow([(720, 344), (580, 300)], color=RED, sw=3)
    s.box(20, 442, 920, 44, 'check first: is the industry structurally profitable at all?',
          'yellow', fs=17, opacity=65)
    s.save('l16-five-forces')


# 2 ─ SWOT 2x2 ──────────────────────────────────────────────────────────────────────────────────────
def d_swot_grid():
    s = Scene()
    title(s, 'SWOT: a 2x2 grid, then match the rows',
          'internal or external, helpful or harmful')
    s.text(150, 88, 'helpful', 18, PURPLE)
    s.text(490, 88, 'harmful', 18, PURPLE)
    s.text(20, 170, 'internal', 18, PURPLE)
    s.text(20, 330, 'external', 18, PURPLE)
    s.box(150, 116, 330, 150, 'STRENGTHS\ncost, features, culture, reputation\nexample: an existing customer base',
          'green', fs=16, opacity=50)
    s.box(490, 116, 330, 150, 'WEAKNESSES\ngaps: distribution, thin engineering bench\nexample: no experience of physical devices',
          'red', fs=16, opacity=40)
    s.box(150, 276, 330, 150, 'OPPORTUNITIES\nmarket growth, new technology\na competitor\'s weakness',
          'green', fs=16, opacity=50)
    s.box(490, 276, 330, 150, 'THREATS\nnew rivals, adverse regulation\ninput cost shocks',
          'red', fs=16, opacity=40)
    s.box(0, 440, 960, 44, 'match: each opportunity to a strength, each threat to a weakness',
          'yellow', fs=17, opacity=65)
    s.save('l16-swot-grid')


# 3 ─ the Five Cs ───────────────────────────────────────────────────────────────────────────────────
def d_five_cs():
    s = Scene()
    title(s, 'The Five Cs: the wider scan before a launch',
          'the whole picture around the decision')
    cards = [
        ('1 Company', 'products, culture, brand\nstrengths and weaknesses'),
        ('2 Competitors', 'direct, potential and\nsubstitute products\nshare, positioning, next moves'),
        ('3 Customers', 'demographics, buying\nbehaviour, size, channels\nunmet needs'),
        ('4 Collaborators', 'suppliers, distributors\nand partners that make\nsuccess possible'),
        ('5 Climate', 'regulation, technology\neconomy, culture\na hostile climate can\nkill a good idea'),
    ]
    for i, (head, body) in enumerate(cards):
        x = 10 + i * 192
        s.box(x, 100, 182, 60, head, 'purple', fs=17, opacity=60)
        s.box(x, 164, 182, 170, body, 'purple', fs=14, opacity=25)
    s.box(10, 360, 940, 40, 'SWOT: "should we do this?" with a bias to the company', 'yellow', fs=17, opacity=65)
    s.box(10, 412, 940, 40, 'Five Cs: "what does the whole picture look like?" before entry', 'yellow',
          fs=17, opacity=45)
    s.box(10, 462, 940, 30, 'frameworks overlap: use them as checklists, not as answers', 'grey', fs=15, opacity=50)
    s.save('l16-five-cs')


# 4 ─ moats ──────────────────────────────────────────────────────────────────────────────────────────
def d_moats():
    s = Scene()
    title(s, 'Moats: durable advantage, not features',
          'what keeps customers when a rival copies the product')
    moats = [
        'network effects: value grows with users',
        'switching costs: data, workflows, integrations',
        'scale economies: unit cost falls with volume',
        'proprietary data: better product, more users',
        'brand and trust: loyalty, pricing power',
        'distribution: exclusive channels, default placement',
        'regulatory or IP: patents, licences, certificates',
    ]
    for i, t in enumerate(moats):
        s.box(20, 96 + i * 50, 440, 40, t, 'green', fs=15, opacity=50)
    s.text(490, 96, 'Helmer 7 Powers (the rigorous list)', 18, PURPLE)
    powers = ['scale economies', 'network economies', 'counter-positioning', 'switching costs',
              'branding', 'cornered resource', 'process power']
    for i, t in enumerate(powers):
        s.text(506, 128 + i * 26, '- ' + t, 16, INK, ff=3)
    s.box(490, 336, 430, 104, 'test a moat\nif a well-funded rival copied it tomorrow,\nwhat still keeps customers with us?\nfeatures alone = no moat',
          'yellow', fs=15, opacity=55)
    s.box(20, 452, 920, 34, 'features alone are not a moat', 'grey', fs=15, opacity=45)
    s.save('l16-moats')


# 5 ─ market sizing: TAM, SAM, SOM with the worked numbers ──────────────────────────────────────────
def d_market_sizing():
    s = Scene()
    title(s, 'Market sizing: TAM, SAM, SOM (Pune e-scooters)',
          'all numbers illustrative; bottom-up method')
    s.box(20, 96, 520, 84, 'TAM: everyone who could ever use it\n1.8M households x 50% = 900,000 households',
          'blue', fs=15, opacity=45)
    s.box(90, 200, 400, 84, 'SAM: reachable with product, price, channels\n30% can charge at home and afford it',
          'teal', fs=15, opacity=45)
    s.box(130, 304, 360, 84, 'SOM: share to win in 3 to 5 years\n10% of SAM in 3 years',
          'green', fs=15, opacity=55)
    s.text(580, 96, 'bottom-up chain', 18, PURPLE)
    chain = [
        ('1,800,000 households', INK),
        ('x 50% with a two-wheeler need', INK),
        ('= 900,000 households', INK),
        ('one scooter every 6 years', INK),
        ('= 150,000 scooters a year', INK),
        ('x Rs 1.2 lakh each', PINK),
        ('= about Rs 1,800 crore a year', PINK),
    ]
    for i, (t, c) in enumerate(chain):
        s.text(580, 128 + i * 26, t, 15, c, ff=3)
    s.box(20, 404, 920, 40, 'SAM: 45,000 scooters, about Rs 540 crore. SOM: 4,500, about Rs 54 crore',
          'pink', fs=15, opacity=30)
    s.box(20, 454, 920, 32, 'cross-check top-down: does Pune land in the same range?', 'yellow',
          fs=15, opacity=65)
    s.save('l16-market-sizing')


# 6 ─ entry checklist ────────────────────────────────────────────────────────────────────────────────
def d_entry_checklist():
    s = Scene()
    title(s, 'Market entry checklist: should we enter, then how',
          "Sigma concept book's 'Market Entry' section")
    left = [
        ('1 company fit', 'goals, vision, VRIN, SWOT, what we excel at'),
        ('2 industry structure', 'market size, growth, five forces'),
        ('3 competitors', 'how many, and what they are doing'),
        ('4 feasibility', 'operations, finance, distribution, expertise'),
    ]
    right = [
        ('5 customers', 'target, overlap with rivals, value offer'),
        ('6 alternative strategies', 'trade-offs on cost and time to market'),
        ('7 risks', 'legal and compliance, market, operational'),
    ]
    for i, (h, b) in enumerate(left):
        s.box(20, 96 + i * 66, 460, 56, h + '\n' + b, 'purple', fs=15, opacity=45)
    for i, (h, b) in enumerate(right):
        s.box(500, 96 + i * 66, 440, 56, h + '\n' + b, 'purple', fs=15, opacity=45)
    s.box(500, 300, 440, 70, 'how should we enter?\ntiming, then the route:\nfrom scratch (STP, 4Ps), JV, or M&A',
          'orange', fs=15, opacity=45)
    s.box(20, 392, 920, 76, 'write the go/no-go thresholds BEFORE the analysis\n'
          'example: SOM above Rs X crore in 3 years, break-even within 24 months',
          'green', fs=16, opacity=50)
    s.box(20, 478, 920, 26, 'the decision is defensible only when the bar was set first', 'grey', fs=14, opacity=40)
    s.save('l16-entry-checklist')


# 7 ─ build, partner or buy ─────────────────────────────────────────────────────────────────────────
def d_build_partner_buy():
    s = Scene()
    title(s, 'Build, partner or buy: three routes, one lens',
          'the capability decides the route, not habit')
    routes = [
        ('BUILD', 'develop in-house', 'full control and IP', 'slower and riskier', 'right when core to the moat'),
        ('PARTNER', 'alliance, licence, channel deal', 'fast and low-capital', 'you depend on the partner', 'may share data'),
        ('ACQUIRE', 'buy a company or team', 'fastest route to capability', 'expensive, hard to integrate', 'culture and product fit'),
    ]
    for i, (h, *lines) in enumerate(routes):
        s.box(20 + i * 320, 96, 280, 200, h + '\n' + '\n'.join(lines), 'orange', fs=15, opacity=40)
    lens = [('1 is it core?', 'defines your moat?'), ('2 time to market', 'window in months?'),
            ('3 cost and risk', 'total cost, not price'), ('4 integration load', 'culture or incentives'),
            ('5 reversibility', 'easier to unwind (partner)')]
    for i, (h, b) in enumerate(lens):
        s.box(20 + i * 186, 330, 176, 70, h + '\n' + b, 'purple', fs=14, opacity=50)
    s.box(20, 420, 920, 44, 'staged plan: partner now to test demand, acquire later if usage clears a bar',
          'yellow', fs=17, opacity=65)
    s.save('l16-build-partner-buy')


# 8 ─ chapter 19 on one page ───────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 19 on one page: five tools, five questions',
          'from the industry down to the route in')
    cols = [
        ('19.1 Five Forces', 'the industry:\nis it profitable?', 'is the industry worth entering?', 'purple'),
        ('19.2 SWOT, 5 Cs', 'the company and\nthe whole picture', 'does a strength match each threat?', 'purple'),
        ('19.3 Moats', 'durable advantage\nvs rivals', 'what keeps customers if copied?', 'green'),
        ('19.4 Sizing, entry', 'TAM, SAM, SOM\nand go/no-go', 'is the market big enough, and how?', 'pink'),
        ('19.5 Build or buy', 'build, partner\nor acquire', 'which route: how fast, how core?', 'orange'),
    ]
    for i, (head, core, q, c) in enumerate(cols):
        x = 10 + i * 192
        s.box(x, 84, 182, 62, head, 'purple', fs=15, opacity=60)
        s.box(x, 158, 182, 110, core, c, fs=15, opacity=45)
        s.box(x, 280, 182, 92, q, 'yellow', fs=15, opacity=60)
    s.box(10, 392, 940, 58, 'strategy = where to play, how to win, how to get there', 'purple', fs=17, opacity=35)
    s.box(10, 462, 940, 36, 'beyond · good answer: a number, a route, and a threshold that decides', 'green', fs=15, opacity=45)
    s.save('l16-big-picture')


for f in [d_five_forces, d_swot_grid, d_five_cs, d_moats, d_market_sizing, d_entry_checklist,
          d_build_partner_buy, d_big_picture]:
    f()

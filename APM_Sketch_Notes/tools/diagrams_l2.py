# Excalidraw scenes for Chapter 5 (page 2, l2-*). Run: python3 diagrams_l2.py ../diagrams/src   (lchk.sh does this)
from scene import Scene, INK
from dhelp import RED, GREEN, BLUE, PURPLE, ORANGE, TEAL, GREY, _tw
from shelp import title

YEL = '#f08c00'   # yellow as a text colour (the highlight)
PINK = '#9c36b5'  # pink as a text colour (money)


# 1 ─ AI contains ML, which contains deep learning and GenAI ──────────────────────────────────────────
def d_ai_nesting():
    s = Scene()
    title(s, 'AI contains ML, which contains deep learning and GenAI',
          'each term is a subset of the one before it')
    s.zone(0, 84, 600, 400, 'zblue')
    s.text(14, 92, 'AI: any system that does a task needing judgement', 16, INK)
    s.box(440, 124, 150, 60, 'rules engine\nalso counts as AI', 'grey', fs=14, opacity=60)
    s.zone(14, 124, 410, 350, 'zpurple')
    s.text(28, 132, 'machine learning: learns from examples', 16, INK)
    s.zone(30, 166, 380, 226, 'zgreen')
    s.text(44, 174, 'deep learning: many-layer neural networks', 15, INK)
    s.box(50, 206, 170, 110, 'generative AI\nLLMs, diffusion\nmodels', 'teal', fs=15, opacity=70)
    s.box(236, 206, 165, 110, 'predictive DL\nUber ETA\n(DeepETA)', 'teal', fs=15, opacity=50)
    s.box(50, 410, 340, 44, 'classic ML: Gmail spam filter', 'teal', fs=15, opacity=50)
    s.text(620, 92, 'where the examples sit', 18, PURPLE)
    for i, t in enumerate(['Gmail spam filter: classic ML',
                           'Google Photos search: deep learning',
                           'ChatGPT, Claude, Gemini: GenAI (LLMs)',
                           'Uber ETA (DeepETA): predictive DL']):
        s.text(620, 126 + i * 34, t, 14, INK)
    s.box(620, 300, 330, 96, 'Could a rules engine or a simple\nstatistical model solve 80% of it?\nIf yes, start there.',
          'yellow', fs=15, opacity=60)
    s.box(0, 500, 960, 40, 'GenAI produces new content; classic ML mostly predicts',
          'purple', fs=15, opacity=30)
    s.save('l2-ai-nesting')


# 2 ─ three learning types, and the LLM training pipeline that uses all three ─────────────────────────
def d_learning_types():
    s = Scene()
    title(s, 'Learning types differ by the feedback the model gets',
          'labelled answers, no answers, or rewards for actions')
    cols = [
        (0, 'supervised learning', 'input plus the correct answer', 'used for: spam, price prediction',
         'PM: where do the labels come from\nand how reliable are they?'),
        (330, 'unsupervised learning', 'no labels: finds the structure', 'used for: segments, anomalies, topics',
         'PM: who checks the clusters mean\nsomething to the business?'),
        (660, 'reinforcement learning', 'actions scored by rewards over time', 'used for: games, robots, ad bidding',
         'PM: what is the reward, and can the\nsystem game it?'),
    ]
    for x, head, feedback, used, pm in cols:
        s.box(x, 84, 300, 44, head, 'purple', fs=18)
        s.box(x, 138, 300, 46, feedback, 'teal', fs=15)
        s.text(x + 4, 196, used, 15, INK)
        s.box(x, 226, 300, 60, pm, 'yellow', fs=15, opacity=60)
    s.text(0, 306, 'an LLM assistant uses all three types, in one pipeline', 19, PURPLE)
    steps = [
        ('pre-training', 'self-supervised:', 'predict the next token'),
        ('supervised fine-tuning', 'human example chats', 'teach the assistant format'),
        ('preference tuning', 'RLHF: humans rank outputs', 'DPO and RLAIF are related'),
        ('reasoning RL', 'verifiable rewards:', 'maths and code tests'),
    ]
    for i, (a, b, c) in enumerate(steps):
        x = i * 250
        s.box(x, 340, 210, 92, f'{a}\n{b}\n{c}', 'orange', fs=14, opacity=55)
        if i < 3:
            s.arrow([(x + 210, 386), (x + 248, 386)], color=ORANGE, sw=3)
    s.box(0, 452, 960, 40, 'self-supervised: labels made from the data itself',
          'yellow', fs=15, opacity=60)
    s.save('l2-learning-types')


# 3 ─ the ML lifecycle, seven stages, and the LLM-era loop ──────────────────────────────────────────────
def d_ml_lifecycle():
    s = Scene()
    title(s, 'An ML product moves through seven stages',
          'most of the time goes to data and monitoring, not to training')
    row1 = [(0, 100, '1 problem definition', 'decision, metric, baseline'),
            (250, 100, '2 data', 'source, label, split'),
            (500, 100, '3 modelling', 'train, compare to baseline'),
            (750, 100, '4 evaluation', 'offline + slice analysis')]
    row2 = [(750, 230, '5 deployment', 'serve, behind a flag'),
            (500, 230, '6 monitoring', 'drift, quality, KPIs'),
            (250, 230, '7 retraining', 'new data, regression check')]
    for x, y, a, b in row1 + row2:
        s.box(x, y, 210, 84, f'{a}\n{b}', 'orange', fs=14, opacity=55)
    for x in (210, 460, 710):
        s.arrow([(x, 142), (x + 40, 142)], color=ORANGE, sw=3)
    s.arrow([(855, 184), (855, 230)], color=ORANGE, sw=3)
    s.arrow([(750, 272), (712, 272)], color=ORANGE, sw=3)
    s.arrow([(500, 272), (462, 272)], color=ORANGE, sw=3)
    s.arrow([(355, 230), (355, 186)], color=GREY, dashed=True, sw=2)
    s.text(364, 200, 'new data', 14, GREY)
    s.text(0, 340, 'the LLM-era version: data and modelling shrink,', 18, PURPLE)
    s.text(0, 364, 'and evaluation grows', 18, PURPLE)
    loop = [('define the task', 'and the acceptance bar'),
            ('write prompt, retrieval', 'build an eval set'),
            ('iterate against the evals', 'ship behind a flag'),
            ('re-run evals on every', 'model or prompt change')]
    for i, (a, b) in enumerate(loop):
        x = i * 250
        s.box(x, 394, 210, 56, f'{a}\n{b}', 'teal', fs=14, opacity=55)
        if i < 3:
            s.arrow([(x + 210, 422), (x + 248, 422)], color=TEAL, sw=3)
    s.box(0, 468, 960, 40, 'fine-tuning comes later, if at all', 'grey', fs=15, opacity=50)
    s.save('l2-ml-lifecycle')


# 4 ─ tokens, the context window and what it costs ─────────────────────────────────────────────────────
def d_tokens_context():
    s = Scene()
    title(s, 'Tokens set the cost; the context window sets the limit',
          'a big window is a limit on what one call can read, not memory')
    s.box(0, 84, 440, 84, '1 token is about 4 characters,\nor about three-quarters of a word.\n'
          '1,000 tokens is about 750 words.', 'teal', fs=15, opacity=55)
    s.box(500, 84, 460, 84, 'input and output billed separately\nper million tokens; output often costs\n'
          'more. Prices fall: date every quote.', 'pink', fs=15, opacity=35)
    s.text(0, 190, 'context window: all input plus output in one call', 18, PURPLE)
    segs = [('system prompt', 150, 'purple'), ('chat history', 190, 'blue'), ('retrieved text', 300, 'teal'),
            ('question', 120, 'blue'), ('answer room', 200, 'orange')]
    x = 0
    for lab, w, c in segs:
        s.box(x, 226, w, 56, lab, c, fs=15, opacity=60)
        x += w
    s.line([(400, 290), (600, 290)], color=RED, sw=3)
    s.text(400, 298, 'lost in the middle: facts here get missed', 15, RED)
    s.box(0, 336, 310, 96, 'you pay for every input token\non every call: a long context\nis a recurring cost',
          'pink', fs=15, opacity=35)
    s.box(325, 336, 310, 96, 'no memory between calls.\nchat memory is history or saved\nfacts re-sent inside the window',
          'blue', fs=15, opacity=35)
    s.box(650, 336, 310, 96, 'quality can drop for facts buried\nin the middle of a very long window\n'
          'so test with real documents', 'yellow', fs=15, opacity=50)
    s.box(0, 452, 960, 40, 'prompts are product code: version them, test them, monitor them',
          'purple', fs=15, opacity=30)
    s.save('l2-tokens-context')


# 5 ─ the RAG pipeline ───────────────────────────────────────────────────────────────────────────────
def d_rag_pipeline():
    s = Scene()
    title(s, 'RAG: retrieve the right passages, then answer from them',
          'embeddings are the search index that makes it work')
    steps = [('chunk\ndocuments', 'orange'), ('embed and\nindex', 'teal'),
             ('retrieve top matches\n(semantic + keyword)', 'teal'),
             ('re-rank\nthe results', 'orange'), ('generate with\ncitations', 'teal')]
    for i, (t, c) in enumerate(steps):
        x = i * 198
        s.box(x, 96, 168, 84, t, c, fs=14, opacity=60)
        if i < 4:
            s.arrow([(x + 168, 138), (x + 196, 138)], color=GREY, sw=3)
    s.text(0, 194, 'failure modes', 17, RED)
    fails = ['poor retrieval:\nwrong chunks', 'chunks split the\ncontext they need',
             'stale or conflicting\ndocuments', 'answer ignores the\nretrieved text']
    for i, t in enumerate(fails):
        s.box(i * 246, 220, 222, 66, t, 'red', fs=14, opacity=35)
    s.text(0, 304, 'evaluate the two halves separately', 18, PURPLE)
    s.box(0, 332, 470, 70, 'retrieval: did the right passage appear\nin the top results?', 'teal', fs=15, opacity=55)
    s.box(490, 332, 470, 70, 'generation: is the answer faithful to the\npassages, and does it answer the question?',
          'orange', fs=15, opacity=50)
    s.box(0, 420, 960, 56, 'good for: company documents, policies, catalogues,\n'
          'and anything that changes. Gives citations; no retraining.', 'green', fs=15, opacity=40)
    s.save('l2-rag-pipeline')


# 6 ─ prompting vs RAG vs fine-tuning, and long context ──────────────────────────────────────────────
def d_rag_ft_long():
    s = Scene()
    title(s, 'Prompting, RAG or fine-tuning: each changes something else',
          'start with the cheapest one; move on only when it fails on evals')
    heads = ['prompting', 'RAG', 'fine-tuning']
    cols = [180, 440, 700]
    for x, h in zip(cols, heads):
        s.box(x, 84, 250, 40, h, 'purple', fs=17, opacity=60)
    rows = [
        ('changes', 130, 50, [('instructions', 'grey'), ('what the model knows\nat query time', 'grey'),
                              ('how the model behaves', 'grey')]),
        ('fresh facts', 186, 40, [('no', 'red'), ('yes', 'green'), ('no: goes stale', 'red')]),
        ('citations', 232, 40, [('no', 'red'), ('yes', 'green'), ('no', 'red')]),
        ('upfront cost', 278, 50, [('lowest', 'green'), ('medium: pipeline, index', 'orange'),
                                   ('highest: data, training, re-evals', 'red')]),
        ('best for', 334, 56, [('a first version', 'teal'), ('private or changing knowledge', 'teal'),
                               ('tone, format, narrow tasks, cost cutting', 'teal')]),
    ]
    for label, y, h, cells in rows:
        s.text(4, y + h / 2 - 9, label, 16, INK)
        for x, (t, c) in zip(cols, cells):
            s.box(x, y, 250, h, t, c, fs=14, opacity=40)
    steps = ['step 1: prompting', 'step 2: add RAG for knowledge', 'step 3: fine-tune for behaviour']
    for i, t in enumerate(steps):
        x = i * 340
        s.box(x, 404, 280, 40, t, 'orange', fs=15, opacity=55)
        if i < 2:
            s.arrow([(x + 280, 424), (x + 338, 424)], color=ORANGE, sw=3)
    s.text(0, 452, 'move on only when the cheaper option fails on evals', 15, INK)
    s.box(0, 480, 960, 50, 'long context: fine for a small corpus; costly and less reliable\n'
          'as it grows; no per-user access control.', 'grey', fs=14, opacity=50)
    s.save('l2-rag-ft-long')


# 7 ─ the agent loop with tools ───────────────────────────────────────────────────────────────────────
def d_agent_loop():
    s = Scene()
    title(s, 'An agent loops: plan, act with a tool, observe, decide',
          'it stops on success, a limit, or a handoff to a person')
    s.text(100, 84, 'the agent loop', 18, PURPLE)
    s.box(100, 110, 200, 56, 'plan the next step', 'orange', fs=15, opacity=55)
    s.box(400, 110, 200, 56, 'act: call a tool', 'teal', fs=15, opacity=55)
    s.box(400, 230, 200, 56, 'observe the result', 'orange', fs=15, opacity=55)
    s.box(100, 230, 200, 56, 'decide: stop or repeat', 'orange', fs=15, opacity=55)
    s.arrow([(300, 138), (400, 138)], color=ORANGE, sw=3)
    s.arrow([(500, 166), (500, 230)], color=ORANGE, sw=3)
    s.arrow([(400, 258), (300, 258)], color=ORANGE, sw=3)
    s.arrow([(200, 230), (200, 166)], color=ORANGE, sw=3)
    s.text(230, 190, 'loop until done', 15, GREY)
    s.box(680, 110, 280, 70, 'stops on success,\na step or cost limit,\nor a handoff', 'green', fs=14, opacity=40)
    s.box(680, 196, 280, 60, 'tools: few, well described,\nleast privilege; log each call', 'teal', fs=14, opacity=40)
    s.box(680, 272, 280, 70, 'send, pay or delete: approval\ngate first (human confirmation)', 'red', fs=14, opacity=35)
    s.box(0, 360, 470, 62, 'workflow: the developer fixes the steps in code\n'
          'the LLM fills in each step; cheaper, predictable', 'orange', fs=15, opacity=45)
    s.box(490, 360, 470, 62, 'agent: the model decides the next step itself\n'
          'use it only when the path cannot be known', 'teal', fs=15, opacity=45)
    s.box(0, 436, 960, 56, 'per-step accuracy compounds: 0.95 over five steps = 77%\n'
          'at 0.90 per step, five steps succeed about 59%', 'yellow', fs=15, opacity=60)
    s.save('l2-agent-loop')


# 8 ─ big picture cheat sheet ─────────────────────────────────────────────────────────────────────────
def d_big_picture():
    s = Scene()
    title(s, 'Chapter 5 on one page: the vocabulary to scope AI work',
          'the goal is to ask the right questions, not to build models')
    cols = [
        ('5.1-5.2 AI and learning types',
         'AI > ML > DL > GenAI\nlabels, no labels, rewards\nLLM pipeline: pre-train, SFT,\npreference tuning, reasoning RL',
         'could rules or a simple\nmodel solve 80% of it?'),
        ('5.3-5.4 lifecycle, LLM basics',
         'ML lifecycle: 7 stages\nmost time on data and\nmonitoring\ntokens drive cost\ncontext is not memory\ntemperature: consistency',
         'can you say what happens\nwhen the model is wrong?'),
        ('5.5 RAG, fine-tuning, embeddings',
         'prompting first\nRAG for facts that change\nfine-tuning for behaviour\nembeddings: search by meaning\nRAG and fine-tuning combine',
         'what changes weekly?\nthen RAG, not training'),
        ('5.6-5.7 agents, CV, speech, recs',
         'errors compound per step\napproval gates, irreversible steps\nCV: test on real cameras\nspeech: test accent, noise\nrecs: pick, rank, re-rank',
         'what does one error cost,\nand who notices?'),
    ]
    for i, (head, core, q) in enumerate(cols):
        x = 10 + i * 240
        s.box(x, 84, 230, 56, head, 'purple', fs=15, opacity=60)
        s.box(x, 150, 230, 186, core, 'teal', fs=14, opacity=40)
        s.box(x, 346, 230, 60, q, 'yellow', fs=14, opacity=60)
    s.box(10, 420, 940, 40, 'good outcome: start simple, justify each step up, test on the real segments',
          'green', fs=15, opacity=40)
    s.box(10, 470, 940, 36, 'the same question for every AI feature: what is the data, the loop, the cost?',
          'purple', fs=15, opacity=30)
    s.save('l2-big-picture')


for f in [d_ai_nesting, d_learning_types, d_ml_lifecycle, d_tokens_context, d_rag_pipeline,
          d_rag_ft_long, d_agent_loop, d_big_picture]:
    f()

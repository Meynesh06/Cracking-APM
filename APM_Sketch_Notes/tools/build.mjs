import zlib from 'node:zlib';
// Build the sketchbook HTML from the master markdown.
// Usage: node build.mjs <notes.md> <diagramsDir> <template.html> <out.html>
import fs from 'fs';
import path from 'path';
import MarkdownIt from 'markdown-it';
import anchor from 'markdown-it-anchor';
import mark from 'markdown-it-mark';
import { createHighlighter } from 'shiki';
import { fileURLToPath } from 'node:url';

const [mdPath, diagDir, tplPath, outPath, imgDir = 'images'] = process.argv.slice(2);
// Project settings live in <project>/dkfile.json (or $DKFILE_CONFIG): names, branding, the word for a page ("Part",
// "Lecture", "Episode"...), the word for the source ("video", "lecture", "book"...). See DEFAULTS for every key.
const HERE = path.dirname(fileURLToPath(import.meta.url));
const CFG_PATH = process.env.DKFILE_CONFIG || path.join(HERE, '..', 'dkfile.json');
const DEFAULTS = {
  title: 'Sketch Notes', description: 'Sketchbook-style study notes with Excalidraw diagrams, real code runs and quiz cards.',
  course: '', unit: 'Part', units: 'Parts', tab: 'P', source: 'video', source_count: 0,
  brand_html: 'sketch·<span>notes</span>', brand_sub: 'sketch notes', sticker: 'sketch notes!',
  hero_html: '<span class="hl">Sketch</span> <span class="py">notes</span>', hero_sub: '',
  cards_title: '', sig_html: 'Happy learning!', about_html: '',
  sir_label: 'In the lecturer’s words', sir_short: 'Lecturer’s words',
  shot_url: 'local lab', shot_tag: 'reproduced locally',
  langs: ['python', 'cpp', 'bash', 'json', 'text', 'sql', 'scala', 'java', 'javascript', 'typescript', 'yaml', 'go', 'rust'],
  code_tabs: { python: 'Python', cpp: 'C++ · as in the video' },
};
const CFG = { ...DEFAULTS, ...(fs.existsSync(CFG_PATH) ? JSON.parse(fs.readFileSync(CFG_PATH, 'utf8')) : {}) };
CFG.unit_lower = CFG.unit.toLowerCase(); CFG.units_lower = CFG.units.toLowerCase();
if (!CFG.cards_title) CFG.cards_title = `Pick a ${CFG.unit_lower}`;
const COURSE = CFG.course;
const traceDir = process.env.TRACE_DIR || path.join(path.dirname(mdPath), '..', 'traces');
const TRACES = {};
const COLORS = ['yellow', 'pink', 'green', 'blue', 'lav', 'orange', 'teal', 'rose', 'lime'];

const hl = await createHighlighter({ themes: ['catppuccin-mocha'], langs: CFG.langs });
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
let SLUG_PREFIX = '';
const slug = s => SLUG_PREFIX + s.replace(/\s*\d+:\d\d(:\d\d)?\s*$/, '').toLowerCase().replace(/<[^>]+>/g, '').replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '-');
const stats = { code: 0, diagrams: 0, notes: 0, quiz: 0, traces: 0 };
const EXC = {};

// hand-drawn-ish mini icons (stroke = currentColor)
const I = (d) => `<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${d}</svg>`;
const ICONS = {
  pin: I('<path d="M9 3.5l6.2 .3-.9 5.2 3.2 3.1-11.4.4 3.4-3.4z"/><path d="M11.8 12.6 12 21"/>'),
  bulb: I('<path d="M9 18h6M10 21.2h4"/><path d="M12 3c-3.6 0-6 2.7-6 5.8 0 2.3 1.3 3.7 2.5 4.9.8.8 1 1.5 1 2.6h5c0-1.1.3-1.8 1.1-2.6 1.2-1.2 2.4-2.6 2.4-4.9C18 5.7 15.6 3 12 3z"/>'),
  warn: I('<path d="M12 3.3 2.8 20.2h18.6z"/><path d="M12 9.5v5M12 17.6v.3"/>'),
  star: I('<path d="m12 3 2.7 5.9 6.3.6-4.8 4.2 1.5 6.3L12 16.8 6.3 20l1.5-6.3L3 9.5l6.3-.6z"/>'),
  cloud: I('<path d="M7 18.5h10.3a3.8 3.8 0 0 0 .5-7.6A5.6 5.6 0 0 0 7 9.7a4.4 4.4 0 0 0 0 8.8z"/>'),
  mic: I('<rect x="9" y="2.8" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0M12 17.6v3.6M8.6 21.2h6.8"/>'),
  clock: I('<circle cx="12" cy="12.4" r="8.6"/><path d="M12 7.2v5.4l3.4 2.1"/>'),
  sir: I('<path d="M4 5.5h16v10H10l-4.5 3.8v-3.8H4z"/><path d="M8 9.4h8M8 12.2h5"/>'),
};
const CALLOUTS = {
  NOTE: { cls: 'yellow', label: 'Note', icon: ICONS.pin },
  TIP: { cls: 'green', label: 'Tip', icon: ICONS.bulb },
  WARNING: { cls: 'pink', label: 'Careful!', icon: ICONS.warn },
  CAUTION: { cls: 'pink', label: 'Careful!', icon: ICONS.warn },
  IMPORTANT: { cls: 'blue', label: 'Important', icon: ICONS.star },
  ANALOGY: { cls: 'lav', label: 'Analogy', icon: ICONS.cloud },
  INTERVIEW: { cls: 'orange', label: 'Interview corner', icon: ICONS.mic },
  SIR: { cls: 'teal', label: CFG.sir_label, icon: ICONS.sir },
  PENDING: { cls: 'grey', label: 'Pending', icon: ICONS.clock },
};

const md = new MarkdownIt({ html: true, linkify: true, typographer: true })
  .use(mark)
  .use(anchor, { slugify: slug, level: [1, 2, 3] });

// ---- code fences → code cards / output strips
md.renderer.rules.fence = (tokens, idx) => {
  const t = tokens[idx];
  const info = t.info.trim();
  const lang = info.split(/\s+/)[0] || 'text';
  const title = (info.match(/title="([^"]+)"/) || [])[1];
  const body = t.content.replace(/\n$/, '');
  if (lang === 'file') {
    return `<div class="output is-file"><span class="out-label">📄 ${esc(title || 'file')} <small>file contents</small></span><pre>${esc(body)}</pre></div>\n`;
  }
  if (lang === 'output' || lang === 'error') {
    return `<div class="output ${lang === 'error' ? 'is-error' : ''}"><span class="out-label">${lang === 'error' ? 'error' : 'output'}</span><pre>${esc(body)}</pre></div>\n`;
  }
  const l = hl.getLoadedLanguages().includes(lang) ? lang : 'text';
  stats.code++;
  const html = hl.codeToHtml(body, { lang: l, theme: 'catppuccin-mocha' });
  return `<figure class="code-card" data-lang="${esc(lang)}"><div class="code-bar"><span class="dots"><i></i><i></i><i></i></span><span class="fname">${esc(title || lang)}</span><button class="copy" type="button">copy</button></div>${html}</figure>\n`;
};

// ---- diagrams/*.svg images → inline real Excalidraw SVG
md.renderer.rules.image = (tokens, idx) => {
  const t = tokens[idx];
  const src = t.attrGet('src');
  const alt = t.content;
  const sh = src.match(/^shots\/([\w.-]+\.(webp|png|jpe?g))$/);
  if (sh) {
    const buf = fs.readFileSync(path.join(diagDir, '..', 'shots', sh[1]));
    const mime = { webp: 'image/webp', png: 'image/png' }[sh[2]] || 'image/jpeg';
    const w = sh[2] === 'webp' ? buf.readUInt32LE(24) & 0xffffff : 0;   // VP8X canvas width - 1 (only for extended webp)
    stats.shots = (stats.shots || 0) + 1;
    return `<figure class="shot" id="shot-${sh[1].replace(/\.\w+$/, '')}"><div class="shot-bar"><span class="dots"><i></i><i></i><i></i></span><span class="shot-url">${esc(CFG.shot_url)}</span><span class="shot-tag">${esc(CFG.shot_tag)}</span></div><div class="shot-scroll"><img src="data:${mime};base64,${buf.toString('base64')}" alt="${esc(alt.replace(/`/g, ''))}" loading="lazy"></div><figcaption><span class="cap">${md.renderInline(alt)}</span><span class="fig-actions"><button class="zoom" type="button">zoom</button></span></figcaption></figure>`;
  }
  const im = src.match(/^images\/([\w.-]+\.(jpe?g|png))$/);
  if (im) {
    const buf = fs.readFileSync(path.join(imgDir, im[1]));
    const mime = /png$/.test(im[1]) ? 'image/png' : 'image/jpeg';
    return `<figure><img src="data:${mime};base64,${buf.toString('base64')}" alt="${esc(alt)}" loading="lazy"><figcaption>${esc(alt)}</figcaption></figure>`;
  }
  const m = src.match(/diagrams\/([\w-]+)\.svg$/);
  if (!m) return `<img src="${esc(src)}" alt="${esc(alt)}" loading="lazy">`;
  let svg = fs.readFileSync(path.join(diagDir, m[1] + '.svg'), 'utf8');
  svg = svg.replace(/<style class="style-fonts">[\s\S]*?<\/style>/, '');   // Excalifont is declared once in the page CSS instead of once per drawing
  svg = svg.replace(/ d="([^"]*)"/g, (_, d) => ` d="${d.replace(/-?\d+\.\d{2,}/g, n => String(Math.round(+n * 10) / 10))}"`);   // path data to 0.1 px: same look, ~8% smaller
  const vbw = +(svg.match(/viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+)/) || [0, 800])[1];
  svg = svg.replace('<svg ', `<svg role="img" aria-label="${esc(alt.replace(/`/g, ''))}" style="--natural:${Math.round(vbw)}px" `);
  EXC[m[1]] = JSON.parse(fs.readFileSync(path.join(diagDir, m[1] + '.excalidraw'), 'utf8'));
  stats.diagrams++;
  return `<figure class="sketch" id="fig-${m[1]}"><div class="sketch-scroll">${svg}</div><figcaption><span class="cap">${md.renderInline(alt)}</span><span class="fig-actions"><button class="zoom" type="button">zoom</button><button class="edit" type="button" data-exc="${m[1]}" title="Copies the drawing; paste it (Ctrl+V) on excalidraw.com">copy for Excalidraw</button><button class="dl" type="button" data-exc="${m[1]}" title="Download ${m[1]}.excalidraw">.excalidraw ↓</button></span></figcaption></figure>`;
};

// ---- GitHub-style callouts  > [!TYPE] Title
md.core.ruler.after('inline', 'callouts', state => {
  const toks = state.tokens;
  for (let i = 0; i < toks.length; i++) {
    if (toks[i].type !== 'blockquote_open') continue;
    let j = i + 1;
    while (j < toks.length && toks[j].type !== 'inline') j++;
    const inl = toks[j];
    const m = inl && inl.content.match(/^\[!(\w+)\][ \t]*([^\n]*)\n?/);
    if (!m) continue;
    const type = m[1].toUpperCase();
    toks[i].meta = { callout: type, title: m[2].trim() };
    inl.content = inl.content.slice(m[0].length);
    inl.children = [];
    state.md.inline.parse(inl.content, state.md, state.env, inl.children);
    if (!inl.content.trim()) { toks[j - 1].hidden = true; toks[j + 1].hidden = true; }
    let depth = 0;
    for (let k = i; k < toks.length; k++) {
      if (toks[k].type === 'blockquote_open') depth++;
      if (toks[k].type === 'blockquote_close' && --depth === 0) { toks[k].meta = { callout: type }; break; }
    }
  }
});
md.renderer.rules.blockquote_open = (tokens, idx) => {
  const m = tokens[idx].meta;
  if (!m || !m.callout) return '<blockquote>';
  if (m.callout === 'PEN') {
    stats.pens = (stats.pens || 0) + 1;
    return `<aside class="pen-note"><svg class="pen-arrow" viewBox="0 0 64 40" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 30c14-2 30-8 46-20"/><path d="M38 8l13 1-4 12"/></svg><span class="pen-text">${md.renderInline(m.title)}</span>`;
  }
  if (m.callout === 'QUESTION') {
    return `<aside class="qa"><div class="bubble q"><span class="who">Doubt</span>${md.renderInline(m.title)}</div><div class="bubble a"><span class="who">Answer</span>`;
  }
  const c = CALLOUTS[m.callout] || CALLOUTS.NOTE;
  if (m.callout !== 'PENDING') stats.notes++;
  return `<aside class="sticky ${c.cls}"><div class="sticky-title">${c.icon}<span>${m.title ? md.renderInline(m.title) : c.label}</span></div>`;
};
md.renderer.rules.blockquote_close = (tokens, idx) => {
  const m = tokens[idx].meta;
  if (!m || !m.callout) return '</blockquote>';
  return m.callout === 'QUESTION' ? '</div></aside>' : '</aside>';
};

// ---- links: timestamp chips + external targets
const defaultLink = md.renderer.rules.link_open || ((t, i, o, e, s) => s.renderToken(t, i, o));
md.renderer.rules.link_open = (tokens, idx, opts, env, self) => {
  const t = tokens[idx];
  const href = t.attrGet('href') || '';
  if (/youtube\.com\/watch\?v=[\w-]+&t=\d+s?$/.test(href) || /youtu\.be\/[\w-]+\?t=\d+/.test(href)) t.attrJoin('class', 'ts');
  if (/^https?:/.test(href)) { t.attrSet('target', '_blank'); t.attrSet('rel', 'noopener'); }
  return defaultLink(tokens, idx, opts, env, self);
};

// ---- tables get a scroll wrapper
md.renderer.rules.table_open = () => '<div class="table-wrap"><table>';
md.renderer.rules.table_close = () => '</table></div>';

// ---- <div class="tracer" data-trace="NAME" ...></div> → step-through widget (trace made by make_traces.py)
const tracerWidget = (attrs) => {
  const name = attrs.match(/data-trace="([^"]+)"/)[1];
  const T = JSON.parse(fs.readFileSync(path.join(traceDir, name + '.json'), 'utf8'));
  const codeHtml = hl.codeToHtml(T.code, { lang: 'python', theme: 'catppuccin-mocha' });
  TRACES[name] = { call: T.call, viz: T.viz, v0: T.v0, steps: T.steps, names: T.names };
  stats.traces++;
  const setup = T.setup ? `<code class="tr-call" title="set up first">${esc(T.setup)}</code>` : '';
  return `<figure class="tracer" data-trace="${esc(name)}" tabindex="0" aria-label="Step-through of ${esc(T.call)}">
<div class="tr-head"><span class="tr-badge">▶ step through it</span>${setup}<code class="tr-call">${esc(T.call)}</code><span class="tr-count"></span></div>
<div class="tr-grid"><div class="tr-code">${codeHtml}</div>
<div class="tr-side"><div class="tr-stack-wrap"><span class="tr-label">call stack (newest on top)</span><ol class="tr-stack"></ol></div>
<div class="tr-viz" hidden></div>
<div class="tr-out-wrap"><span class="tr-label">output</span><pre class="tr-out"></pre></div></div></div>
<p class="tr-say" aria-live="polite"></p>
<div class="tr-controls"><button type="button" data-act="first" title="back to the start">⏮</button><button type="button" data-act="prev">◀ back</button><button type="button" data-act="next">next ▶</button><button type="button" class="play" data-act="play">▶ play</button><button type="button" data-act="last" title="jump to the end">⏭</button><input type="range" min="0" value="0" aria-label="scrub through the steps"></div>
</figure>`;
};
// quiz cards are written as <details class="quiz"><summary>QUESTION (one line) + a blank line + the answer:
// close the summary at the end of the question line, so the answer stays hidden until the card is opened
const closeSummaries = h => h.replace(/(<details class="quiz"><summary>)([^\n]*)\n/g, (m, open, q) => q.includes('</summary>') ? m : open + md.renderInline(q) + '</summary>\n');
const withTracers = h => h.replace(/<div class="tracer"((?:[^>"]|"[^"]*")*)><\/div>/g, (_, a) => tracerWidget(a));

// ---------------------------------------------------------------------------
const src = fs.readFileSync(mdPath, 'utf8');
const heroM = src.match(/<!--\s*hero:\s*([\s\S]*?)-->/);
const HERO_SUB = heroM ? md.renderInline(heroM[1].trim()) : md.renderInline(CFG.hero_sub || '');
// split into H1 chunks (ignore '# ' inside fences)
const lines = src.split('\n');
const chunks = [];
let inFence = false, cur = [];
for (const line of lines) {
  if (/^```/.test(line)) inFence = !inFence;
  if (!inFence && /^# /.test(line) && cur.length) { chunks.push(cur.join('\n')); cur = []; }
  cur.push(line);
}
chunks.push(cur.join('\n'));

const lectures = [];
let introHtml = '';
for (const chunk of chunks) {
  const metaM = chunk.match(/<!--\s*lecture\s+([^>]*?)-->/);
  if (!metaM) {
    // intro: drop its H1 (the hero shows the title)
    introHtml += md.render(chunk.replace(/^# .*\n/, ''));
    continue;
  }
  const meta = Object.fromEntries([...metaM[1].matchAll(/(\w+)="([^"]*)"/g)].map(x => [x[1], x[2]]));
  const env = {};
  SLUG_PREFIX = `l${meta.n}-`;
  const tokens = md.parse(chunk, env);
  SLUG_PREFIX = '';
  const h2s = [];
  let h1 = null;
  tokens.forEach((tk, i) => {
    if (tk.type === 'heading_open' && (tk.tag === 'h1' || tk.tag === 'h2')) {
      const raw = tokens[i + 1].content;
      const tsM = raw.match(/\[(\d+:\d\d(?::\d\d)?)\]\([^)]*\)/) || raw.match(/<span class="ts nolink"[^>]*>(\d+:\d\d(?::\d\d)?)<\/span>/);
      const text = raw.replace(/\s*\[\d+:\d\d(?::\d\d)?\]\([^)]*\)/g, '').replace(/\s*<span class="ts nolink"[^>]*>[^<]*<\/span>/g, '');   // timestamp chips stay in the heading only
      const vid = (raw.match(/watch\?v=([\w-]+)/) || [])[1];
      const item = { id: tk.attrGet('id'), text, html: md.renderInline(text), t: tsM ? tsM[1] : '', second: !!(vid && vid === meta.video2) };
      if (tk.tag === 'h1' && !h1) h1 = item; else if (tk.tag === 'h2') h2s.push(item);
    }
  });
  let html = md.renderer.render(tokens, md.options, env);
  html = html.replace(/<h1[^>]*>[\s\S]*?<\/h1>\s*/, '');
  html = html.replace(/<p>\s*(<figure class="sketch"[\s\S]*?<\/figure>)\s*<\/p>/g, '$1');
  html = html.replace(/<p>\s*(<figure><img[\s\S]*?<\/figure>)\s*<\/p>/g, '$1');
  html = withTracers(html);
  html = closeSummaries(html);
  stats.quiz += (html.match(/<details class="quiz"/g) || []).length;
  html = html.replace(/<summary>([\s\S]*?)<\/summary>/g, '<summary><span class="qtext">$1</span></summary>');
  lectures.push({ meta, h1, h2s, html });
}
introHtml = withTracers(introHtml.replace(/<p>\s*(<figure class="sketch"[\s\S]*?<\/figure>)\s*<\/p>/g, '$1'));

const total = lectures.filter(L => !L.meta.extra).length;   // the wrap-up chapter is not a lecture
const span = m => { const r = (m.label || '').match(/^(\d+)[–-](\d+)$/); return r ? +r[2] - +r[1] + 1 : 1; };
const nVideos = lectures.filter(L => !L.meta.extra).reduce((k, L) => k + span(L.meta), 0);   // a combined page covers several videos
const numOf = m => m.extra ? 'Σ' : (m.label || m.n);   // label: a page made of two videos, e.g. "5–6"
// on a two-video page, say which video a section's time belongs to ("L6 · 1:59")
// on a page made of two sources (label "5–6"), say which one a section's time belongs to ("P6 · 1:59")
const partOf = (m, h) => { const r = (m.label || '').match(/^(\d+)[–-](\d+)$/); return r ? `${CFG.tab}${h.second ? r[2] : r[1]} · ` : ''; };
const isRange = m => /[–-]/.test(m.label || '');   // project tweak: plural only for range labels like "5–6"
const lecName = m => m.extra ? 'Wrap-up' : (m.label ? (isRange(m) ? CFG.units : CFG.unit) + ' ' + m.label : CFG.unit + ' ' + m.n);
const titleOnly = h => h.html.replace(/^[A-Z][A-Za-z]+ \d+(?:[–-]\d+)? · /, '');
const statusChip = s => s === 'done' ? '<span class="chip ok">notes complete</span>'
  : s === 'preview' ? '<span class="chip draft">✎ drafted from class notes · transcript pending</span>'
  : '<span class="chip wait">transcript pending</span>';

const lecturesHtml = lectures.map(({ meta, h1, h2s, html }, idx) => {
  const n = +meta.n;
  const prev = lectures[idx - 1], next = lectures[idx + 1];
  const pagerLink = (L, dir) => L ? `<a class="pager-link ${dir} c-${COLORS[((+L.meta.n % COLORS.length) + COLORS.length) % COLORS.length]}" href="#l${L.meta.n}"><small>${dir === 'prev' ? '← previous' : 'next →'}</small><span>${lecName(L.meta)} · ${esc(L.meta.short)}</span></a>` : `<a class="pager-link ${dir} home-link" href="#home"><small>${dir === 'prev' ? '← back to' : 'back to →'}</small><span>All ${CFG.units_lower}</span></a>`;
  const pager = `<nav class="pager" aria-label="${CFG.unit} navigation">${pagerLink(prev, 'prev')}${pagerLink(next, 'next')}</nav>`;
  const color = COLORS[((n % COLORS.length) + COLORS.length) % COLORS.length];
  // no video links or timestamps in this series: a small reading-time chip instead
  const words = html.replace(/<pre[\s\S]*?<\/pre>/g, ' ').replace(/<svg[\s\S]*?<\/svg>/g, ' ').replace(/<[^>]+>/g, ' ').split(/\s+/).filter(Boolean).length;
  const mins = Math.max(2, Math.round(words / 200));
  const ytChips = meta.extra
    ? `<span class="chip src">Σ all ${CFG.source_count || nVideos} ${CFG.units_lower} in one place · plus beyond-the-${CFG.source} extras</span><span class="chip src">⏱ ~${mins} min read</span>`
    : `<span class="chip src">⏱ ~${mins} min read</span>`;
  const inThis = h2s.length ? `<div class="in-this"><span class="in-this-label">${meta.extra ? 'In this chapter' : meta.label ? 'On this page' : 'In this ' + CFG.unit_lower}</span><ol>${h2s.map(h => `<li><a href="#${h.id}">${h.html}</a>${h.t ? `<small class="tt">${partOf(meta, h)}${h.t}</small>` : ''}</li>`).join('')}</ol></div>` : '';
  const stamp = meta.status === 'pending' ? '<div class="stamp">coming soon</div>' : meta.status === 'preview' ? '<div class="stamp stamp-blue">preview</div>' : '';
  return `
<section class="lecture view c-${color} status-${meta.status}" id="l${n}" data-n="${n}" aria-label="${lecName(meta)}">
  <header class="cover">
    <div class="tape tape-l"></div><div class="tape tape-r"></div>
    <div class="lec-num${meta.label ? ' lbl' : ''}"><small>${meta.extra ? 'wrap-up' : isRange(meta) ? CFG.units_lower : CFG.unit_lower}</small><b>${numOf(meta)}</b></div>
    ${stamp}
    <p class="kicker">${[meta.extra ? `After all ${total} ${CFG.units_lower}` : lecName(meta), COURSE, meta.kind ? esc(meta.kind) : ''].filter(Boolean).join(' · ')}</p>
    <h1 id="${h1.id}">${titleOnly(h1)}</h1>
    <div class="meta">${ytChips}${statusChip(meta.status)}</div>
    ${inThis}
  </header>
  <div class="lecture-body">${html}</div>
  ${pager}
</section>`;
}).join('\n');

const cardsHtml = `<div class="lec-cards">${lectures.map(({ meta, h2s }) => {
  const n = +meta.n;
  const color = COLORS[((n % COLORS.length) + COLORS.length) % COLORS.length];
  const st = meta.status === 'done' ? `<span class="chip ok">${h2s.length} sections · ready</span>` : meta.status === 'preview' ? `<span class="chip draft">${h2s.length} sections · draft</span>` : '<span class="chip wait">transcript pending</span>';
  return `<a class="lec-card c-${color} status-${meta.status}" href="#l${n}"><span class="lc-num${meta.label ? ' lbl' : ''}">${numOf(meta)}</span><span class="lc-title">${esc(meta.short)}</span>${st}<span class="lc-open">${meta.status === 'pending' ? 'peek →' : 'open page →'}</span></a>`;
}).join('')}</div>`;

const tocHtml = `<ol class="toc-list"><li class="toc-lec toc-home"><a href="#home" data-target="home"><span class="n">★</span><span class="t">Home · all ${CFG.units_lower}</span></a></li>${lectures.map(({ meta, h1, h2s }) => {
  const n = +meta.n;
  const color = COLORS[((n % COLORS.length) + COLORS.length) % COLORS.length];
  return `<li class="toc-lec c-${color} status-${meta.status}"><a href="#l${n}" data-target="l${n}"><span class="n">${numOf(meta)}</span><span class="t">${esc(meta.short)}</span></a>${h2s.length ? `<ol>${h2s.map(h => `<li><a href="#${h.id}" data-target="${h.id}">${h.html}</a></li>`).join('')}</ol>` : ''}</li>`;
}).join('')}</ol>`;

const chipsHtml = lectures.map(({ meta }) => {
  const n = +meta.n;
  return `<a class="tab c-${COLORS[((n % COLORS.length) + COLORS.length) % COLORS.length]} status-${meta.status}" href="#l${n}" title="${esc(meta.short)}">${meta.extra ? 'Σ' : CFG.tab + (meta.label || n)}</a>`;
}).join('');

const F = (p) => fs.readFileSync(new URL('./node_modules/' + p, import.meta.url)).toString('base64');
const fontCss = [
  ['Caveat', '@fontsource-variable/caveat/files/caveat-latin-wght-normal.woff2', '400 700', 'normal'],
  ['Permanent Marker', '@fontsource/permanent-marker/files/permanent-marker-latin-400-normal.woff2', '400', 'normal'],
  ['Nunito', '@fontsource-variable/nunito/files/nunito-latin-wght-normal.woff2', '200 1000', 'normal'],
  ['Nunito', '@fontsource-variable/nunito/files/nunito-latin-wght-italic.woff2', '200 1000', 'italic'],
  ['JetBrains Mono', '@fontsource-variable/jetbrains-mono/files/jetbrains-mono-latin-wght-normal.woff2', '100 800', 'normal'],
  ['Excalifont', '@excalidraw/excalidraw/dist/prod/fonts/Excalifont/Excalifont-Regular-a88b72a24fb54c9f94e3b5fdaa7481c9.woff2', '400', 'normal'],
].map(([fam, file, wt, st]) => `@font-face{font-family:"${fam}";src:url(data:font/woff2;base64,${F(file)}) format("woff2");font-weight:${wt};font-style:${st};font-display:swap}`).join('\n');
let out = fs.readFileSync(tplPath, 'utf8')
  .replace('{{FONTS}}', () => fontCss)
  .replace('{{TOC}}', () => tocHtml)
  .replace('{{CHIPS}}', () => chipsHtml)
  .replace('{{INTRO}}', () => introHtml)
  .replace('{{CARDS}}', () => cardsHtml)
  .replace('{{LECTURES}}', () => lecturesHtml)
  .replaceAll('{{N_LECTURES}}', String(nVideos))
  .replaceAll('{{N_DIAGRAMS}}', String(stats.diagrams))
  .replaceAll('{{N_CODE}}', String(stats.code))
  .replaceAll('{{N_QUIZ}}', String(stats.quiz))
  .replaceAll('{{N_TRACES}}', String(stats.traces))
  .replaceAll('{{N_SHOTS}}', String(stats.shots || 0))
  .replace('{{HERO_SUB}}', () => HERO_SUB)
  .replaceAll('{{N_NOTES}}', String(stats.notes))
  .replace(/\{\{RAW\.(\w+)\}\}/g, (_, k) => String(CFG[k] ?? ''))
  .replace(/\{\{CFG\.(\w+)\}\}/g, (_, k) => esc(CFG[k] ?? ''))
  .replace(/\{\{JS\.(\w+)\}\}/g, (_, k) => JSON.stringify(CFG[k] ?? '').replace(/</g, '\\u003c'));
// Internal links carry no href at all: the preview host treats every <a href> click as
// "leaving", so in-page navigation uses data-go and the router in the template.
out = out.replace(/<a(\s[^>]*?)?\shref="#([^"]*)"([^>]*)>/g, (_, pre = '', id, post) => `<a${pre} data-go="${id}" role="link" tabindex="0"${post}>`);
const excJson = JSON.stringify(EXC).replace(/</g, '\\u003c');
const trJson = JSON.stringify(TRACES).replace(/</g, '\\u003c');
const bodyEnd = out.lastIndexOf('<script>\n(() => {');   // data first, so the page script can read it at start-up
if (bodyEnd < 0) throw new Error('main script not found');
out = out.slice(0, bodyEnd) + `<script type="application/octet-stream" id="exc-data" data-enc="gzip">${zlib.gzipSync(Buffer.from(excJson, 'utf8'), { level: 9 }).toString('base64')}</script>\n<script type="application/json" id="trace-data">${trJson}</script>\n` + out.slice(bodyEnd);
const leftovers = (out.match(/<a\s[^>]*href="#/g) || []).length;
if (leftovers) throw new Error(leftovers + ' internal href links left');
fs.writeFileSync(outPath, out);
console.log('built', outPath, (out.length / 1024).toFixed(0) + 'KB', stats);

import { launch } from './browser.mjs';
const [url, outPrefix, w, h, dark, ...sels] = process.argv.slice(2);
const b = await launch();
const p = await b.newPage({ viewport: { width: +w, height: +h }, colorScheme: dark === '1' ? 'dark' : 'light' });
p.on('pageerror', e => console.error('PAGEERR', e.message));
await p.goto(url, { waitUntil: 'load' });
await p.waitForTimeout(1500);
const sw = await p.evaluate(() => [document.documentElement.scrollWidth, innerWidth, document.documentElement.scrollHeight]);
console.log('scrollWidth/innerWidth/height', sw);
let i = 0;
for (const sel of sels) {
  if (sel.startsWith('y=')) await p.evaluate(y => window.scrollTo({top:+y,behavior:'instant'}), sel.slice(2));
  else await p.evaluate(s => { const el = document.querySelector(s); if (el) { el.scrollIntoView({block:'start',behavior:'instant'}); window.scrollBy({top:-90,behavior:'instant'}); } else console.log('missing', s); }, sel);
  await p.waitForTimeout(400);
  await p.screenshot({ path: `${outPrefix}-${i++}.png` });
}
// overflow check: elements wider than viewport
const wide = await p.evaluate(() => [...document.querySelectorAll('.page *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > innerWidth + 1 && !e.closest('.sketch-scroll,.table-wrap,pre,.tabs,.output'); }).slice(0,8).map(e => e.tagName + '.' + e.className + ' ' + Math.round(e.getBoundingClientRect().right)));
console.log('overflowing:', wide);
await b.close();

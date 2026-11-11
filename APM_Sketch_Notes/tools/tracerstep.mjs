import { launch } from './browser.mjs';
const [url, out, n, sel='.tracer', w='1300', clickSel=''] = process.argv.slice(2);
const b = await launch();
const p = await b.newPage({ viewport: { width: +w, height: 900 } });
p.on('pageerror', e => console.error('PAGEERR', e.message));
await p.goto(url); await p.waitForTimeout(1200);
const fig = await p.$(sel);
await fig.scrollIntoViewIfNeeded();
if (clickSel) { await p.click(clickSel); await p.waitForTimeout(300); }
for (let i = 0; i < +n; i++) { await fig.$eval('[data-act=next]', b => b.click()); await p.waitForTimeout(40); }
await p.waitForTimeout(600);
await fig.screenshot({ path: out });
console.log(await fig.$eval('.tr-count', e => e.textContent), '|', await fig.$eval('.tr-say', e => e.textContent));
await b.close();

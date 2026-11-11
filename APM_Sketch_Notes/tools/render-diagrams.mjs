// Usage: node render-diagrams.mjs <inDir> <outDir>
// Renders Excalidraw skeleton JSON files -> real Excalidraw SVG (+ .excalidraw source)
import { launch } from './browser.mjs';
import fs from 'fs'; import path from 'path'; import http from 'http';
const [inDir, outDir, prefix = ''] = process.argv.slice(2);   // optional prefix: render only files starting with it (e.g. l7-)
fs.mkdirSync(outDir, { recursive: true });
const root = path.resolve('.');
const mime = { '.js':'text/javascript', '.html':'text/html', '.woff2':'font/woff2', '.css':'text/css', '.json':'application/json' };
const server = http.createServer((req, res) => {
  const p = path.join(root, decodeURIComponent(req.url.split('?')[0]));
  if (!p.startsWith(root) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': mime[path.extname(p)] || 'application/octet-stream', 'Access-Control-Allow-Origin': '*' });
  fs.createReadStream(p).pipe(res);
}).listen(0);
await new Promise(r => server.once('listening', r));
const PORT = server.address().port;
const browser = await launch();
const page = await browser.newPage();
page.on('pageerror', e => console.error('PAGEERR', e.message));
await page.goto(`http://localhost:${PORT}/exc-page.html`);
await page.waitForFunction(() => window.__ready === true, null, { timeout: 60000 });
const files = fs.readdirSync(inDir).filter(f => f.endsWith('.json') && f.startsWith(prefix)).sort();
for (const f of files) {
  const skel = JSON.parse(fs.readFileSync(path.join(inDir, f), 'utf8')).filter(e => !['cameraUpdate','delete','restoreCheckpoint'].includes(e.type));
  // default hand-drawn font (Excalifont = 5)
  for (const e of skel) { if (e.type === 'text' && e.fontFamily == null) e.fontFamily = 5; if (e.label && e.label.fontFamily == null) e.label.fontFamily = 5; }
  try {
    const { svg, elements } = await page.evaluate(async s => await window.renderScene(s), skel);
    const base = f.replace(/\.json$/, '');
    fs.writeFileSync(path.join(outDir, base + '.svg'), svg);
    fs.writeFileSync(path.join(outDir, base + '.excalidraw'), JSON.stringify({ type: 'excalidraw', version: 2, source: 'https://excalidraw.com', elements, appState: { viewBackgroundColor: '#ffffff' }, files: {} }, null, 1));
    console.log('rendered', base, (svg.length/1024).toFixed(0) + 'KB');
  } catch (err) { console.error('FAILED', f, err.message); }
}
await browser.close(); server.close();

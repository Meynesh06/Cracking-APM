// Find a Chromium for playwright-core on any machine (cloud sandbox, Linux, macOS, Windows).
// Order: $DKFILE_CHROME → the sandbox's /opt/pw-browsers → Playwright's own cache → an installed Chrome/Chromium.
// If nothing is found: run `npx playwright-core install chromium` in the toolkit's engine folder.
import { chromium } from 'playwright-core';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const exists = p => { try { return p && fs.statSync(p).isFile(); } catch { return false; } };
const globDirs = (root, re) => { try { return fs.readdirSync(root).filter(d => re.test(d)).sort().reverse().map(d => path.join(root, d)); } catch { return []; } };

export function findChrome() {
  if (exists(process.env.DKFILE_CHROME)) return process.env.DKFILE_CHROME;
  const cands = [];
  const caches = ['/opt/pw-browsers', process.env.PLAYWRIGHT_BROWSERS_PATH,
    path.join(os.homedir(), '.cache', 'ms-playwright'),
    path.join(os.homedir(), 'Library', 'Caches', 'ms-playwright'),
    path.join(process.env.LOCALAPPDATA || '', 'ms-playwright')].filter(Boolean);
  for (const c of caches) {
    for (const d of globDirs(c, /^chromium_headless_shell-\d+$/)) {
      cands.push(path.join(d, 'chrome-linux', 'headless_shell'), path.join(d, 'chrome-headless-shell-linux64', 'chrome-headless-shell'),
        path.join(d, 'chrome-mac', 'headless_shell'), path.join(d, 'chrome-headless-shell-mac-arm64', 'chrome-headless-shell'),
        path.join(d, 'chrome-headless-shell-mac-x64', 'chrome-headless-shell'), path.join(d, 'chrome-win', 'headless_shell.exe'));
    }
    for (const d of globDirs(c, /^chromium-\d+$/)) {
      cands.push(path.join(d, 'chrome-linux', 'chrome'), path.join(d, 'chrome-linux64', 'chrome'),
        path.join(d, 'chrome-mac', 'Chromium.app', 'Contents', 'MacOS', 'Chromium'),
        path.join(d, 'chrome-mac-arm64', 'Google Chrome for Testing.app', 'Contents', 'MacOS', 'Google Chrome for Testing'),
        path.join(d, 'chrome-win', 'chrome.exe'));
    }
    cands.push(path.join(c, 'chromium'));
  }
  cands.push('/usr/bin/chromium', '/usr/bin/chromium-browser', '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Chromium.app/Contents/MacOS/Chromium',
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe');
  return cands.find(exists) || null;
}

export async function launch(opts = {}) {
  const exe = findChrome();
  const args = ['--disable-background-networking', '--no-first-run', '--disable-component-update', ...(opts.args || [])];
  if (exe) return chromium.launch({ ...opts, executablePath: exe, args });
  try { return await chromium.launch({ ...opts, args }); }                       // playwright's default location
  catch (e) {
    throw new Error('No Chromium found. Set DKFILE_CHROME=/path/to/chrome, or run `npx playwright-core install chromium` '
      + 'in the dkfile toolkit engine folder.\n' + e.message);
  }
}

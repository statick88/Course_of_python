const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const { chromium } = require(process.argv[2]);
const root = path.resolve(process.argv[3]);
const pages = JSON.parse(fs.readFileSync(process.argv[4], 'utf8'));
const browserPath = process.argv[5] || undefined;

const server = http.createServer((request, response) => {
  const file = path.resolve(root, `.${decodeURIComponent(request.url.split('?')[0])}`);
  if (!file.startsWith(`${root}${path.sep}`) || !fs.existsSync(file) || !fs.statSync(file).isFile()) {
    response.writeHead(404).end();
    return;
  }
  response.setHeader('Content-Type', path.extname(file) === '.js' ? 'text/javascript' : 'text/html');
  response.end(fs.readFileSync(file));
});

(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  let browser;
  const report = { pages: [], errors: [] };
  try {
    browser = await chromium.launch({ headless: true, executablePath: browserPath });
    const page = await browser.newPage();
    page.on('pageerror', error => report.errors.push(error.message));
    for (const file of pages) {
      const response = await page.goto(`http://127.0.0.1:${server.address().port}/${file}`, { waitUntil: 'networkidle' });
      assert.equal(response.status(), 200, file);
      const quiz = page.locator('.quizdown');
      assert.ok(await quiz.count() >= 1, `missing quiz host: ${file}`);
      await quiz.first().locator('input, button').first().waitFor({ state: 'attached', timeout: 8000 });
      report.pages.push(file);
    }
    assert.deepEqual(report.errors, []);
    console.log(JSON.stringify(report));
  } finally {
    if (browser) await browser.close();
    server.close();
  }
})().catch(error => { console.error(error.stack); process.exit(1); });

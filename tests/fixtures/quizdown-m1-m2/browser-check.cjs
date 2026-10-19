const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const { chromium } = require(process.argv[2]);
const root = path.resolve(process.argv[3]);
const expected = JSON.parse(fs.readFileSync(process.argv[4], 'utf8'));
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
  const report = { questions: [], errors: [] };
  try {
    browser = await chromium.launch({ headless: true, executablePath: browserPath });
    const page = await browser.newPage();
    page.on('pageerror', error => report.errors.push(error.message));
    const response = await page.goto(`http://127.0.0.1:${server.address().port}/quiz.html`, { waitUntil: 'networkidle' });
    assert.equal(response.status(), 200);
    const quiz = page.locator('.quizdown');
    assert.equal(await quiz.count(), 1);
    await quiz.locator('input').first().waitFor({ state: 'attached', timeout: 8000 });

    for (const incorrectFirst of [false, true]) {
      const seen = new Set();
      for (let index = 0; index < expected.length; index += 1) {
        const title = await quiz.locator('h1,h2,h3,h4,h5,h6').allTextContents();
        const question = expected.find(item => title.join(' ').includes(item.title));
        assert.ok(question, `unknown question: ${title.join(' ')}`);
        assert.ok(!seen.has(question.title), `repeated question: ${question.title}`);
        seen.add(question.title);
        const chosen = incorrectFirst && index === 0
          ? question.answers.filter(answer => !question.correct.includes(answer)).slice(0, 1)
          : question.correct;
        for (const answer of chosen) {
          const escaped = answer.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\s+/g, '\\s+');
          const label = quiz.locator('label').filter({ hasText: new RegExp(`^\\s*${escaped}\\s*$`) });
          const visibleLabels = await quiz.locator('label').allTextContents();
          assert.equal(await label.count(), 1, `missing/ambiguous answer: ${answer}; visible: ${visibleLabels.join(' | ')}`);
          await label.click();
          assert.ok(await label.locator('input').isChecked(), `answer not selected: ${answer}`);
        }
        report.questions.push(title.join(' '));
        await quiz.getByRole('button', { name: index + 1 === expected.length ? 'Evaluate' : 'Next', exact: true }).click();
      }
      const score = `${String(expected.length - Number(incorrectFirst)).padStart(2, '0')}/${String(expected.length).padStart(2, '0')}`;
      await quiz.getByRole('heading', { name: score, exact: true }).waitFor({ state: 'visible', timeout: 8000 });
      assert.equal(seen.size, expected.length);
      await quiz.getByRole('button', { name: 'One more time!', exact: true }).click();
      await quiz.locator('input').first().waitFor({ state: 'attached', timeout: 8000 });
      assert.equal(await quiz.locator('input:checked').count(), 0);
    }
    assert.deepEqual(report.errors, []);
    console.log(JSON.stringify(report));
  } finally {
    if (browser) await browser.close();
    server.close();
  }
})().catch(error => { console.error(error.stack); process.exit(1); });

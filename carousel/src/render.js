// Render a carousel HTML page to one 8640x1350 panorama PNG.
// usage: node render.js [carousel.html] [../out/panorama.png]
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
const html = path.resolve(__dirname, process.argv[2] || 'carousel.html');
const out = path.resolve(__dirname, process.argv[3] || '../out/panorama.png');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 8640, height: 1350 }, deviceScaleFactor: 1 });
  await page.goto('file://' + html, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  await page.locator('#canvas').screenshot({ path: out });
  await browser.close();
})();

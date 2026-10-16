// Render carousel.html to one 8640x1350 panorama PNG.
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' in process.env ? undefined : undefined });
  const page = await browser.newPage({ viewport: { width: 8640, height: 1350 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.resolve(__dirname, 'carousel.html'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  await page.locator('#canvas').screenshot({ path: path.resolve(__dirname, '../out/panorama.png') });
  await browser.close();
})();

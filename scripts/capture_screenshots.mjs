import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { mkdir } from 'node:fs/promises';

await mkdir('artifacts/screenshots', { recursive: true });
const server = spawn('python', ['-m', 'http.server', '4173', '--bind', '127.0.0.1'], { stdio: 'ignore' });
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
let browser;
try {
  await sleep(1200);
  browser = await chromium.launch({ headless: true });
  for (const viewport of [{ name: 'desktop', width: 1440, height: 1000 }, { name: 'mobile', width: 390, height: 844 }]) {
    const page = await browser.newPage({ viewport: { width: viewport.width, height: viewport.height }, deviceScaleFactor: 1 });
    await page.goto('http://127.0.0.1:4173/index.html', { waitUntil: 'networkidle' });
    await page.screenshot({ path: `artifacts/screenshots/home-${viewport.name}.png`, fullPage: true });
    await page.goto('http://127.0.0.1:4173/store.html', { waitUntil: 'networkidle' });
    await page.screenshot({ path: `artifacts/screenshots/store-${viewport.name}.png`, fullPage: true });
    if (viewport.name === 'desktop') {
      await page.getByRole('button', { name: /\+ Keranjang/ }).first().click();
      if ((await page.locator('#cartCount').innerText()) !== '1') throw new Error('Cart add-item check failed');
      await page.getByRole('button', { name: /Lanjut checkout/ }).click();
      await page.locator('#buyerName').fill('Demo Buyer');
      await page.locator('#buyerPhone').fill('081234567890');
      await page.getByRole('button', { name: /Buat pesanan demo/ }).click();
      if (!(await page.locator('#txnId').innerText()).startsWith('NX-')) throw new Error('Transaction ID check failed');
      if ((await page.locator('#timer').innerText()) !== '10:00') throw new Error('Checkout timer check failed');
      await page.screenshot({ path: 'artifacts/screenshots/checkout-demo-desktop.png', fullPage: true });
    }
    await page.close();
  }
  console.log('PASS: desktop/mobile screenshots captured; cart, checkout ID, and 10-minute timer verified.');
} finally {
  if (browser) await browser.close();
  server.kill('SIGTERM');
}

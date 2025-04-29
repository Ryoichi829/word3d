import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto('https://word3d-b55mwlmtulmgspme2njkxc.streamlit.app/')

        # ページ全体ロード完了を待つ
        await page.wait_for_load_state('networkidle')

        # （何も押さない！アクセスするだけ）
        await page.wait_for_timeout(5000)  # 少しだけ待機して安定化

        await browser.close()

asyncio.run(run())

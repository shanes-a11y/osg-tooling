import asyncio
import sys
from playwright.async_api import async_playwright

URL = "https://osgboutiquehunter.streamlit.app"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        )

        print(f"Visiting {URL}...")
        await page.goto(URL, wait_until="domcontentloaded", timeout=120_000)
        await page.wait_for_timeout(8000)

        content = await page.inner_text("body")

        if "Oh no" in content or "Error running app" in content:
            print(f"FAIL: App is in an error state.\n{content[:500]}")
            await browser.close()
            sys.exit(1)

        print("OK: App is awake.")
        await browser.close()


asyncio.run(main())

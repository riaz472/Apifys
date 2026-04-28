from apify import Actor
from playwright.async_api import async_playwright
import asyncio

async def run_bot(browser_type):
    url = "https://abr.ge/zz4y46"
    async with browser_type.launch(headless=True, args=["--no-sandbox"]) as browser:
        context = await browser.new_context(viewport={'width': 375, 'height': 667})
        page = await context.new_page()
        try:
            Actor.log.info(f"Visiting: {url}")
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            await asyncio.sleep(5) # Ads load hone ka wait
            
            Actor.log.info("Clicking Ad area...")
            await page.mouse.click(180, 330)
            
            Actor.log.info("Staying for 30s to register view...")
            await asyncio.sleep(30)
            Actor.log.info("Cycle complete. Restarting...")
        except Exception as e:
            Actor.log.error(f"Error in cycle: {e}")
        finally:
            await browser.close()

async def main():
    async with Actor:
        Actor.log.info("=== INFINITE LOOP STARTED ===")
        async with async_playwright() as p:
            # Ye loop kabhi nahi rukega jab tak aap 'Abort' nahi dabate
            while True:
                await run_bot(p.chromium)
                # 10 second ka break taaki server block na kare
                await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())

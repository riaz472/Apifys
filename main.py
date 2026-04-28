from apify import Actor
from playwright.async_api import async_playwright
import asyncio

async def main():
    async with Actor:
        url = "https://abr.ge/zz4y46"
        Actor.log.info("Starting bot in safe mode...")

        async with async_playwright() as p:
            # Extra arguments for Apify/Docker environment
            browser = await p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
            )
            
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Linux; Android 13) Chrome/122.0.0.0 Mobile"
            )
            page = await context.new_page()

            try:
                Actor.log.info(f"Opening URL: {url}")
                # Timeout barha diya hai taaki slow loading par error na aaye
                await page.goto(url, wait_until="domcontentloaded", timeout=90000)
                
                Actor.log.info("Page loaded! Performing human-like actions...")
                await asyncio.sleep(5)
                
                # Screen ke beech mein click
                await page.mouse.click(200, 400)
                
                Actor.log.info("Waiting 50 seconds for ad registration...")
                await asyncio.sleep(50)
                
                Actor.log.info("Mission Successful!")

            except Exception as e:
                Actor.log.error(f"Error occurred: {e}")
            finally:
                await browser.close()

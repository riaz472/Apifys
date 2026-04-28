from apify import Actor
from playwright.async_api import async_playwright
import asyncio
import random

async def main():
    async with Actor:
        # Aapka link aur keyword
        url = "https://abr.ge/zz4y46"
        keyword = "riazinvest" # Asli lagne ke liye search keyword

        Actor.log.info("Bot starting... using GitHub source for reliability.")

        async with async_playwright() as p:
            # Har baar fresh browser instance (Cookies/Cache auto-clear)
            browser = await p.chromium.launch(headless=True)
            
            # Mobile View Simulation (S901B model)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile",
                viewport={'width': 390, 'height': 844}
            )
            page = await context.new_page()

            try:
                # STEP 1: Google Search bypass (Traffic Quality high karne ke liye)
                Actor.log.info("Bypassing via Google Search...")
                await page.goto("https://www.google.com")
                await page.wait_for_timeout(2000)
                
                # STEP 2: Target Link par jana
                Actor.log.info(f"Navigating to: {url}")
                await page.goto(url, wait_until="networkidle", timeout=60000)
                
                # STEP 3: HUMAN-LIKE CLICKS (Ads trigger karne ke liye)
                # Yeh page par 3 alag-alag random spots par click karega
                for i in range(3):
                    x = random.randint(50, 350)
                    y = random.randint(150, 600)
                    await page.mouse.click(x, y)
                    Actor.log.info(f"Click {i+1} performed at {x}, {y}")
                    await asyncio.sleep(random.randint(2, 5))

                # STEP 4: STAY TIME (Wait taaki click register ho)
                # 50 seconds ka stay taaki ad revenue count ho
                Actor.log.info("Staying for 50 seconds to ensure ad load...")
                await asyncio.sleep(50)
                
                Actor.log.info("Mission Successful: Click & View Registered!")

            except Exception as e:
                Actor.log.error(f"Something went wrong: {e}")
            finally:
                await browser.close()

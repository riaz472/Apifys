from apify import Actor
from playwright.async_api import async_playwright
import asyncio

async def run_bot(browser_type):
    url = "https://abr.ge/zz4y46"
    # Yahan 'await' ka izafa kiya gaya hai jo error khatam kar dega
    browser = await browser_type.launch(headless=True, args=["--no-sandbox"])
    
    try:
        context = await browser.new_context(viewport={'width': 375, 'height': 667})
        page = await context.new_page()
        
        Actor.log.info(f"Visiting: {url}")
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(5) 
        
        Actor.log.info("Clicking Ad area...")
        await page.mouse.click(180, 330)
        
        Actor.log.info("Staying for 30s...")
        await asyncio.sleep(30)
        Actor.log.info("Cycle complete.")
        
    except Exception as e:
        Actor.log.error(f"Error in cycle: {e}")
    finally:
        await browser.close()

async def main():
    async with Actor:
        Actor.log.info("=== INFINITE LOOP STARTED ===")
        async with async_playwright() as p:
            while True:
                # Har cycle ke baad browser band ho kar naya khulega
                await run_bot(p.chromium)
                
                Actor.log.info("Waiting 10s before next cycle...")
                await asyncio.sleep(10)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

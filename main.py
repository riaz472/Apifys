from apify import Actor
from playwright.async_api import async_playwright

async def main():
    async with Actor:
        # Aapka target link
        url = "https://abr.ge/zz4y46"
        
        Actor.log.info(f"Bot shuru ho raha hai... Target: {url}")

        async with async_playwright() as p:
            # Browser configuration
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            )
            page = await context.new_page()

            try:
                Actor.log.info("Page khul raha hai...")
                await page.goto(url, wait_until="networkidle", timeout=60000)
                
                Actor.log.info("Page load ho gaya. 5 seconds wait...")
                await page.wait_for_timeout(5000)

                # Screen ke darmiyan click (Ad trigger karne ke liye)
                Actor.log.info("Click perform kar rahe hain...")
                await page.mouse.click(250, 400) 

                # 50 seconds stay taaki view count ho
                Actor.log.info("Wait kar rahe hain (50s) view register karne ke liye...")
                await page.wait_for_timeout(50000)

                Actor.log.info("Mission Successful! View register ho chuka hoga.")

            except Exception as e:
                Actor.log.error(f"Error: {str(e)}")
            finally:
                await browser.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

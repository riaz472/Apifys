from apify import Actor
from playwright.async_api import async_playwright

async def main():
    async with Actor:
        url = "https://abr.ge/zz4y46"
        Actor.log.info("Starting Fast-Mode Bot...")

        async with async_playwright() as p:
            # Memory bachane ke liye extra arguments
            browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
            context = await browser.new_context(viewport={'width': 375, 'height': 667}) # Mobile size (kam RAM khata hai)
            page = await context.new_page()

            try:
                # Page load hone ka wait (sirf 30s timeout)
                Actor.log.info(f"Navigating to: {url}")
                await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                
                # 5 second ka wait ads load hone ke liye
                await page.wait_for_timeout(5000)

                # Pakka Click (Center of screen)
                Actor.log.info("Performing click...")
                await page.mouse.click(180, 330)

                # Sirf 25-30 second mazeed rukna hai
                Actor.log.info("Staying for 25s...")
                await page.wait_for_timeout(25000)

                Actor.log.info("Done! Closing to save resources.")

            except Exception as e:
                Actor.log.error(f"Error: {str(e)}")
            finally:
                await browser.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()

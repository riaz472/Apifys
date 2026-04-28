import requests
import time
from apify import Actor

def main():
    with Actor:
        url = "https://abr.ge/zz4y46"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        Actor.log.info(f"Bot starting... Targeting: {url}")

        try:
            # Link ko hit karna
            response = requests.get(url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                Actor.log.info("Link hit successful! Status 200.")
                Actor.log.info("Waiting 60 seconds to simulate human view...")
                time.sleep(60) # Clicks aur views count hone ka time
                Actor.log.info("Mission Successful! View registered.")
            else:
                Actor.log.error(f"Failed to load. Status code: {response.status_code}")

        except Exception as e:
            Actor.log.error(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()

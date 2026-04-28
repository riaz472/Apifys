# Step 1: Use official Apify Python image with Playwright
FROM apify/actor-python-playwright-chrome:latest

# Step 2: Copy all files
COPY . ./

# Step 3: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Install Playwright Browsers (Ye sabse zaroori line hai)
RUN playwright install chromium

# Step 5: Start the bot
CMD ["python3", "main.py"]

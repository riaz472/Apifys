# Step 1: Apify ka official Python Playwright image use karein
FROM apify/actor-python-playwright-chrome:latest

# Step 2: Apni files copy karein
COPY . ./

# Step 3: Requirements install karein
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Playwright browsers ko install aur verify karein
# Ye step sabse zaroori hai browser launch error khatam karne ke liye
RUN playwright install chromium

# Step 5: Bot ko run karne ki command
CMD ["python3", "main.py"]

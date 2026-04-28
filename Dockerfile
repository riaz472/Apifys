FROM apify/actor-python-playwright-chrome:latest

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

# Browser install karna lazmi hai
RUN playwright install chromium

CMD ["python3", "main.py"]

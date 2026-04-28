FROM apify/actor-python-playwright-chrome:latest

# Files copy karein
COPY . ./

# Dependencies install karein
RUN pip install -r requirements.txt

# Bot shuru karne ki command
CMD ["python3", "main.py"]

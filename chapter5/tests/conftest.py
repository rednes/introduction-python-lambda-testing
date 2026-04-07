import os

PAYMENT_API_URL = "https://api.example.com/payments"

os.environ["PAYMENT_API_URL"] = PAYMENT_API_URL
os.environ["PAYMENT_API_TIMEOUT"] = "5"

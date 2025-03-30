import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
CAPTCHA_API_KEY = os.getenv("CAPTCHA_API_KEY")
SMS_API_KEY = os.getenv("SMS_API_KEY")

# Proxy Credentials
PROXY_USERNAME = os.getenv("PROXY_USER")
PROXY_PASSWORD = os.getenv("PROXY_PASS")
PROXY_DOMAIN = os.getenv("PROXY_DOMAIN", "p.webshare.io")  # Default value if missing
PROXY_PORT = os.getenv("PROXY_PORT", "80")  # Default value if missing

# Construct Proxy URL
PROXY = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_DOMAIN}:{PROXY_PORT}"

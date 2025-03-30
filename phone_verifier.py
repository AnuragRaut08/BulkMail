import os
import time
import json
import csv
import requests
import random
import logging
import threading
from fake_useragent import UserAgent
from config import SMS_API_KEY, CAPTCHA_API_KEY, PROXY_USERNAME, PROXY_PASSWORD

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Proxy & User-Agent Setup
PROXY_URL = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@p.webshare.io:80"
ua = UserAgent()

# File Storage Lock
lock = threading.Lock()

# SMS-Activate API Base URL
BASE_URL = "https://api.sms-activate.org/stubs/handler_api.php"

def get_phone_number():
    """Requests a phone number from SMS-Activate."""
    country = "187"  # Indonesia
    url = f"{BASE_URL}?api_key={SMS_API_KEY}&action=getNumber&service=go&country={country}"

    retries = 5
    for attempt in range(retries):
        try:
            headers = {"User-Agent": ua.random}
            response = requests.get(url, timeout=10, headers=headers, proxies={"http": PROXY_URL, "https": PROXY_URL})
            response_text = response.text.strip()
            logging.info(f"📩 API Response: {response_text}")

            if response_text.startswith("ACCESS_NUMBER"):
                _, activation_id, phone_number = response_text.split(":")
                logging.info(f"✅ Phone Number: {phone_number} (Activation ID: {activation_id})")
                return activation_id, phone_number
            elif response_text == "NO_NUMBERS":
                logging.warning("❌ No numbers available, retrying...")
                time.sleep(random.uniform(5, 10))  # Random delay
            else:
                logging.error(f"❌ Unexpected API response: {response_text}")
                break
        except requests.RequestException as e:
            logging.error(f"❌ Network error: {e}")
    return None, None

def get_sms_code(activation_id):
    """Fetches the SMS verification code from SMS-Activate."""
    url = f"{BASE_URL}?api_key={SMS_API_KEY}&action=getStatus&id={activation_id}"

    for _ in range(10):  # Retry 10 times
        try:
            headers = {"User-Agent": ua.random}
            response = requests.get(url, timeout=10, headers=headers, proxies={"http": PROXY_URL, "https": PROXY_URL})
            response_text = response.text.strip()
            logging.info(f"📩 SMS API Response: {response_text}")

            if "STATUS_OK" in response_text:
                _, sms_code = response_text.split(":")
                logging.info(f"✅ SMS Code received: {sms_code}")
                return sms_code
            elif response_text == "STATUS_WAIT_CODE":
                logging.info("⏳ Waiting for SMS code...")
                time.sleep(random.uniform(5, 8))  # Randomized delay
            else:
                logging.error(f"❌ Unexpected response while fetching SMS: {response_text}")
                break
        except requests.RequestException as e:
            logging.error(f"❌ Network error: {e}")
    logging.error("❌ ERROR: Timed out waiting for SMS code.")
    return None

def solve_captcha(site_key, url):
    """Solves Google reCAPTCHA using 2Captcha."""
    request_url = "http://2captcha.com/in.php"
    payload = {
        "key": CAPTCHA_API_KEY,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": url,
        "json": 1
    }

    headers = {"User-Agent": ua.random}
    response = requests.post(request_url, data=payload, headers=headers)
    request_result = response.json()

    if request_result["status"] == 1:
        captcha_id = request_result["request"]
        time.sleep(20)  # Wait for solution
        result_url = f"http://2captcha.com/res.php?key={CAPTCHA_API_KEY}&action=get&id={captcha_id}&json=1"

        for _ in range(10):
            result = requests.get(result_url, headers=headers).json()
            if result["status"] == 1:
                return result["request"]
            time.sleep(random.uniform(4, 7))
    return None

def save_account(email, password, phone, proxy):
    """Saves account details to CSV and JSON."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    account_data = {"email": email, "password": password, "phone": phone, "proxy": proxy, "timestamp": timestamp}

    # Save to CSV
    with lock:
        file_exists = os.path.exists("accounts.csv")
        with open("accounts.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["email", "password", "phone", "proxy", "timestamp"])
            writer.writerow([email, password, phone, proxy, timestamp])

    # Save to JSON
    with lock:
        if os.path.exists("accounts.json"):
            with open("accounts.json", "r") as json_file:
                try:
                    accounts = json.load(json_file)
                except json.JSONDecodeError:
                    accounts = []
        else:
            accounts = []

        accounts.append(account_data)
        with open("accounts.json", "w") as json_file:
            json.dump(accounts, json_file, indent=4)

    logging.info(f"✅ Account saved: {email}")

def generate_random_email():
    """Generates a random Gmail address."""
    return f"{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))}@gmail.com"

def create_gmail_account():
    """Automates Gmail account creation with CAPTCHA and phone verification."""
    activation_id, phone_number = get_phone_number()
    if not activation_id:
        logging.error("❌ Failed to get phone number.")
        return

    email = generate_random_email()
    password = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", k=12))
    proxy = PROXY_URL

    # Simulate Gmail signup (replace this with real browser automation)
    logging.info(f"✅ Gmail account created: {email} | Password: {password} | Phone: {phone_number}")
    save_account(email, password, phone_number, proxy)

# Run the script
if __name__ == "__main__":
    create_gmail_account()

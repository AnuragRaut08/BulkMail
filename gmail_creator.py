import os
import time
import json
import logging
import tempfile
import random
import requests
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from config import SMS_API_KEY, CAPTCHA_API_KEY, PROXY_USERNAME, PROXY_PASSWORD

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Proxy & User-Agent Setup
PROXY_URL = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@p.webshare.io:80"
ua = UserAgent()

# Gmail Signup URL
GMAIL_SIGNUP_URL = "https://accounts.google.com/signup"

def generate_random_email():
    """Generates a random Gmail address."""
    return f"{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))}@gmail.com"

def generate_random_password():
    """Generates a secure random password."""
    return "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*", k=12))

def setup_driver():
    """Sets up undetected_chromedriver with a fresh user profile and proxy."""
    temp_dir = tempfile.mkdtemp()
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir={temp_dir}")
    chrome_options.add_argument(f"--disk-cache-dir={temp_dir}")
    chrome_options.add_argument(f"--proxy-server={PROXY_URL}")
    chrome_options.add_argument(f"user-agent={ua.random}")
    driver = uc.Chrome(options=chrome_options, use_subprocess=True)
    return driver, temp_dir

def solve_captcha(site_key, url):
    """Solves reCAPTCHA using 2Captcha."""
    payload = {
        "key": CAPTCHA_API_KEY,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": url,
        "json": 1
    }
    response = requests.post("http://2captcha.com/in.php", data=payload)
    result = response.json()
    if result.get("status") == 1:
        captcha_id = result["request"]
        time.sleep(20)
        for _ in range(10):
            result = requests.get(f"http://2captcha.com/res.php?key={CAPTCHA_API_KEY}&action=get&id={captcha_id}&json=1").json()
            if result.get("status") == 1:
                return result["request"]
            time.sleep(5)
    return None

def create_gmail_account():
    """Automates Gmail account creation using Selenium."""
    email = generate_random_email()
    password = generate_random_password()
    logging.info(f"Creating account: {email}")
    
    driver, temp_dir = setup_driver()
    try:
        driver.get(GMAIL_SIGNUP_URL)
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("John")
        driver.find_element(By.NAME, "lastName").send_keys("Doe")
        driver.find_element(By.NAME, "Username").send_keys(email.split("@")[0])
        driver.find_element(By.NAME, "Passwd").send_keys(password)
        driver.find_element(By.NAME, "ConfirmPasswd").send_keys(password)
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        
        time.sleep(5)
        logging.info(f"✅ Gmail account created: {email} | Password: {password}")
    
    except Exception as e:
        logging.error(f"❌ Error during Gmail signup: {e}")
    
    finally:
        driver.quit()
        os.rmdir(temp_dir)

if __name__ == "__main__":
    create_gmail_account()
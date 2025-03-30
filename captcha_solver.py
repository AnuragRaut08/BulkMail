import requests
import time
from config import CAPTCHA_API_KEY

def solve_captcha(site_key, page_url):
    url = "http://2captcha.com/in.php"
    data = {"key": CAPTCHA_API_KEY, "method": "userrecaptcha", "googlekey": site_key, "pageurl": page_url, "json": 1}
    response = requests.post(url, data=data).json()

    if response.get("status") != 1:
        return None
    request_id = response.get("request")

    # Wait and retry
    time.sleep(20)  
    result_url = f"http://2captcha.com/res.php?key={CAPTCHA_API_KEY}&action=get&id={request_id}&json=1"
    
    for _ in range(10):  
        result = requests.get(result_url).json()
        if result.get("status") == 1:
            return result.get("request")
        time.sleep(5)
    return None


#new 

import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

TWO_CAPTCHA_API_KEY = os.getenv("TWO_CAPTCHA_API_KEY")

def solve_captcha(site_key, page_url):
    """Solve reCAPTCHA using 2Captcha API"""
    session = requests.Session()
    
    # Step 1: Request CAPTCHA solving
    response = session.post("http://2captcha.com/in.php", {
        "key": TWO_CAPTCHA_API_KEY,
        "method": "userrecaptcha",
        "googlekey": site_key,
        "pageurl": page_url,
        "json": 1
    }).json()
    
    if response.get("status") != 1:
        print("Error sending CAPTCHA:", response)
        return None
    
    captcha_id = response.get("request")
    
    # Step 2: Wait for CAPTCHA solution
    time.sleep(15)  # Wait before fetching solution
    for _ in range(10):  # Retry 10 times
        solution_response = session.get(f"http://2captcha.com/res.php?key={TWO_CAPTCHA_API_KEY}&action=get&id={captcha_id}&json=1").json()
        
        if solution_response.get("status") == 1:
            return solution_response.get("request")
        
        time.sleep(5)  # Wait before retrying

    print("CAPTCHA solving failed.")
    return None

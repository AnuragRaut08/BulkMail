import random
import requests
import logging
from config import PROXY_USERNAME, PROXY_PASSWORD  # Ensure config contains these

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# List of proxy servers (Replace with your own)
PROXY_LIST = [
    "p1.webshare.io:80",
    "p2.webshare.io:80",
    "p3.webshare.io:80",
    "p4.webshare.io:80",
]

# Test sites to verify proxy functionality
TEST_URLS = [
    "http://ipinfo.io/json",
    "https://www.google.com",
    "https://www.cloudflare.com/cdn-cgi/trace"
]

def get_random_proxy():
    """Returns a proxy with authentication."""
    proxy = random.choice(PROXY_LIST)
    return {
        "http": f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{proxy}",
        "https": f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{proxy}",
    }

def test_proxy(proxy):
    """Tests if the proxy is working by checking external IP."""
    headers = {"User-Agent": "Mozilla/5.0"}
    
    for url in TEST_URLS:
        try:
            logging.info(f"🔍 Testing proxy {proxy['http']} with {url}")
            response = requests.get(url, proxies=proxy, headers=headers, timeout=7)
            if response.status_code == 200:
                logging.info(f"✅ Proxy is working: {response.json() if 'json' in response.headers.get('Content-Type', '') else response.text}")
                return True
        except requests.exceptions.ProxyError:
            logging.warning(f"❌ Proxy failed (ProxyError): {proxy['http']}")
        except requests.exceptions.Timeout:
            logging.warning(f"⏳ Proxy timeout: {proxy['http']}")
        except requests.RequestException as e:
            logging.warning(f"❌ Proxy request error: {e}")
    
    return False

def get_proxy():
    """Fetches a working proxy from the list."""
    shuffled_proxies = random.sample(PROXY_LIST, len(PROXY_LIST))  # Shuffle proxies for fairness
    for proxy_address in shuffled_proxies:
        proxy = {
            "http": f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{proxy_address}",
            "https": f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{proxy_address}",
        }
        if test_proxy(proxy):
            return proxy
    
    logging.error("🚨 No working proxies found!")
    return None  # Fallback behavior: Handle this in the main script

if __name__ == "__main__":
    proxy = get_proxy()
    if proxy:
        print(f"✅ Using Proxy: {proxy['http']}")
    else:
        print("❌ No working proxy found.")

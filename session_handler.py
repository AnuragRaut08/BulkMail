import pickle
import os

def save_session(driver, filename="session.pkl"):
    """Saves browser cookies to a file."""
    try:
        with open(filename, "wb") as file:
            pickle.dump(driver.get_cookies(), file)
        print(f"✅ Session saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving session: {e}")

def load_session(driver, url, filename="session.pkl"):
    """Loads browser cookies from a file."""
    if not os.path.exists(filename):
        print("⚠️ No saved session found.")
        return
    
    try:
        driver.get(url)  # Open a page before setting cookies
        with open(filename, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        print(f"✅ Session loaded from {filename}")
    except Exception as e:
        print(f"❌ Error loading session: {e}")

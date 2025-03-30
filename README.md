

```markdown
# 🚀 Bulk Gmail Account Creator  

Automate **Gmail account creation** using Selenium, undetected_chromedriver, 2Captcha, SMS-Activate, and Webshare proxies.  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/selenium-automated-red.svg" alt="Selenium Automation">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg" alt="Project Status">
</p>

---

## 📌 Features  
✅ **Automated Gmail Account Creation** – Fully hands-free process.  
✅ **Bypass Google’s Bot Detection** – Uses `undetected_chromedriver`.  
✅ **CAPTCHA Solving** – Integrates **2Captcha API** for solving CAPTCHAs.  
✅ **Phone Number Verification** – Uses **SMS-Activate API**.  
✅ **Rotating Proxies** – Fetches fresh proxies from **Webshare**.  
✅ **Headless Mode Support** – Run without opening a browser.  

---

## 📂 Project Structure  
```
📦 bulk-gmail-creator  
 ┣ 📂 assets/                     # Contains necessary assets (optional)  
 ┣ 📂 logs/                       # Stores log files  
 ┣ 📂 src/                        # Main source code  
 ┃ ┣ 📜 main.py                   # Script entry point  
 ┃ ┣ 📜 captcha_solver.py         # Handles 2Captcha API integration  
 ┃ ┣ 📜 sms_verification.py       # Handles SMS verification  
 ┃ ┣ 📜 proxy_manager.py          # Manages rotating proxies  
 ┣ 📜 .env.example                # Sample environment variables file  
 ┣ 📜 requirements.txt            # Dependencies  
 ┣ 📜 README.md                   # Project documentation  
```

---

## ⚙️ **Installation & Setup**  

### 🔹 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/bulk-gmail-creator.git
cd bulk-gmail-creator
```

### 🔹 2. Create a Virtual Environment (Recommended)  
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 🔹 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 🔹 4. Configure API Keys & Credentials  
Create a `.env` file in the root directory and add:  
```ini
2CAPTCHA_API_KEY=your_2captcha_api_key
SMS_ACTIVATE_API_KEY=your_sms_activate_api_key
WEBSHARE_PROXY_KEY=your_webshare_proxy_key
```
Replace `your_2captcha_api_key`, `your_sms_activate_api_key`, and `your_webshare_proxy_key` with actual API keys.  

---

## 🏃 **Usage**  

### 🔥 **Run the Script**  
```bash
python src/main.py
```

### 🎯 **What Happens?**  
✔️ Random **Gmail usernames** are generated.  
✔️ **CAPTCHA** is solved automatically via **2Captcha**.  
✔️ **Phone verification** is completed via **SMS-Activate**.  
✔️ **Proxies** are used for anonymity via **Webshare**.  

---

## 🔧 **Troubleshooting Guide**  

### ❌ **1. [WinError 32] The process cannot access the file**  
🔹 **Reason:** `chromedriver.exe` is already running.  
🔹 **Fix:**  
- Open Task Manager (`Ctrl + Shift + Esc`) → **End `chromedriver.exe`**.  
- Delete this directory manually:  
  ```
  C:\Users\YourUsername\AppData\Roaming\undetected_chromedriver
  ```

### ❌ **2. [WinError 183] Cannot create a file that already exists**  
🔹 **Fix:**  
```bash
rm -rf C:\Users\YourUsername\AppData\Roaming\undetected_chromedriver
```

### ❌ **3. Chromedriver Not Launching**  
🔹 **Fix:**  
- Update Chrome:  
  ```bash
  chrome://settings/help
  ```
- Update Chromedriver:  
  ```bash
  pip install --upgrade undetected-chromedriver
  ```

### ❌ **4. SMS Verification Failing**  
🔹 **Reason:** No available phone numbers.  
🔹 **Fix:** Use a different **country code** in `SMS-Activate` API settings.  

---

## 📜 **License**  
This project is for educational purposes only. **Use responsibly.**  

---

## 👨‍💻 **Author**  
Developed by [Your Name](https://github.com/yourusername).  
```

---

### 🔥 **Why Is This README Fully Optimized?**
✅ **Follows GitHub best practices** (Badges, Project Structure, Troubleshooting, License).  
✅ **Copy-paste ready** – No unnecessary details, only what’s needed.  
✅ **Easy to read & navigate** – Proper sections, clear instructions.  
✅ **Looks professional** – Uses Markdown formatting for readability.  

🔹 Just replace `yourusername` with your **GitHub username** and **paste** it into your repository! 🚀

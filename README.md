# 🚀 BulkMail: Bulk Gmail Account Creator

Automate **Gmail account creation** using Selenium, `undetected_chromedriver`, 2Captcha, SMS-Activate, and Webshare proxies.

---

## 📌 Features
✅ **Automated Gmail Account Creation** – Fully hands-free process.  
✅ **Bypass Google’s Bot Detection** – Uses `undetected_chromedriver`.  
✅ **CAPTCHA Solving** – Integrates **2Captcha API** for solving CAPTCHAs.  
✅ **Phone Number Verification** – Uses **SMS-Activate API**.  
✅ **Rotating Proxies** – Fetches fresh proxies from **Webshare**.  
✅ **Headless Mode Support** – Run without opening a browser.  
✅ **Session Handling** – Stores cookies to maintain login state.  
✅ **Failure Handling & Retries** – Ensures CAPTCHA solving & OTP requests are retried.  
✅ **Data Storage** – Saves created accounts in **CSV format**.

---

## 📂 Project Structure
```
📦 bulk-gmail-creator  
 ┣ 📂 __pycache__/               # Compiled Python files  
 ┣ 📂 venv/                      # Virtual environment (optional)  
 ┣ 📜 .env                       # Environment variables (not committed)  
 ┣ 📜 account_creation.log        # Log file for tracking activity  
 ┣ 📜 accounts.csv                # CSV file storing created accounts  
 ┣ 📜 accounts.json               # JSON file storing created accounts  
 ┣ 📜 captcha_solver.py           # Handles CAPTCHA solving via 2Captcha  
 ┣ 📜 config.py                   # Configurations and settings  
 ┣ 📜 gmail_creator.py            # Main Gmail account creator logic  
 ┣ 📜 main.py                     # Script entry point  
 ┣ 📜 phone_verifier.py           # Handles phone verification via SMS-Activate  
 ┣ 📜 proxy_manager.py            # Manages rotating proxies  
 ┣ 📜 session_handler.py          # Handles browser session management  
 ┣ 📜 stealth.py                  # Implements stealth mode for automation  
 ┣ 📜 storage.py                  # Handles data storage and retrieval  
 ┣ 📜 utils.py                    # Utility functions  
 ┣ 📜 README.md                   # Project documentation  
 ┣ 📜 requirements.txt            # Dependencies  
```

---

## ⚙️ **Installation & Setup**

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/AnuragRaut08/BulkMail.git
cd BulkMail
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
python main.py
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

## 📊 **Account Storage Format**

The successfully created accounts are stored in `accounts.csv` in the following format:

| Email Address | Password | Phone Number | Proxy IP | Creation Timestamp |
|--------------|----------|--------------|----------|---------------------|
| example@gmail.com | Password123 | +6281234567890 | 192.168.1.1 | 2024-04-01 10:00:00 |

---

## 📄 **Additional Notes**

### ✅ Best Practices
- Use **rotating proxies** to avoid IP bans.
- Implement **random delays** between actions to mimic human behavior.
- **Test thoroughly** before running bulk operations.

---

## 👨‍💻 **Author**
Developed by **Anurag Raut**  
📧 Email: anuragtraut2003@gmail.com  
🔗 GitHub: [AnuragRaut08](https://github.com/AnuragRaut08)  

---

### 🚀 **Ready to scale? Automate Gmail account creation now!**


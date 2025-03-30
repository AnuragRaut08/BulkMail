import json
import csv
import os
import threading
from datetime import datetime

# File paths
CSV_FILE = "accounts.csv"
JSON_FILE = "accounts.json"

# Thread lock to prevent concurrent file access issues
lock = threading.Lock()

def save_account(email, password, phone_number, proxy, backup_email=None):
    """Save account details in both CSV and JSON format safely."""
    
    # Validate inputs
    if not all([email, password, phone_number, proxy]):
        print("❌ ERROR: Missing required fields. Account not saved.")
        return
    
    # Ensure timestamp is recorded
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create account dictionary
    account_data = {
        "email": email,
        "password": password,
        "phone_number": phone_number,
        "proxy": proxy,
        "backup_email": backup_email if backup_email else "N/A",
        "timestamp": timestamp
    }

    # ✅ Save to CSV
    with lock:  # Prevent concurrent writing issues
        file_exists = os.path.exists(CSV_FILE)
        try:
            with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["email", "password", "phone_number", "proxy", "backup_email", "timestamp"])  # Header
                writer.writerow(account_data.values())
        except Exception as e:
            print(f"❌ ERROR: Failed to write to CSV - {e}")
            return

    # ✅ Save to JSON
    with lock:
        try:
            if os.path.exists(JSON_FILE):
                with open(JSON_FILE, "r", encoding="utf-8") as file:
                    try:
                        accounts = json.load(file)
                    except json.JSONDecodeError:
                        accounts = []  # Reset in case of corruption
            else:
                accounts = []

            accounts.append(account_data)

            with open(JSON_FILE, "w", encoding="utf-8") as file:
                json.dump(accounts, file, indent=4)

            print(f"✅ Account saved: {email}")

        except Exception as e:
            print(f"❌ ERROR: Could not save account to JSON - {e}")

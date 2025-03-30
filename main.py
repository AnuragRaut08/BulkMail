from concurrent.futures import ThreadPoolExecutor, as_completed
from gmail_creator import create_gmail_account
import logging

# Number of accounts to create
NUM_ACCOUNTS = 10  
MAX_WORKERS = min(5, NUM_ACCOUNTS)  # Limit concurrency for efficiency

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def create_bulk_accounts():
    """Creates multiple Gmail accounts in parallel with error handling."""
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_index = {executor.submit(create_gmail_account): i+1 for i in range(NUM_ACCOUNTS)}
        
        for future in as_completed(future_to_index):
            index = future_to_index[future]
            try:
                future.result()  # Ensures exception handling
                logging.info(f"✅ Account {index}/{NUM_ACCOUNTS} created successfully!")
            except Exception as e:
                logging.error(f"❌ Failed to create account {index}: {e}")

if __name__ == "__main__":
    create_bulk_accounts()


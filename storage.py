import pandas as pd

def save_account(email, password, phone, proxy, timestamp):
    df = pd.DataFrame([[email, password, phone, proxy, timestamp]], columns=["Email", "Password", "Phone", "Proxy", "Timestamp"])
    df.to_csv("accounts.csv", mode='a', index=False, header=False)

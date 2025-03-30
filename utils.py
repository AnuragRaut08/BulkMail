import random
import string

COMMON_NAMES = ["alex", "mike", "john", "emma", "sarah", "lisa", "mark", "jake"]
DOMAINS = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com"]

def generate_email(domains=None):
    """Generate a more realistic email address with mixed characters"""
    if domains is None:
        domains = DOMAINS  # Use default domains
    
    username = random.choice(COMMON_NAMES) + "".join(random.choices(string.ascii_lowercase + string.digits, k=3))
    return username + random.choice(domains)

def generate_password(length=12):
    """Generate a strong random password ensuring all character types are included"""
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security.")

    while True:
        password = "".join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=length))
        if (any(c.islower() for c in password) and 
            any(c.isupper() for c in password) and 
            any(c.isdigit() for c in password) and 
            any(c in "!@#$%^&*" for c in password)):
            return password

# Example Usage:
if __name__ == "__main__":
    print("Generated Email:", generate_email())
    print("Generated Password:", generate_password(14))  # Customize password length

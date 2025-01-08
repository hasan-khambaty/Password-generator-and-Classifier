import re

def extract_features(password):
    """Extract features from a password."""
    length = len(password)
    uppercase = sum(1 for char in password if char.isupper())
    lowercase = sum(1 for char in password if char.islower())
    digits = sum(1 for char in password if char.isdigit())
    special_chars = sum(1 for char in password if re.match(r'[!@#$%^&*(),.?":{}|<>]', char))

    # Return features as a dictionary
    return {
        "length": length,
        "uppercase": uppercase,
        "lowercase": lowercase,
        "digits": digits,
        "special_chars": special_chars
    }

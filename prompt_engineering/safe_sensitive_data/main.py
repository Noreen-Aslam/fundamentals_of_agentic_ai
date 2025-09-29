import re

text = "My email is noreen123@gmail.com and my phone is +92 321 1234567. My password is 12345"

# --- Patterns ---
email_pattern = r"\S+@\S+\.\S+"
phone_pattern = r"(\+92|0?3[0-9]{2}[- ]?[0-9]{7})"  # fixed full phone number
keywords = ["password", "api_key", "secret"]

# --- Redact function ---
def redact_sensitive(text):
    # Regex redaction
    text = re.sub(email_pattern, "[REDACTED_EMAIL]", text)
    text = re.sub(phone_pattern, "[REDACTED_PHONE]", text)
    
    # Keyword redaction
    for kw in keywords:
        # (?i) → ignore case
        text = re.sub(f"(?i){kw}.*?(\s|$)", f"[REDACTED_{kw.upper()}] ", text)
    
    return text

redacted_text = redact_sensitive(text)
print("Redacted message:", redacted_text)

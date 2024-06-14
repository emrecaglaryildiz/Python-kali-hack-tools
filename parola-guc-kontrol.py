def check_password_strength(password):
    if len(password) < 8:
        return "Weak password: Too short"
    if not any(char.isdigit() for char in password):
        return "Weak password: No digits"
    if not any(char.islower() for char in password):
        return "Weak password: No lowercase letters"
    if not any(char.isupper() for char in password):
        return "Weak password: No uppercase letters"
    return "Strong password"

passwords = ["password123", "StrongPass1", "weakpass"]
for pwd in passwords:
    print(f"{pwd}: {check_password_strength(pwd)}")

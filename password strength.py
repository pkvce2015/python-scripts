import re

def check_password_strength(password):
    # Criteria checks
    length_error = len(password) < 8
    lowercase_error = not re.search(r"[a-z]", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Scoring system
    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    # Feedback
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"\nPassword Strength: {strength}")

    # Suggestions (optional)
    if strength != "Strong":
        print("Suggestions to improve your password:")
        if length_error:
            print("- Use at least 8 characters.")
        if lowercase_error:
            print("- Include lowercase letters.")
        if uppercase_error:
            print("- Include uppercase letters.")
        if digit_error:
            print("- Include digits (0-9).")
        if special_char_error:
            print("- Include special characters (!@#$%^&* etc.)")

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password to check strength: ")
    check_password_strength(user_password)

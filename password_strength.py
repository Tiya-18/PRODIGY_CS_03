import re

def assess_password_strength(password):
    # Initialize strength score and feedback list
    strength_score = 0
    feedback = []

    # Criteria for assessing password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    # Increment score based on criteria met
    if length_criteria:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lowercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if number_criteria:
        strength_score += 1
    else:
        feedback.append("Password should include at least one number.")

    if special_char_criteria:
        strength_score += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #, $, etc.).")

    # Determine password strength based on score
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback

# Example usage
password = input("Enter a password to assess its strength: ")
strength, feedback = assess_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for suggestion in feedback:
        print(f"- {suggestion}")

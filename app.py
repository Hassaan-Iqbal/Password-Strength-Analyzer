from flask import Flask, render_template, request

app = Flask(__name__)


# Load common passwords/words from the text file
def load_common_passwords():
    with open("common_passwords.txt", "r", encoding="utf-8") as file:
        return {
            line.strip().lower()
            for line in file
            if line.strip()
        }


COMMON_PASSWORDS = load_common_passwords()


# Detect common words or patterns inside a password
def find_common_pattern(password):
    password_lower = password.lower()

    for common_word in COMMON_PASSWORDS:
        if common_word in password_lower:
            return True, common_word

    return False, None


# Analyze password strength
def check_password_strength(password):

    score = 0

    checks = {
        "length": False,
        "length_12": False,
        "lowercase": False,
        "uppercase": False,
        "number": False,
        "symbol": False,
        "variety": False
    }

    # Check for common password pattern
    is_common, matched_word = find_common_pattern(password)

    # Check minimum length
    if len(password) >= 8:
        checks["length"] = True
        score += 1

    # Check 12+ characters
    if len(password) >= 12:
        checks["length_12"] = True
        score += 1

    # Check lowercase letter
    if any(char.islower() for char in password):
        checks["lowercase"] = True
        score += 1

    # Check uppercase letter
    if any(char.isupper() for char in password):
        checks["uppercase"] = True
        score += 1

    # Check number
    if any(char.isdigit() for char in password):
        checks["number"] = True
        score += 1

    # Check special character
    if any(not char.isalnum() for char in password):
        checks["symbol"] = True
        score += 1

    # Check character variety
    character_types = 0

    if any(char.islower() for char in password):
        character_types += 1

    if any(char.isupper() for char in password):
        character_types += 1

    if any(char.isdigit() for char in password):
        character_types += 1

    if any(not char.isalnum() for char in password):
        character_types += 1

    if character_types >= 3:
        checks["variety"] = True
        score += 1

    # Calculate password strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    # Common passwords/patterns should not be considered strong
    if is_common:
        strength = "Weak"

    return strength, checks, score, is_common, matched_word


# Main page
@app.route("/", methods=["GET", "POST"])
def home():

    strength = None
    checks = None
    score = 0
    is_common = False
    matched_word = None

    if request.method == "POST":

        password = request.form.get("password", "")

        strength, checks, score, is_common, matched_word = (
            check_password_strength(password)
        )

    return render_template(
        "index.html",
        strength=strength,
        checks=checks,
        score=score,
        is_common=is_common,
        matched_word=matched_word
    )


# Start the application
if __name__ == "__main__":
    app.run(debug=True)
import re
import math

def password_strength(password):
    score = 0
    length = len(password)

    # Scoring rules
    if length >= 8:
        score += 2
    if re.search(r'[A-Z]', password):
        score += 2
    if re.search(r'[a-z]', password):
        score += 2
    if re.search(r'\d', password):
        score += 2
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2

    # Entropy calculation
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32

    entropy = length * math.log2(charset_size) if charset_size else 0

    # Output
    print("\n🔍 Password Analysis:")
    print(f"🧠 Strength Score: {score}/10")
    print(f"🔐 Entropy: {entropy:.2f} bits")

    if score <= 4:
        print("Verdict: ❌ Weak")
    elif score <= 7:
        print("Verdict: ⚠️  Medium")
    else:
        print("Verdict: ✅ Strong")

from analyze_password import password_strength
from wordlist_generator import generate_wordlist
from export_wordlist import export_wordlist

def main():
    print("\n🔐 Password Strength Analyzer + Wordlist Generator 🔐")
    
    # Password analysis
    password = input("Enter a password to analyze: ")
    password_strength(password)

    # Collect user details
    print("\n📋 Let's collect details to generate a custom wordlist")
    name = input("Name: ")
    dob = input("Date of Birth (YYYYMMDD): ")
    pet = input("Pet Name: ")
    extras = input("Other keywords (comma-separated): ").split(",")

    # Generate and export wordlist
    wordlist = generate_wordlist(name, dob, pet, extras)
    export_wordlist(wordlist)

if __name__ == "__main__":
    main()

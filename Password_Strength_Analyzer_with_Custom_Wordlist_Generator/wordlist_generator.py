def leetspeak(word):
    replace = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
    return ''.join(replace.get(c.lower(), c) for c in word)

def generate_wordlist(name, dob, pet, extras=None):
    wordlist = set()

    base_words = [name, pet, dob, name + pet, pet + dob, name + dob]
    years = ["2023", "2024", "2025"]
    suffixes = ["123", "!", "@", dob[-2:], dob[-4:]]

    variations = []

    for word in base_words:
        variations.extend([
            word.lower(), word.upper(), word.capitalize(),
            leetspeak(word),
        ])

    for var in variations:
        for suffix in suffixes + years:
            wordlist.add(var + suffix)

    if extras:
        wordlist.update([e.strip() for e in extras])

    return sorted(wordlist)

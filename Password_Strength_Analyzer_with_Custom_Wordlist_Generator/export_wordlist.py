def export_wordlist(wordlist, filename="custom_wordlist.txt"):
    with open(filename, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')
    print(f"\n📁 Wordlist saved to: {filename}")

import hashlib

def crack_md5_hash(hash_value, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            word = line.strip()
            if hashlib.md5(word.encode()).hexdigest() == hash_value:
                print(f"Password found: {word}")
                return
    print("Password not found in wordlist")

hash_value = "5f4dcc3b5aa765d61d8327deb882cf99"  # Hash'lenmiş "password" değeri
wordlist = "wordlist.txt"  # Parola listesi dosya yolu
crack_md5_hash(hash_value, wordlist)

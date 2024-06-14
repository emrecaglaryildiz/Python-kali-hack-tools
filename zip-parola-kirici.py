import zipfile

def zip_cracker(zip_file, wordlist):
    with zipfile.ZipFile(zip_file, 'r') as zf:
        with open(wordlist, 'r') as file:
            for line in file:
                password = line.strip()
                try:
                    zf.extractall(pwd=password.encode())
                    print(f"Password found: {password}")
                    return
                except RuntimeError:
                    print(f"Failed password: {password}")

zip_file = "protected.zip"
wordlist = "passwords.txt"
zip_cracker(zip_file, wordlist)

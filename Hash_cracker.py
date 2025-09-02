import hashlib
import sys

def crack_hash(hash_type, target_hash, wordlist_path):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
            for word in file:
                word = word.strip()
                if hash_type.lower() == "md5":
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type.lower() == "sha1":
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type.lower() == "sha256":
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                elif hash_type.lower() == "sha512":
                    hashed_word = hashlib.sha512(word.encode()).hexdigest()
                else:
                    print(f"Unsupported hash type: {hash_type}")
                    return None

                if hashed_word == target_hash:
                    return word
        return None
    except FileNotFoundError:
        print("Wordlist file not found.")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python hash_cracker.py <hash_type> <hash> <wordlist>")
        print("Example: python hash_cracker.py md5 5d41402abc4b2a76b9719d911017c592 wordlist.txt")
        sys.exit(1)

    hash_type = sys.argv[1]
    target_hash = sys.argv[2]
    wordlist = sys.argv[3]

    result = crack_hash(hash_type, target_hash, wordlist)
    if result:
        print(f"[+] Hash cracked! Plaintext: {result}")
    else:
        print("[-] Hash not found in wordlist.")

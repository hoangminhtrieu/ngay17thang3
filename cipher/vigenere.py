class VigenereCipher:
    def encrypt(self, text, key):
        result = ""
        key = key.upper()
        key_idx = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_idx % len(key)]) - 65
                if char.isupper():
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                key_idx += 1
            else:
                result += char
        return result

    def decrypt(self, text, key):
        result = ""
        key = key.upper()
        key_idx = 0
        for char in text:
            if char.isalpha():
                shift = ord(key[key_idx % len(key)]) - 65
                if char.isupper():
                    result += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    result += chr((ord(char) - shift - 97) % 26 + 97)
                key_idx += 1
            else:
                result += char
        return result

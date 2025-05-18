def encrypt(text, shift):
    result = ""
    for char in text:
        if char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter a message (lowercase letters only): ")
shift = int(input("Enter a shift number (e.g., 3): "))

encrypted = encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)

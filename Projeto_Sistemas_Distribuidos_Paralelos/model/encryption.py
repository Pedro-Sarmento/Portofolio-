def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character and wrap around the alphabet
            char_shifted = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            
            encrypted_text += char_shifted
        else:
            # If the character is not a letter, keep it unchanged
            encrypted_text += char
            
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    # Decryption is the same as encryption with a negative shift
    return encrypt_caesar(ciphertext, -shift)
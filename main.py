def generate_key():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alphabet)
    return dict(zip('abcdefghijklmnopqrstuvwxyz', alphabet))

def encrypt(key, message):
    encrypted = ''
    for char in message:
        if char.lower() in key:
            encrypted += key[char.lower()]
        else:
            encrypted += char
    return encrypted

def decrypt(key, message):
    reversed_key = {value: key for key, value in key.items()}
    decrypted = ''
    for char in message:
        if char.lower() in reversed_key:
            decrypted += reversed_key[char.lower()]
        else:
            decrypted += char
    return decrypted

key = generate_key()
message = 'hello world'
encrypted_message = encrypt(key, message)
decrypted_message = decrypt(key, encrypted_message)

print(f'Original message: {message}')
print(f'Encrypted message: {encrypted_message}')
print(f'Decrypted message: {decrypted_message}')

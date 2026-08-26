cipher_hex = input("Ciphertext (Hex): ").strip()
cipher = bytes.fromhex(cipher_hex)

known_prefix = "THM{"
known_suffix = "}"

key = [None] * 5

# key[0..3] from the first 4 bytes
for i in range(4):
    key[i] = cipher[i] ^ ord(known_prefix[i])

# the last missing key byte from the last ciphertext byte
last_index = len(cipher) - 1
key[last_index % 5] = cipher[last_index] ^ ord(known_suffix)

recovered_key = ''.join(chr(b) for b in key)
print("Key:", recovered_key)

# sanity check: decrypt the full message with it
decoded = ''.join(chr(cipher[i] ^ key[i % 5]) for i in range(len(cipher)))
print("Decoded:", decoded)

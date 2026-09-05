# W1seGuy

A repeating-key XOR challenge where the flag format is known ahead of time: it starts with `THM{` and ends with `}`. That known plaintext is enough to recover the full key without any brute forcing.

## `W1seGuy.py`

1. Prompts for the ciphertext as a hex string and decodes it to bytes.
2. Assumes a 5-byte repeating key (`key[0..4]`).
3. Recovers `key[0..3]` by XORing the first 4 ciphertext bytes against the known prefix `THM{`.
4. Recovers the one remaining key byte by XORing the *last* ciphertext byte against the known suffix `}` (the key index for the last byte is `len(cipher) - 1 mod 5`).
5. Tiles the 5 recovered key bytes across the whole ciphertext length and XORs it back to reveal the plaintext flag.

**Key takeaway:** with a repeating XOR key, you don't need every byte of plaintext to recover the whole key — just enough known bytes to cover every key position at least once (here, 4 bytes from the start plus 1 byte from the end covers all 5 key positions).

## Usage

```bash
python3 W1seGuy.py
Ciphertext (Hex): <paste hex ciphertext here>
```

# TryHackMe

Personal write-ups and solve scripts for TryHackMe challenges, mostly cryptography-focused (XOR ciphers, key recovery from known-plaintext).

## Structure

Each challenge lives in its own folder. Every folder has its own `README.md` explaining what the scripts inside it do and how the challenge was solved.

| Folder | Challenge | Technique |
|---|---|---|
| [`Order/`](Order/README.md) | "Order" | Recovering a repeating XOR key from a known plaintext prefix, across a two-line ciphertext |
| [`W1seGuy/`](W1seGuy/README.md) | "W1seGuy" | Recovering a 5-byte repeating XOR key from a known `THM{...}` flag prefix/suffix |

## Usage

Each script is standalone and run with Python 3, e.g.:

```bash
python3 W1seGuy/W1seGuy.py
```

Some scripts prompt for hex-encoded ciphertext on stdin; others have the ciphertext hardcoded at the top of the file.

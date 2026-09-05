# Order

Two hex-encoded ciphertext lines are XOR-encrypted with a short repeating key. The plaintext is known to start with `ORDER:`, which is enough to recover the key.

## Files

### `decrypt.py`

Exploration script. It:

1. Loads both ciphertext lines (`line1`, `line2`) and hex-decodes them.
2. Brute-forces key lengths 1-16: for each length, derives as many key bytes as possible from the known `ORDER:` prefix, tiles that into a full-length key, XOR-decrypts `line1`, and checks whether the result is printable.
3. Once a working key length is found, derives the key directly from the first 6 bytes of `line1` XORed against `ORDER:`, then decrypts `line1` and `line2` **independently** with that key restarted from byte 0 each time.

This independent-restart approach decrypts `line1` cleanly but produces garbage for `line2`, because `line2` isn't a fresh message re-using the same key phase — it's a continuation of the same keystream that started at `line1`.

### `decrypt2.py`

The actual solution. It concatenates `line1 + line2` into one byte string *before* decrypting, so the repeating key (`SNEAKY`, recovered by hand from `decrypt.py`'s output) stays in phase across the boundary between the two lines. XOR-decrypting the combined bytes with the tiled key recovers the full message:

```
ORDER: Attack at dawn. Target: THM{the_hackfinity_highschool}.
```

**Key takeaway:** when ciphertext is split across multiple lines/fields but was encrypted as one continuous stream, you must decrypt it as one continuous stream — decrypting each piece independently resets the key phase and breaks everything after the first chunk.

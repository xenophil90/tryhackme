# Cipers Secret Message

A message is encrypted with a positional Caesar cipher: each letter is shifted forward within its own case's alphabet (A-Z or a-z) by its index in the string. Non-letter characters (`_`, digits) are left unchanged but still count toward the index, since the encryption loop uses `enumerate(plaintext)` over the whole string, not just the letters.

## Files

### `decode.py`

The solution. For each character at index `i` in the ciphertext, if it's a letter, it subtracts `i` from its code point (mod 26, within the same case) to undo the shift; non-letters are copied through as-is. Running it against the given message recovers:

```
THM{a_sm4ll_crypt0_message_to_st4rt_with_THM_cracks}
```

**Key takeaway:** the shift amount is the character's index in the *entire* string, not its index among letters only — non-alpha characters still advance the counter even though they aren't themselves shifted.

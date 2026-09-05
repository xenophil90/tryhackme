"""
Decoder for the "Order" challenge.

The encryption shifts each alphabetic character forward by its index `i`
in the *whole* string (enumerate(plaintext) counts every character,
including non-alpha ones like '_' and digits). Non-alpha characters are
left untouched but still count toward the index.

Since the shift is a simple additive Caesar shift per position, decoding
just subtracts the same index back off.
"""

MESSAGE = "a_up4qr_kaiaf0_bujktaz_qm_su4ux_cpbq_ETZ_rhrudm"


def dec(ciphertext: str) -> str:
    result = []
    for i, c in enumerate(ciphertext):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base - i) % 26 + base))
        else:
            result.append(c)
    return "".join(result)


if __name__ == "__main__":
    plaintext = dec(MESSAGE)
    print(f"THM{{{plaintext}}}")

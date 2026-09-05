import itertools

line1 = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
line2 = "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"

b1 = bytes.fromhex(line1)
b2 = bytes.fromhex(line2)
print(len(b1), len(b2))

known = b"ORDER:"

# try key lengths 1..16, derive key bytes from known prefix, then decrypt full and check printable
for keylen in range(1, 17):
    key = bytearray(keylen)
    for i in range(min(len(known), keylen)):
        key[i] = known[i] ^ b1[i]
    full_key = (bytes(key) * (len(b1)//keylen + 1))[:len(b1)]
    dec = bytes([bb ^ kk for bb, kk in zip(b1, full_key)])
    printable = all(32 <= c < 127 or c in (9,10,13) for c in dec)
    print(keylen, printable, dec)

known = b"ORDER:"
key = bytes([known[i] ^ b1[i] for i in range(6)])
print("key:", key)
full_key1 = (key * (len(b1)//6+1))[:len(b1)]
full_key2 = (key * (len(b2)//6+1))[:len(b2)]
dec1 = bytes([bb^kk for bb,kk in zip(b1, full_key1)])
dec2 = bytes([bb^kk for bb,kk in zip(b2, full_key2)])
print(dec1.decode())
print(dec2.decode())
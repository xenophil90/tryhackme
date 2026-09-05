line1 = "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
line2 = "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
combined = bytes.fromhex(line1+line2)
key = b"SNEAKY"
full_key = (key * (len(combined)//6+1))[:len(combined)]
dec = bytes([bb^kk for bb,kk in zip(combined, full_key)])
print(dec)
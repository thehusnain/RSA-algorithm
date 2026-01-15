M = 31
e = 7
d = 3
n = 33

# Encyption 
encrypted = (M ** e) % n
print("Encrypted:",encrypted)

# Decryption
decrypted = (encrypted ** d) % n
print("Decrypted", decrypted)

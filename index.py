from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

# Plaintext (dummy dataset)
plaintext = "Proyek ini menguji algoritma AES untuk keamanan data.".encode()

# Kunci AES (16 byte = 128 bit)
key = get_random_bytes(16)

# AES menggunakan mode ECB
cipher = AES.new(key, AES.MODE_ECB)

# Padding sederhana (agar panjang kelipatan 16)
pad_len = 16 - (len(plaintext) % 16)
padded_plaintext = plaintext + bytes([pad_len]) * pad_len

# Enkripsi
start_enc = time.time()
ciphertext = cipher.encrypt(padded_plaintext)
end_enc = time.time()

# Dekripsi
start_dec = time.time()
decrypted = cipher.decrypt(ciphertext)
end_dec = time.time()

# Hapus padding
unpadded = decrypted[:-decrypted[-1]]

print("Plaintext  :", plaintext.decode())
print("Ciphertext :", ciphertext.hex())
print("Hasil Dekripsi :", unpadded.decode())
print("Waktu Enkripsi :", end_enc - start_enc, "detik")
print("Waktu Dekripsi :", end_dec - start_dec, "detik")

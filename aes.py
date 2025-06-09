from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_aes(inp, out):
    key = get_random_bytes(16)  # AES-128
    cipher = AES.new(key, AES.MODE_CBC)
    
    with open(inp, 'rb') as infile:
        plaintext = infile.read()
    
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    with open(out, 'wb') as outfile:
        outfile.write(cipher.iv)  
        outfile.write(ciphertext)
    print ("Pomyslnie zaszyfrowano plik.")

in1= input("Podaj sciezke pliku wyjsciowego: ")
out = input("Podaj sciezke pliku wyjsciowego: ")
encrypt_aes(in1, out)
       
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def sign_message(data):
    klucz = RSA.generate(2048)
    private_key = klucz.export_key()
    public_key = klucz.publickey().export_key()

    with open('private_key.pem', 'wb') as file:
        file.write(private_key)

    with open('public_key.pem', 'wb') as file:
        file.write(public_key)

   
    with open(data, 'rb') as file:
        message = file.read()

    hash = SHA256.new(message)
    signature = pkcs1_15.new(klucz).sign(hash)

    with open('signature.bin', 'wb') as file:
        file.write(signature)


data = input("Podaj sciezke pliku do podpisania: ")
sign_message(data)
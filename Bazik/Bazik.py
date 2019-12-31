from Crypto.PublicKey import RSA
import binascii
def bytes_to_hex(data):
    return binascii.hexlify(data.encode("ascii"))[0:]

f = open("publickey.pem", "rb")
public_key = RSA.importKey(f.read())
f.close()
print("Public: {}  \nN={}\n".format(public_key.e, public_key.n))
encrypted_data="0x764a18c52802f763f721b6b2d7fd82738e08dc660d039f1a3ee9dff84159cc102de36537d659e26e6a6e9b1088239b4db6bce64929183e8bfd93ad2acef6b3bfe30e53c59f9f205260de5fe149bdeb486a01ed61ca9e574b8807a3a466275c5c2b118015e538eb4bf81a28fc6d51469cde0e441d8348844a3984e35aedfd69f0"
cipher="0x013137fd49bcccd5cb123102231a46b2047f043431295112c748fd8bad840a5fcf46ed1a07c5e1eeebd380e73a0e827798c76ae0c69a3cef6b161d4acd14c5799fd1e36063e009571fb2314c2e619ea98754c3b908d3f52bbf2522069fac574ccb7562b08e563e030eaf1d381fbc5e26294e2f5e6bb09077333598cc9abfb996"
x = int(cipher, 16)
print("x: {}".format(x))
print("lala: "+hex(279194786064165631462403655571007005294665174222443770940031343055849950569774655464736942913588929603436045601725648607914471752112311886315257902))
text="Your OTP for transaction #731337 in ABCXYZ Bank is 687845634."
text_2=bytes_to_hex(text)
print("text_2: {}".format(text_2))
xx=int(text_2,16)
print("xx: {}".format(xx))
wynik=pow(xx,public_key.e,public_key.n)
print("wynik w hex: {}".format(hex(wynik)))
print(binascii.hexlify(public_key.encrypt(text.encode("ascii"),"")[0]))
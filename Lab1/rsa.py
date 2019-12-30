from Crypto.PublicKey import RSA

f = open("private.pem", "rb")
private_key = RSA.importKey(f.read())
f.close()
f = open("public.pem", "rb")
public_key = RSA.importKey(f.read())
f.close()
print("Public: {} \n Private: {} \nN={}\n".format(public_key.e,private_key.d,public_key.n))
message="alamakota"
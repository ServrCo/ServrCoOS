import hashlib, sys

passwdHash = hashlib.sha512(input("Please enter a password: ").encode())
passwdHashTxt = passwdHash.hexdigest()

print("Hashed!")

passwdFile = open("pwdFile", "w")
passwdFile.write(passwdHashTxt)
passwdFile.close()
print("Saved!")

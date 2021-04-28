print(" Welcome In Hashing App ")
import hashlib
string = input("Enter your word to hash : ")
result = hashlib.md5(string.encode())
print(" Result : ", result.hexdigest())


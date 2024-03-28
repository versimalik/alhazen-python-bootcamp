import hashlib as h

mypassword = "abc123"
encoded_pass = mypassword.encode()

hashed_pass = h.sha256(encoded_pass).hexdigest()
print(hashed_pass)
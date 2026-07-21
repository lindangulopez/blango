import hashlib

# SHA-256 hashes
print(hashlib.sha256(b"password").hexdigest())
print(hashlib.sha256(b"hello wold").hexdigest())
print(hashlib.sha256(b"password123").hexdigest())

# Salted hash
print(hashlib.sha256(b"abc123" + b"password123").hexdigest())

# Repeated hashing
hash_value = hashlib.sha256(b"abc123" + b"password123").hexdigest()

for i in range(1000):
    hash_value = hashlib.sha256(
        b"abc123" + hash_value.encode("ascii")
    ).hexdigest()

print(hash_value)
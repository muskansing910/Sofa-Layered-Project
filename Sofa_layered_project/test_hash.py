import bcrypt

password = input("Enter password: ")

password_hash = bcrypt.hashpw(
    password.encode('utf-8'),
    bcrypt.gensalt()
)

print("Original Password:", password)
print("Hashed Password:", password_hash.decode('utf-8'))
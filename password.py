from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

password = "meet123"

hashed = pwd_context.hash(password)

print("Original Password:", password)
print("Hashed Password:", hashed)

print("Valid :", pwd_context.verify(password, hashed))
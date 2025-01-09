from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"])

def get_password_hash(password):
    return bcrypt_context.hash(password)

def vevify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)

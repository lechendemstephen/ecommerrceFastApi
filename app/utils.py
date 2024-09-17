from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# hash password function 
def password_hasher(password: str): 

    return pwd_context.hash(password)

# function to verify password 
def password_verifier(plain_password: str, hashed_passsword:str ): 

    return pwd_context.verify(plain_password, hashed_passsword)


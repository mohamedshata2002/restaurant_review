from passlib.context import CryptContext


pwd_enc = CryptContext(schemes=["bcrypt"], deprecated="auto")
hash= CryptContext(schemes=["bcrypt"],deprecated="auto")

def Hash(password):
 return pwd_enc.hash(password)

def compare_pwd(plain_pwd,enter_pwd):
    return pwd_enc.verify(plain_pwd,enter_pwd)


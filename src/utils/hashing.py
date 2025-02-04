from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")

class hash():
    def bcypt(password:str):
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword
    def verify(orignalPass,givenPassword):
        return pwd_cxt.verify(givenPassword,orignalPass)

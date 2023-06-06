from pydantic import BaseModel, constr, conint, EmailStr, validator
from passlib.context import CryptContext
class User(BaseModel):
    first_name: constr(strict=True, min_length=4, max_length=15)
    last_name : constr(strict=True, min_length=4, max_length=15)
    password: str
    email: EmailStr
    phone: int
    
    
    
    
    @validator('phone')
    def check_phone(cls, v):
        if len(str(v)) < 10 or len(str(v)) > 12:
            raise ValueError('The phone number must have a length between 10 and 12 characters.')
        return v
    
    @validator('password')
    def password_security(cls, v):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        return pwd_context.hash(v)
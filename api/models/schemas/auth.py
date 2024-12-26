from pydantic import BaseModel, EmailStr

class Registration(BaseModel):
    phone: int
    password: str
    name: str
    login: str
    
class Login(BaseModel):
    phone: int
    password: str
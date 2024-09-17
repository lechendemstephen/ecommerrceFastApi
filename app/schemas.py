from pydantic import BaseModel, EmailStr


class CreatePost(BaseModel): 
    title: str
    description: str
    


class SignUp(BaseModel): 
    name: str 
    email: EmailStr
    password: str 


class Login(BaseModel): 
    email: EmailStr
    password: str 

class TokenData(BaseModel): 
    id: str 


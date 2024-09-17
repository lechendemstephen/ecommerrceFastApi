from pydantic import BaseModel, EmailStr


class CreatePost(BaseModel): 
    pass 



class SignUp(BaseModel): 
    name: str 
    email: EmailStr
    password: str 


class Login(BaseModel): 
    email: EmailStr
    password: str 

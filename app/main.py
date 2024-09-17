from fastapi import FastAPI
from .routers import blog, product, users
from . import models 

from .database import Base, engine



app = FastAPI()


app.include_router(blog.router)
app.include_router(product.router)
app.include_router(users.router)


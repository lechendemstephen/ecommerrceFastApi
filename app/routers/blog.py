from fastapi import APIRouter, Depends, HTTPException, status
from app.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/posts',
    tags= ['Blog']

)



@router.get('/post')
def get_all_post(): 

    return {
        "all_post": 'all_post'
    }


# creating a blog post
@router.post('/')
def create_blog(db: Session = Depends(get_db)): 
    pass



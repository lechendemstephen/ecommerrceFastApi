from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, models, utils


router = APIRouter(
    tags= ['Authentication']

)



# creating a user or Signup
@router.post('/user', status_code=status.HTTP_200_OK)
def create_user(user:schemas.SignUp,  db: Session = Depends(get_db)): 

    # hash the password before saving it to the database 
    hashed_password = utils.password_hasher(user.password)
    user.password = hashed_password

    new_user = models.Users(
        **user.dict()
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



# signing in the user 
@router.post('/login', status_code=status.HTTP_200_OK)
def login_user(user: schemas.Login, db: Session = Depends(get_db)): 

    db_user = db.query(models.Users).filter(models.Users.email == user.email).first()

    if not db_user: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'no user found with provided email, please created an account')
    
    if not utils.password_verifier(user.password, db_user.password): 
          raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Invalid password')
    
    # creat an access token 

    return {
         "okay": "you are doing excellent"
    }






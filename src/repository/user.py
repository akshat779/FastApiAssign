from fastapi import APIRouter,HTTPException,status
from ..utils.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from ..models import models
from ..schemas import schemas
from ..utils import hashing

def get_all_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    # if not users:
    #     return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="We dont have any registered Users as of Now")
    
    return users

def create_user(request:schemas.CreateUser,db:Session = Depends(get_db)):
    newUser = models.User(username=request.username,name = request.name,role=request.role,password = hashing.hash.bcypt(request.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

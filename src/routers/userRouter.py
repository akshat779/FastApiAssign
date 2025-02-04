from fastapi import APIRouter
from ..utils.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from ..models import models
from ..schemas import schemas
from ..repository import user

router = APIRouter(
    tags=["user"],
    prefix="/user"
)



@router.get('/')
def getAll(db:Session = Depends(get_db)):
    return user.get_all_users(db)



@router.post("/")
def createUser(request: schemas.CreateUser,db:Session = Depends(get_db)):
    return user.create_user(request,db)
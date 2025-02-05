from fastapi import APIRouter,HTTPException,status
from ..utils.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from ..models import models
from ..schemas import schemas
from ..repository import user
from ..utils import hashing
from fastapi.security import OAuth2PasswordRequestForm
from ..utils import oauth2

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

@router.get("/{id}")
def getUser(id:int, db:Session = Depends(get_db)):
    return user.singleUser(id,db)

@router.delete("/{id}")
def deleteUser(id:int,db:Session = Depends(get_db)):
    return user.delete_user(id,db)

@router.put("/{id}")
def updateUser(id:int,request:schemas.CreateUser,db:Session = Depends(get_db)):
    return user.update_user(id,request,db)

@router.post("/login", response_model=schemas.TokenData)
def login(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    if not hashing.hash.verify(user.password, form_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = oauth2.create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
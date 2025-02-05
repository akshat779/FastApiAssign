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

def create_user(request:schemas.CreateUser,db:Session = Depends(get_db),current_user = models.User):
    # newUser = models.User(username=request.username,name = request.name,role=request.role,password = hashing.hash.bcypt(request.password))
    # db.add(newUser)
    # db.commit()
    # db.refresh(newUser)
    # return newUser
    if request.role in [models.Roles.admin,models.Roles.tenant] and current_user.role != models.Roles.admin: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not allowed to create a user with this role")
    
    hashed_password = hashing.hash.bcrypt(request.password)
    if request.role == models.Roles.tenant:
        new_tenant = models.Tenant(name = request.name,password = hashed_password)
        db.add(new_tenant)
        db.commit()
        db.refresh(new_tenant)
        new_user = models.User(username=request.username,name = request.name,role=request.role,password = hashed_password,tenant_id = new_tenant.id)
    else:
        new_user = models.User(username=request.username,name = request.name,role=request.role,password = hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def singleUser(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    return user

def delete_user(id:int,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    user.delete(synchronize_session=False)
    db.commit()
    return {"message":"User Deleted Successfully"}

def update_user(id:int,request:schemas.CreateUser,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    if 'password' in request.dict():
        request.password = hashing.hash.bcypt(request.password)
    user.update(request.dict())
    db.commit()
    return {"message":"User Updated Successfully"}


from fastapi import APIRouter,HTTPException,status
from ..utils.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from ..models import models
from ..schemas import schemas
from ..utils import hashing

def get_all_tenants(db:Session = Depends(get_db)):
    tenants = db.query(models.Tenant).all()
    return tenants

def create_tenant(request:schemas.CreateTenant,db:Session = Depends(get_db)):
    new_tenant = models.Tenant(name = request.name,password = hashing.hash.bcypt(request.password))
    db.add(new_tenant)
    db.commit()
    db.refresh(new_tenant)
    return new_tenant

def get_tenant(id:int, db:Session = Depends(get_db)):
    tenant = db.query(models.Tenant).filter(models.Tenant.id == id).first()
    if not tenant:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Tenant with the id {id} is not available")
    return tenant

def update_tenant(id: int, request: schemas.CreateTenant, db: Session = Depends(get_db)):
    tenant = db.query(models.Tenant).filter(models.Tenant.id == id)
    if not tenant.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tenant with the id {id} is not available")
    tenant.update(
        name = request.name,
        password = hashing.hash.bcypt(request.password)
    )
    db.commit()
    return {"message": "Tenant Updated Successfully"}

def delete_tenant(id: int, db: Session = Depends(get_db)):
    tenant = db.query(models.Tenant).filter(models.Tenant.id == id)
    if not tenant.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tenant with the id {id} is not available")
    tenant.delete(synchronize_session=False)
    db.commit()
    return {"message": "Tenant Deleted Successfully"}
from fastapi import APIRouter
from ..utils.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from ..models import models
from ..schemas import schemas
from ..repository import tenant

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..utils.database import get_db
from ..models import models
from ..schemas import schemas
from ..repository import tenant
from ..utils import oauth2

router = APIRouter(
    tags=["tenant"],
    prefix="/tenant"
)

@router.post("/", dependencies=[Depends(oauth2.check_admin)])
def create_tenant(request: schemas.CreateTenant, db: Session = Depends(get_db)):
    return tenant.create_tenant(request, db)

@router.get("/", dependencies=[Depends(oauth2.check_admin)])
def get_all_tenants(db: Session = Depends(get_db)):
    return tenant.get_all_tenants(db)

@router.get("/{id}", dependencies=[Depends(oauth2.check_admin)])
def get_tenant(id: int, db: Session = Depends(get_db)):
    return tenant.get_tenant(id, db)

@router.put("/{id}", dependencies=[Depends(oauth2.check_admin)])
def update_tenant(id: int, request: schemas.CreateTenant, db: Session = Depends(get_db)):
    return tenant.update_tenant(id, request, db)

@router.delete("/{id}", dependencies=[Depends(oauth2.check_admin)])
def delete_tenant(id: int, db: Session = Depends(get_db)):
    return tenant.delete_tenant(id, db)
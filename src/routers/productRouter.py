from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..utils.database import get_db
from ..models import models
from ..schemas import schemas
from ..repository import product
from ..utils import oauth2

router = APIRouter(
    tags=["product"],
    prefix="/{tenant_name}/product"
)

@router.post("/", dependencies=[Depends(oauth2.get_current_user)])
def create_product(tenant_name: str, request: schemas.CreateProduct, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return product.create_product(tenant_name, request, db, current_user)

@router.get("/")
def get_all_products(tenant_name: str, db: Session = Depends(get_db)):
    return product.get_all_products(tenant_name, db)

@router.get("/{id}")
def get_product(tenant_name: str, id: int, db: Session = Depends(get_db)):
    return product.get_product(tenant_name, id, db)

@router.put("/{id}", dependencies=[Depends(oauth2.get_current_user)])
def update_product(tenant_name: str, id: int, request: schemas.CreateProduct, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return product.update_product(tenant_name, id, request, db, current_user)

@router.delete("/{id}", dependencies=[Depends(oauth2.get_current_user)])
def delete_product(tenant_name: str, id: int, db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    return product.delete_product(tenant_name, id, db, current_user)
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from ..models import models
from ..schemas import schemas

def create_product(tenant_name: str, request: schemas.CreateProduct, db: Session, current_user: models.User):
    tenant = db.query(models.Tenant).filter(models.Tenant.name == tenant_name).first()
    if not tenant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")
    if current_user.role != models.Roles.tenant or current_user.tenant_id != tenant.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not have permission to create products for this tenant")
    new_product = models.Product(
        name=request.name,
        category=request.category,
        quantity=request.quantity,
        tenant_id=tenant.id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_all_products(tenant_name: str, db: Session):
    tenant = db.query(models.Tenant).filter(models.Tenant.name == tenant_name).first()
    if not tenant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")
    return db.query(models.Product).filter(models.Product.tenant_id == tenant.id).all()

def get_product(tenant_name: str, id: int, db: Session):
    tenant = db.query(models.Tenant).filter(models.Tenant.name == tenant_name).first()
    if not tenant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")
    product = db.query(models.Product).filter(models.Product.id == id, models.Product.tenant_id == tenant.id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
    return product

def update_product(tenant_name: str, id: int, request: schemas.CreateProduct, db: Session, current_user: models.User):
    tenant = db.query(models.Tenant).filter(models.Tenant.name == tenant_name).first()
    if not tenant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")
    product = db.query(models.Product).filter(models.Product.id == id, models.Product.tenant_id == tenant.id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
    if current_user.role != models.Roles.tenant or current_user.tenant_id != tenant.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not have permission to update this product")
    product.name = request.name
    product.category = request.category
    product.quantity = request.quantity
    db.commit()
    db.refresh(product)
    return product

def delete_product(tenant_name: str, id: int, db: Session, current_user: models.User):
    tenant = db.query(models.Tenant).filter(models.Tenant.name == tenant_name).first()
    if not tenant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")
    product = db.query(models.Product).filter(models.Product.id == id, models.Product.tenant_id == tenant.id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found")
    if current_user.role != models.Roles.tenant or current_user.tenant_id != tenant.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You do not have permission to delete this product")
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted"}
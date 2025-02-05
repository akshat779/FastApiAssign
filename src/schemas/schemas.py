from typing import List,Optional
from pydantic import BaseModel
import enum

class Role(str, enum.Enum):
    admin="admin"
    tenant="tenant"
    user="user"


class UserBase(BaseModel):
    username: str
    name: str
    role: Role

class CreateUser(UserBase):
    password:str
    
class User(UserBase):
    id:int
    tenantId:Optional[int]

    class Config:
        orm_mode = True


class TenantBase(BaseModel):
    name: str

class CreateTenant(TenantBase):
    password:str

class Tenant(TenantBase):
    id:int
    users: List[User] = []

    class Config():
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    category:str
    quantity:int

class CreateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: int
    tenant_id:int
    
    class Config():
        orm_mode = True

class OrderItemBase(BaseModel):
    quantity:int

class CreateOrderItem(OrderItemBase):
    product_id:int

class OrderItem(OrderItemBase):
    id:int
    order_id:int
    product: Product

    class Config:
        orm_mode=True

class OrderBase(BaseModel):
    total_quantity:int
    total_amount:int

class CreateOrder(OrderBase):
    user_id:int

class Order(OrderBase):
    id: int
    user:User
    order_items: List[OrderItem] = []

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    user_id: Optional[str] = None

class LoginUser(BaseModel):
    username: str
    password: str
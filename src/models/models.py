from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,ForeignKey,Enum
from ..utils.database import Base
import enum

class Roles(enum.Enum):
    admin = "admin"
    tenant = "tenant"
    user = "user"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True, index = True)
    username = Column(String, unique=True,index=True)
    name = Column(String)
    password = Column(String)
    role = Column(Enum(Roles))
    tenant = relationship("Tenant",back_populates='users')
    tenant_id = Column(Integer,ForeignKey("tenants.id"))
    orders = relationship("Order",back_populates="users")


class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,unique=True, index=True)
    user =relationship("User",back_populates="tenants")
    products = relationship("Products",back_populates="tenants")
   
class Product(Base):
    __tabelname__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index = True)
    category = Column(String)
    quantity = Column(Integer)
    order_items = relationship("OrderItem",back_populates='products')
    tenant = relationship("Tenant",back_populates="products")
    tenant_id = Column(Integer, ForeignKey("tenants.id"))


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer,primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    total_quantity = Column(Integer)
    total_amount = Column(Integer)
    order_items = relationship("OrderItem", back_populates="orders")
    user = relationship("User",back_populates="orders")



class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index = True)
    quantity = Column(Integer)
    product_id = Column(Integer,ForeignKey("products.id"))
    product = relationship("Product",back_populates='order_items')
    order = relationship("Order",back_populates="order_items")
    order_id = Column(Integer, ForeignKey("orders.id"))
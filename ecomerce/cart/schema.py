from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

from ecomerce.products.schema import Product


class ShowCartItems(BaseModel):
    id: int
    products: Product
    created_date: datetime

    class Config:
        orm_mode = True


class ShowCart(BaseModel):
    id: int
    cart_items: List[ShowCartItems] = Field(default_factory=list)

    class Config:
        orm_mode = True

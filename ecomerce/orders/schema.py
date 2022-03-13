from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

from ecomerce.products.schema import ProductListing


class ShowOrderDetails(BaseModel):
    id: int
    order_id: int
    product_order_details: ProductListing

    class Config:
        orm_mode = True


class ShowOrder(BaseModel):
    id: Optional[int]
    order_date: datetime
    order_amount: float
    order_status: str
    shipping_address: str
    order_details: List[ShowOrderDetails] = Field(default_factory=list)

    class Config:
        orm_mode = True

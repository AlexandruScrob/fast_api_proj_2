from typing import List
from fastapi import APIRouter
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ecomerce import db
from ecomerce.auth.jwt import get_current_user
from . import services, schema


router = APIRouter(tags=["Orders"], prefix="/orders")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.ShowOrder)
async def initiate_order_processing(
    database: Session = Depends(db.get_db),
    current_user: schema.User = Depends(get_current_user),
):
    return await services.initiate_order(current_user, database)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schema.ShowOrder])
async def orders_list(
    database: Session = Depends(db.get_db),
    current_user: schema.User = Depends(get_current_user),
):
    return await services.get_order_listing(current_user, database)

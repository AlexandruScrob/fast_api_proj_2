from typing import List
from fastapi import HTTPException, status

from ecomerce.cart.models import Cart, CartItems
from ecomerce.orders.models import Order, OrderDetails
from ecomerce.user.models import User
from . import tasks


async def initiate_order(database) -> Order:
    # TODO change this workaround
    user_info = database.query(User).filter(User.email == "test@email.com").first()
    cart = database.query(Cart).filter(Cart.user_id == user_info.id).first()

    cart_items_objects = database.query(CartItems).filter(Cart.id == cart.id)

    if not cart_items_objects.count():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Items found in Cart!"
        )

    total_amount: float = sum(item.products.price for item in cart_items_objects)

    new_order = Order(
        order_amount=total_amount,
        customer_id=user_info.id,
        shipping_address="123 Test Street, Test City, New York",
    )

    database.add(new_order)
    database.commit()
    database.refresh(new_order)

    bulk_order_details_object: list = [
        OrderDetails(order_id=new_order.id, product_id=item.products.id)
        for item in cart_items_objects
    ]

    database.bulk_save_objects(bulk_order_details_object)
    database.commit()

    # Send Email
    tasks.send_email.delay("testemail@test.com")

    # clear items in the cart
    database.query(CartItems).filter(CartItems.cart_id == cart.id).delete()
    database.commit()

    return new_order


async def get_order_listing(database) -> List[Order]:
    # TODO change this workaround
    user_info = database.query(User).filter(User.email == "test@email.com").first()
    return (
        database.query(Order).filter(Order.customer_id == user_info.id).all()
    )  # orders

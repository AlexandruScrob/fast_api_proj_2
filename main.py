import uvicorn

from celery import Celery
from fastapi import FastAPI

from ecomerce.user import router as user_router
from ecomerce.products import router as product_router
from ecomerce.cart import router as cart_router
from ecomerce.orders import router as order_router
from ecomerce.auth import router as auth_router

from ecomerce import config


app = FastAPI(title="EcomerceApp", version="0.0.1", redoc_url=None)


app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)
app.include_router(auth_router.router)


# celery = Celery(
#     __name__,
#     broker=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}",
#     backend=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}",
# )


# celery.conf.imports = ["ecomerce.orders.tasks"]


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

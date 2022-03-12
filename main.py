from fastapi import FastAPI
import uvicorn

from ecomerce.user import router as user_router
from ecomerce.products import router as product_router
from ecomerce.cart import router as cart_router


app = FastAPI(title="EcomerceApp", version="0.0.1", redoc_url=None)


app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

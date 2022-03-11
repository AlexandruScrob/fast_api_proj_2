from fastapi import FastAPI
import uvicorn

from ecomerce.user import router as user_router

app = FastAPI(title="EcomerceApp", version="0.0.1")


app.include_router(user_router.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

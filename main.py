from fastapi import FastAPI


app = FastAPI(title="Sample Docs", description="Private Docs.", version=1.0)


@app.get("/")
async def root():
    return {"message": "Application is running."}

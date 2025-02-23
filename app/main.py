from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.status import router as status_router

app = FastAPI(title="Async Image Processing API")

app.include_router(upload_router, prefix="/upload")
app.include_router(status_router, prefix="/status")

@app.get("/")
def home():
    return {"message": "Welcome to Image Processing API"}

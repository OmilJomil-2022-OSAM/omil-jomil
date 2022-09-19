import uvicorn
from fastapi import FastAPI

from app.user import router as user_router
from app.camera import router as camera_router
from app.token import router as token_router


app = FastAPI()

app.include_router(token_router.router)
app.include_router(user_router.router)
app.include_router(camera_router.router)


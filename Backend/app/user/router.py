from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, FileResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session

from app.user.schema import UserDisplay, UserCreate
from app.user import crud
from core.db import get_db

router = APIRouter(
    prefix="/user",
    tags=["유저 관리"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })


@router.post("/create/", response_model=UserDisplay)
async def create(user: UserCreate = Depends(), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_uid(db, uid=user.uid)
    if db_user:
        raise HTTPException(status_code=400, detail="uid already registered")
    return crud.create_user(db=db, user=user)



@router.get("/read")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })


@router.get("/update")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })

@router.get("/delete")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })


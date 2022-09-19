from fastapi import APIRouter
from fastapi.responses import JSONResponse, FileResponse
from fastapi.requests import Request

router = APIRouter(
    prefix="/camera",
    tags=[" 카메라 관리 "],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })


@router.post("/create")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })

@router.get("/read")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })


@router.post("/update")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })

@router.post("/delete")
async def homepage(req: Request):
    return JSONResponse({
        'green': 'rain'
    })


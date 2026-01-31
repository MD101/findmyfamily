from fastapi import FastAPI, Response, Request
# from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
#from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from app.api.location import router as location_router
from uvicorn import run

geo = FastAPI()

#Register APIs
geo.include_router(location_router)

# Add CORS middleware
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://0.0.0.0",
    "http://0.0.0.0",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
]

geo.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

geo.mount("/public", StaticFiles(directory="public"), name="public")

@geo.get("/favicon.ico")
async def custom_favicon(request: Request):
    response = Response(content=open("public/favicon.ico", "rb").read(), media_type="image/x-icon")
    return response

@geo.get("/")
def read_root():
    return {"Message": "Welcome to FindMyFamily"}

if __name__ == "__main__":
    host = "localhost"
    port = 8080
    run("main:geo", host=host, port=port, reload=True)
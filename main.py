from fastapi import FastAPI, Response, Request
# from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/favicon.ico")
async def custom_favicon(request: Request):
    response = Response(content=open("public/favicon.ico", "rb").read(), media_type="image/x-icon")
    return response

@app.get("/")
def read_root():
    return {"Hello": "World"}

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", log_level="info", host="0.0.0.0", port=8000, reload=True)
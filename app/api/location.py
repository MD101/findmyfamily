from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter()

class LocationData(BaseModel):
    latitude: float
    longitude: float
    timestamp: int
    accuracy: float
    device_id: str

@router.post("/post_location")
async def post_location(request: Request):
    # Access the request method
    method = request.method
    print(f"Method: {method}")
    
    # Access the request URL
    url = request.url
    print(f"URL: {url}")
    
    # Access the request headers
    headers = request.headers
    print(f"Headers: {headers}")
    
    # Access the request cookies
    cookies = request.cookies
    print(f"Cookies: {cookies}")
    
    # Access the request query parameters
    query_params = request.query_params
    print(f"Query Parameters: {query_params}")
    
    # Access the request form data
    form_data = await request.form()
    print(f"Form Data: {form_data}")
    
    # Access the request JSON data
    json_data = await request.json()
    print(f"JSON Data: {json_data}")
    
    # Access the request body
    body = await request.body()
    print(f"Body: {body}")
    return {"Message": "Location received"}
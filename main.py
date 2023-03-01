import os
from fastapi import FastAPI
from pydantic import BaseModel
from fetch import fetchHTML
from scrape import go_scrape
from format_msg import get_format_msg
import uvicorn
from fastapi.responses import PlainTextResponse

app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get('/{plate}')
async def get_car_data(plate):
    print("PLATE: ", plate)
    if (plate is None
        or plate == ''
        or plate == 'favicon.ico'
            or len(plate) != 6):
        return {}
    html_string = fetchHTML(plate=plate, save_file=False)
    data = go_scrape(html_string)
    return data


@app.get('/demo/{plate}')
async def get_demo_car_data(plate):
    print("PLATE: ", plate)
    if (plate is None
        or plate == ''
        or plate == 'favicon.ico'
            or len(plate) != 6):
        return {}
    html_string = fetchHTML(plate=plate, save_file=False)
    data = go_scrape(html_string)
    custom_data = {
        "model": data['car_data'].get('modelo', ''),
        "brand": data['car_data'].get('marca', ''),
        "plate": data['car_data'].get('patente', ''),
        "year": data['car_data'].get('año', ''),
        "engine": data['car_data'].get('nmotor', ''),
        "chassis": data['car_data'].get('nchasis', '')
    }
    return custom_data


@app.get('/format/{plate}', response_class=PlainTextResponse)
async def get_format_message(plate):
    print("PLATE: ", plate)
    if (plate is None
        or plate == ''
        or plate == 'favicon.ico'
            or len(plate) != 6):
        return {}
    html_string = fetchHTML(plate=plate, save_file=False)
    data = go_scrape(html_string)
    msg = get_format_msg(data)
    return msg

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv("PORT", default=8000))
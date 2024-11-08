from fastapi import FastAPI
from enum import Enum


app = FastAPI()


@app.get("/")
def home():
    return "Hello"

@app.get('/hello')
def hello():
    return "Hello Sam.."

@app.get('/hello/{name}')
def hello(name):
    return f"Hello {name}.."

food_items = {
    "Indian": ["Samosa", "Dosa"],
    "American": ["Hot Dog", "Apple Pie"],
    "Italian": ["Ravioli", "Pizza"]
}

@app.get("/get_items/{cuisine}")
def get_items(cuisine):
    items = food_items.get(cuisine)
    if not items:
        return f"{cuisine} cuisine is not available"
    return items

class AvailableCuisines(str, Enum):
    indian = "Indian"
    american = "American"
    italian = "Italian"

@app.get("/get_item/{cuisine}")
def get_item(cuisine: AvailableCuisines):
    return food_items.get(cuisine)


coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_coupon(code: int):
    return {'discount_amount': coupon_code.get(code)}
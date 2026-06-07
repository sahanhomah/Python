from fastapi import FastAPI
from models import Products
app = FastAPI()


products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "description": "A high-performance laptop for work and play.", "quantity": 10},
    {"id": 2, "name": "Smartphone", "price": 499.99, "description": "A sleek smartphone with a powerful camera.", "quantity": 20},
]
@app.get("/")
def greet():
    return "Hello, and welcome to this !"

@app.get("/products")
def get_products():
    return products
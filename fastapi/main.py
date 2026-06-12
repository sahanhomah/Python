from fastapi import FastAPI
from models import Products
from database import session,engine
import database_models
from pydantic import BaseModel
app = FastAPI()
database_models.Base.metadata.create_all(bind=engine)

products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "description": "A high-performance laptop for work and play.", "quantity": 10},
    {"id": 2, "name": "Smartphone", "price": 499.99, "description": "A sleek smartphone with a powerful camera.", "quantity": 20},
]

def init_db():
    db = session()

    count =db.query(database_models.Products).count

    if count==0: 

         for product in products:
          db.add(database_models.Products(**product))
  



         db.commit()
    db.close()

init_db()    



@app.get("/")
def greet():
    return "Hello, and welcome to this !"

@app.get("/products")
def get_products():
    return products

@app.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product
    
    
    return " Product not found"

@app.post("/products")
def create_product(product: Products):
    products.append(product.model_dump())
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Products):
    for i in range(len(products)):
        if products[i]["id"] == id:
            products[i] = product.model_dump()
            return "Product updated successfully"
    return "Product not found"

@app.delete("/products/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i]["id"] == id:
            del products[i]
            return("successfully deleted")
    return("product not found")


       


    
from pydantic.dataclasses import dataclass
from pydantic import BaseModel

# Using dataclass
@dataclass
class Product:
    name: str
    price: float

# Using BaseModel
class ProductModel(BaseModel):
    name: str
    price: float

# Example
p1 = Product("Book", 200)  
p2 = ProductModel(name="Book", price="200")  # auto convert string → float

print(p1)   # Product(name='Book', price=200.0)
print(p2)   # name='Book' price=200.0

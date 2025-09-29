from pydantic import BaseModel

# Define model
class User(BaseModel):
    name: str
    age: int

# Example: validation + auto type conversion
data = {"name": "Noreen", "age": "22"}  # age string hai
user = User(**data)

print(user)  
# name='Noreen' age=22 (Pydantic converts string into intiger)

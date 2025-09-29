from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    is_active: bool

data = {"id": "101", "name": "Ali", "is_active": "true"}
student = Student(**data)

print(student)  
# id=101 name='Ali' is_active=True

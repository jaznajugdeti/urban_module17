# Схемы:
# Создайте 4 схемы в модуле schemas.py, наследуемые от BaseModel,
# для удобной работы с будущими объектами БД:
# Обратите внимание, что 1/2 и 3/4 схемы обладают одинаковыми атрибутами.
from pydantic import BaseModel

# CreateUser с атрибутами: username(str), firstname(str), lastname(str) и age(int)
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
# UpdateUser с атрибутами: firstname(str), lastname(str) и age(int)
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int
# CreateTask с атрибутами: title(str), content(str), priority(int)
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int
# UpdateTask с теми же атрибутами, что и CreateTask.
class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
from typing import List

from pydantic import BaseModel

l = [1, 2, 3]
d = {"a": 1, "b": 2, "c": 3}


class Address(BaseModel):
    city: str
    street: str


class Contact(BaseModel):
    phone: str
    work_phone: str


class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address
    contacts: List[Contact]


user = User(name="Andy", age=22, email="andy@mail.com",
            address=Address(city="New York", street="New York"),
            contacts=[Contact(phone="111", work_phone="222"), Contact(phone="333", work_phone="444")]
            )
print(user)
# Отримання словника
print(user.model_dump())
# Отримання JSON
print(type(user.model_dump_json()))
json_data = user.model_dump_json()

with open("user.json", "w") as f:
    f.write(json_data)

user_2 = User.model_validate_json(json_data)
print(type(user_2))
print(user_2)
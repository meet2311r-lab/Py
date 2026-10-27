from pydantic import BaseModel, EmailStr

class user(BaseModel):
    id: int
    name: str ="Meet Raval"
    signup_ts: str | None = None
    isactive:bool 
    email:EmailStr

objuser = user(id=1, name="Meet Raval", email="meet.raval@example.com")
print(objuser)

from pydantic import BaseModel

# Create Player Schema (Pydantic Model)
class PlayerCreate(BaseModel):
    name: str

# Complete Player Schema (Pydantic Model)
class Player(BaseModel):
    id: int


class Config:
    orm_mode = True
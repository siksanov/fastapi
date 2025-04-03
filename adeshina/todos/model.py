from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Read the next chapter of the book."
            }
        }
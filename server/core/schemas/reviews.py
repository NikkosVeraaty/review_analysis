from pydantic import BaseModel


class ReviewCreateSchema(BaseModel):
    text: str


class ReviewResponseSchema(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: str

from pydantic import BaseModel, Field


class Input(BaseModel):
    text: str = Field(..., min_length=1)

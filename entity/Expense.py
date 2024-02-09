from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Expense(BaseModel):
    exp_id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    amount: float
    date: datetime
    involved_people: str
    split_style: int
    category: str
    create_nm: str



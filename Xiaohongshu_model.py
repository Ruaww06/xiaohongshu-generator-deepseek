from pydantic import BaseModel
from typing import List

class Xiaohongshu(BaseModel):
    titles: List[str]
    content: str
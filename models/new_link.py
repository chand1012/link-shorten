from typing import Optional

from pydantic import BaseModel

class NewLink(BaseModel):
    link: str
    expire: Optional[int] = 86400
    resetExpireOnClick: Optional[bool] = False
    id: Optional[str]
    
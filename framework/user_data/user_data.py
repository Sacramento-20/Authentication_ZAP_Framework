from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path


class User(BaseModel):
    context: str
    url: List[str]
    url_login: Optional[str] = None
    exclude_urls: List[str] = []
    report_title: Optional[str] = "Report"
    login: str
    password: str

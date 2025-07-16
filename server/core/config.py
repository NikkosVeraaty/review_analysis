from pathlib import Path

from pydantic import BaseModel


class DBConfig(BaseModel):
    name: Path = Path(__file__).parent.parent.parent / "reviews.db"


class Config(BaseModel):
    db: DBConfig = DBConfig()
    

settings = Config()

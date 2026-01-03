from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Config(BaseSettings):
    app_name: str = "fast-api-project"
    debug: bool = False
    db_user: str = ""
    db_password: str = ""
    db_name: str = "test_db"

    @property
    def db_url(self) -> str:
        return f"sqlite:///./{self.db_name}"
    
config = Config()

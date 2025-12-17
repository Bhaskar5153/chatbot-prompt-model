# this model contains the configuration for the application.
from pydantic import BaseModel, Field
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Application settings configuration.
    """
    GOOGLE_API_KEY: str = os.getenv(key="GOOGLE_API_KEY", default="")

settings = Settings()


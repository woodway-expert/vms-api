from typing import List
from decouple import config


class Settings:
    # Database
    DATABASE_URL: str = config(
        "DATABASE_URL", default="mssql+pymssql://username:password@server/database"
    )

    # Security
    SECRET_KEY: str = config("SECRET_KEY", default="your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = config(
        "ACCESS_TOKEN_EXPIRE_MINUTES", default=30, cast=int
    )

    # Application
    DEBUG: bool = config("DEBUG", default=False, cast=bool)
    API_V1_STR: str = config("API_V1_STR", default="/api/v1")
    PROJECT_NAME: str = config("PROJECT_NAME", default="VMS API")

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = config(
        "BACKEND_CORS_ORIGINS",
        default="http://localhost:3000,http://localhost:8000",
        cast=lambda v: [i.strip() for i in v.split(",")],
    )

    # Pagination
    DEFAULT_PAGE_SIZE: int = config("DEFAULT_PAGE_SIZE", default=50, cast=int)
    MAX_PAGE_SIZE: int = config("MAX_PAGE_SIZE", default=1000, cast=int)


settings = Settings()

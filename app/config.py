from pydantic_settings import BaseSettings


class Settings(BaseSettings): 
    database_username: str
    database_password: str 
    database_host: str 
    
    secret_key: str 
    access_time_expire_minutes: int
    algorithm: str 

    class Config: 
        env_file = '.env'


settings = Settings()
import os

from dotenv import load_dotenv

class Config:
    def __init__(self) -> None:
        load_dotenv('.env')

        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        
        self.KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER")

CONFIG = Config()
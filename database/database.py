from sqlalchemy import create_engine, Connection, text
from os import getenv
from dotenv import load_dotenv


class Database:
    def __init__(self):
        self.engine = create_engine(f"postgresql+psycopg2://{getenv("USER")}:{getenv("PASSWORD")}@"
                                    f"{getenv("IP")}/{getenv("DB")}")

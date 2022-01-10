from dotenv import load_dotenv
from os import environ as e

load_dotenv(".env")

class UnitsConfig:
    PORT = 8000

class UnitsPropConfig(UnitsConfig):
    PORT = 8000
    SWAGGER_UI = False
    SQLALCHEMY_DATABASE_URI = e.get("DATABASE_URI")
    SQLALCHEMY_ECHO = False

class UnitsTestConfig(UnitsConfig):
    PORT = 8000
    SWAGGER_UI = True
    SQLALCHEMY_DATABASE_URI = e.get("TESTING_DATABASE_URI")
    SQLALCHEMY_ECHO = True

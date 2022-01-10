import logging
import pathlib
import sqlalchemy
from sqlalchemy.orm import Session
import connexion

app = connexion.FlaskApp(__name__, specification_dir="openapi/")

# Expose the bare FlaskApp for use by our WSGI
application = app.app


SQLALCHEMY_ECHO = True
DATABASE_URI = "sqlite+pysqlite:///:memory:"

# Initialize the database connection
db = sqlalchemy.create_engine(DATABASE_URI, echo=SQLALCHEMY_ECHO)
session = Session(db)

# Load in our model
from models import UnitModel

if __name__ == "__main__":
    app.add_api("units-service.yaml")
    app.run(port=UnitsConfig.port)

import logging
import pathlib
import sqlalchemy
import connexion

from config import UnitsConfig

app = connexion.FlaskApp(__name__, specification_dir="openapi/")

if __name__ == "__main__":
    app.add_api("units-service.yaml")
    app.run(port=UnitsConfig.port)

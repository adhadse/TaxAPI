from flask_migrate import Migrate
from app import app
from flask.cli import FlaskGroup
from app.main.database import db

migrate = Migrate()
migrate.init_app(app, db)

cli = FlaskGroup(app)

if __name__ == '__main__':
  cli()

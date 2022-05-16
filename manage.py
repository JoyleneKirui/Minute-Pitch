from app import app, db
from flask_migrate import Migrate

migrate = Migrate()


def create_app():
    migrate.init_app(app, db)

if __name__ == '__main__':
    app.run(debug=True)

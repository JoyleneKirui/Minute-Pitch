from app import app, db
from flask_migrate import Migrate, MigrateCommand

if __name__ == '__main__':
    app.run(debug=True)

migrate = Migrate(app, db)
manager.add_command('db',MigrateCommand)
# import app object from our app package
from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

app = create_app()

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# invokes the run method to start the server
if __name__ == "__main__":
    manager.run()
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])

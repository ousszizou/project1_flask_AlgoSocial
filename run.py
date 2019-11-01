# import app object from our app package
from app import app, manager

# invokes the run method to start the server
if __name__ == "__main__":
    manager.run()
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])

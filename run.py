# import app object from our app package
from app import app

# invokes the run method to start the server
app.run(port=app.config['PORT'], debug=app.config['DEBUG'])

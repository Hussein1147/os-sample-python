from flask import Flask
application = Flask(__name__)

from routes import app as application

if __name__ == "__main__":
    application.run()

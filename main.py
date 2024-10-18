from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    if os.getnev("database_url"):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("database_url")
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{DB_NAME}'
    
    
    

# @app.route('/')
# def index():
#     return 'Hello World.'

# if __name__ == '__main__':
#     app.run(debug=True)
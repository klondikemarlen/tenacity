from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_json import FlaskJSON
# from flask_sslify import SSLify  # currently doesn't support factory pattern

# Initialize database
db = SQLAlchemy()
flask_bcrypt = Bcrypt()
flask_json = FlaskJSON()
# flask_sslify = SSLify()

import datetime

from tenacity import app, db, bcrypt
from tenacity.model.base import Base


class Account(Base):
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(192), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email

        pass_hash = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS'))
        self.password_hash = pass_hash.decode()
        self.registered_on = datetime.datetime.now()
        self.admin = admin

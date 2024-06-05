from werkzeug.security import generate_password_hash, check_password_hash
from optionsinsight.Backend.Infrastructure.Data.User_DB_Gateway import db
from flask_login import UserMixin

class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def verify_password(self, input_password):
        return check_password_hash(self.password_hash, input_password)

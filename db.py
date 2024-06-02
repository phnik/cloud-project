from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Cấu hình chuỗi kết nối đến cơ sở dữ liệu MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://main:lab-password@lab-db.ckmiiql3dhdn.us-east-1.rds.amazonaws.com:3306/lab'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    message = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Idol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    vote_count = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f'<Idol {self.name}>'

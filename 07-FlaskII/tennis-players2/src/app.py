from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config["SQLACHEMY_DATABASE_URI"] = \
  "mysql+pymysql://root:password@localhost/tennis_players"

db = SQLAlchemy(app)


class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return "<Name %r>" % self.name

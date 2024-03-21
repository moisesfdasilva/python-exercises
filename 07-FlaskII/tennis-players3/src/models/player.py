from src.database import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)

    def __init__(self, name, description):
        self.name = name
        self.description = description

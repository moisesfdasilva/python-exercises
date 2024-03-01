from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = \
  "mysql://root:password@127.0.0.1:3306/tennis_players_database"
db = SQLAlchemy(app)


class TennisPlayer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def to_json(self) -> str:
        player_dict = {"id": self.id, "nome": self.name}
        return json.dumps(player_dict)


@app.route("/players", methods=["GET"])
def get_all():
    players = TennisPlayer.query.all()
    players_json = [usuario.to_json() for usuario in players]

    return Response(players_json)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

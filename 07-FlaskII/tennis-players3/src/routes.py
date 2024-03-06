# from blog import blog
from flask import render_template
from src.models.player import Player


@blog.route("/players")
def get_players():
    players = Player.query.all()
    return render_template(
        "src/templates/index.html", players=players)

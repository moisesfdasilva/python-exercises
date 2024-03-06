# mysql configuration
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "password"
MYSQL_DB = "tennis_players_database"

SQLALCHEMY_DB_URI = \
  f"mysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}/{MYSQL_DB}"

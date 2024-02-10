from pymongo import MongoClient
from os import environ


client = MongoClient(environ.get("MONGO_URL"))

db = client.db_students

db.students.insert_many([
    {"name": "Iga Swiatek", "register": "001"},
    {"name": "Aryna Sabalenka", "register": "002"},
    {"name": "Coco Gauff", "register": "003"}])

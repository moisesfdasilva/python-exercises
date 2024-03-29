from pymongo import MongoClient
from os import environ


client = MongoClient(environ.get("MONGO_URL"))

db = client.db_students

students_list = [
    {"name": "Iga Swiatek", "register": "001"},
    {"name": "Aryna Sabalenka", "register": "002"},
    {"name": "Coco Gauff", "register": "003"},
    {"name": "Jessica Pegula", "register": "004"},
    {"name": "Elena Rybakina", "register": "005"},
    {"name": "Ons Jabeur", "register": "006"},
    {"name": "Qinwen Zheng", "register": "007"},
    {"name": "Marketa Vondrousova", "register": "008"},
    {"name": "Maria Sakkari", "register": "009"},
    {"name": "Karolina Muchova", "register": "010"},
    {"name": "Jelena Ostapenko", "register": "011"},
    {"name": "Barbora Krejcikova", "register": "012"},
    {"name": "Beatriz Haddad Maia", "register": "013"},
    {"name": "Daria Kasatkina", "register": "014"},
    {"name": "Liudmila Samsonova", "register": "015"},
    {"name": "Veronika Kudermetova", "register": "016"},
    {"name": "Madison Keys", "register": "017"},
    {"name": "Petra Kvitova", "register": "018"},
    {"name": "Ekaterina Alexandrova", "register": "019"},
    {"name": "Elina Svitolina", "register": "020"},
]

db.students.insert_many(students_list)

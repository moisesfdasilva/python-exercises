# python3 -m venv .venv && source .venv/bin/activate
# python3 -m pip install pymongo

from pymongo import MongoClient

client = MongoClient()
db = client.catalogue
book = {
    "title": "A Light in the Attic",
}
document_id = db.books.insert_one(book).inserted_id
print(document_id)
client.close()  # fecha a conexão com o banco de dados

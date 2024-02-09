from .db import db


class StudentsModel():
    _collection = db['students']

    def __init__(self, data):
        self.data = data
        self.initial_charge()

    @classmethod
    def get_all(self):
        data = self._collection.find()
        return data

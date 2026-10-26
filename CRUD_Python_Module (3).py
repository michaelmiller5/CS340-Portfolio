# CRUD_Python_Module.py
# Full CRUD operations (Create, Read, Update, Delete) for the Animal
# collection in the aac MongoDB database.

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for the 'animals' collection in the 'aac' MongoDB database."""

    def __init__(self, username, password):
        # Connection variables. The username and password are passed in by the
        # caller (for example, the dashboard's authentication fields) so the
        # account used to connect is supplied at runtime instead of hardcoded.
        # The aacuser account lives in the admin database, so authentication
        # resolves against admin by default because no database is named in the URI.
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize the MongoClient, then bind to the target database and collection.
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        """
        Insert a document into the animals collection.
        :param data: dictionary of key/value pairs to insert.
        :return: True if the insert was acknowledged, False on failure.
        """
        if data is not None:
            try:
                result = self.database.animals.insert_one(data)
                return result.acknowledged
            except PyMongoError as error:
                print("Insert failed: %s" % error)
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, query):
        """
        Query documents from the animals collection.
        :param query: dictionary of key/value lookup pair(s) for the find() call.
        :return: list of matching documents, or an empty list if none found or on failure.
        """
        if query is not None:
            try:
                cursor = self.database.animals.find(query)
                return list(cursor)
            except PyMongoError as error:
                print("Read failed: %s" % error)
                return []
        else:
            raise Exception("Nothing to read, because query parameter is empty")

    def update(self, query, new_values):
        """
        Update document(s) in the animals collection.
        :param query: dictionary selecting which documents to change.
        :param new_values: dictionary of key/value pairs to set on the matched documents.
        :return: the number of documents modified; 0 if none matched or on failure.
        """
        if query is not None and new_values is not None:
            try:
                result = self.database.animals.update_many(query, {"$set": new_values})
                return result.modified_count
            except PyMongoError as error:
                print("Update failed: %s" % error)
                return 0
        else:
            raise Exception("Nothing to update, because query or new_values parameter is empty")

    def delete(self, query):
        """
        Delete document(s) from the animals collection.
        :param query: dictionary selecting which documents to remove.
        :return: the number of documents removed; 0 if none matched or on failure.
        """
        if query is not None:
            try:
                result = self.database.animals.delete_many(query)
                return result.deleted_count
            except PyMongoError as error:
                print("Delete failed: %s" % error)
                return 0
        else:
            raise Exception("Nothing to delete, because query parameter is empty")
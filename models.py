from flask_pymongo import PyMongo
from bson.objectid import ObjectId

def setup_mongo(app):
    app.config["MONGO_URI"] = "mongodb+srv://helpyourassistant:pqam0Mwv3Vwv8Off@cluster0.qc3bq.mongodb.net/book-store?retryWrites=true&w=majority&appName=Cluster0"
    mongo = PyMongo(app)
    return mongo

# Model functions

def get_books_by_genre(mongo, genre=None):
    query = {"category": genre} if genre else {}
    return list(mongo.db.books.find(query))

def get_book(mongo, book_id):
    return mongo.db.books.find_one({"_id": ObjectId(book_id)})

def create_order(mongo, order_data):
    return mongo.db.orders.insert_one(order_data)

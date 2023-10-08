from decouple import config
from mongo_db.mongo_connection import Mongo


if __name__ == "__main__":
    credentials = {
        "user": config("MONGO_USERNAME"),
        "password": config("MONGO_PASSWORD"),
        "host": config("MONGO_HOST"),
        "port": config("MONGO_PORT"),
        "db_name": config("MONGO_DBNAME"),
    }
    mongo_obj = Mongo(credentials=credentials)
    mongo_obj.connect_to_mongo()
    value = {"key": "Value", "AnotherKey": "AnotherValue"}
    my_db = mongo_obj.get_connection()
    my_collection = my_db["NEW_COLLECTION"]
    my_collection.insert_one(value)

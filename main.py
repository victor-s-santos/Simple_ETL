from pymongo import MongoClient
from decouple import config
import pandas as pd


credentials = {"user": config("MONGO_USERNAME"), "password": config("MONGO_PASSWORD")}
connection_config = (
    f"mongodb://{credentials['user']}:{credentials['password']}@localhost:27017/"
)
my_val = {"Key": "Value2", "AnotherKey": "AnotherValue"}

if __name__ == "__main__":
    myclient = MongoClient(connection_config)
    my_db = myclient["DATABASE"]
    my_collection = my_db["COLLECTION"]
    my_collection.insert_one(my_val)

from decouple import config
from mongo_db.mongo_connection import Mongo
from handle_csv.main import generate_list_of_dictionaries
import os

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
    file_name = "FastFoodNutritionMenu.csv"
    path_of_csv_file = f"{os.getcwd()}/input_files/{file_name}"
    list_of_values = generate_list_of_dictionaries(path_of_csv_file)
    for value in list_of_values:
        my_collection.insert_one(value)
    print(f"{len(list_of_values)} records has been inserted!")

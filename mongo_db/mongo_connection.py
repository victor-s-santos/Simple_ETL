from pymongo import MongoClient, database, mongo_client
from decouple import config


class Mongo:
    def __init__(self, credentials: dict) -> None:
        """Class to handle mongodb connection object

        Args:
            credentials (dict): The database credentials
        """
        self.credentials = credentials
        self.connection_config = f"mongodb://{self.credentials['user']}:{self.credentials['password']}@{self.credentials['host']}:{self.credentials['port']}/"
        self.client = None
        self.db_connection = None

    def connect_to_mongo(self) -> None:
        """Make the mongodb connection"""
        self.client = MongoClient(self.connection_config)
        self.db_connection = self.client[self.credentials["db_name"]]

    def get_connection(self) -> database.Database:
        """Get the mongodb connection object

        Returns:
            database.Database: The client object of the respective db_name
        """
        return self.db_connection

    def get_client(self) -> mongo_client.MongoClient:
        """Get the mongodb client object

        Returns:
            mongo_client.MongoClient: The client object
        """
        return self.client


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
    connection_obj = mongo_obj.get_connection()
    client_obj = mongo_obj.get_client()

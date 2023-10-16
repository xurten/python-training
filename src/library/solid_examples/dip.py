# 5. Dependency Inversion Principle (DIP):
#
# Description:
# The Dependency Inversion Principle (DIP) states that high-level modules should not depend on
#                                          low-level modules; both should depend on abstractions.
#                                          Abstractions should not depend on details; details should depend on abstractions.
#
# Benefits:
#
# Decoupling: DIP reduces direct dependencies between modules, which makes it easier to swap out
#             implementations without affecting other parts of the system.
#
# Testability: By using interfaces or abstract classes, it becomes easier to create mock or stub
#              implementations for testing purposes.
#
# Flexibility: DIP enables a more flexible architecture that supports a wider range of configurations and implementations.
import logging


class Database:
    def __init__(self):
        # initialize database connection here
        pass

    def get_data(self, table_name, columns):
        pass

    def close(self):
        # code to close the database connection
        pass

    def get_data(self):
        try:
            # code to retrieve data from the database
            pass
        except Exception as e:
            logging.error(f"Error retrieving data from the database: {str(e)}")
            # handle the error appropriately, e.g., retry, log, or raise a custom exception

    def insert_data(self, data):
        pass

    def update_data(self, data):
        pass

    def delete_data(self, data):
        pass


class DataManager:
    def __init__(self, database):
        self.database = database

    def fetch_data(self):
        return self.database.get_data()


# database = Database()
# data_manager = DataManager(database)
# data = data_manager.fetch_data()

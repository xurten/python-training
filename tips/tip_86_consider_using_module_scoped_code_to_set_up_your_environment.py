# Tip 86 consider using module-scoped code to set up your environment
# good to have different configurations for different environments, you  can use modules sys and os
import __main__
import sys

# file dev_main.py
#TESTING = True
#import db_connection
#db = db_connection.Database()

# file prod_main.py
#TESTING = False
#import db_connection
#db = db_connection.Database()


class TestingDatabase:
    pass


class RealDatabase:
    pass


class Win32Database:
    pass


class PosixDatabase:
    pass


Database = None

if __main__.TESTING:
    Database = TestingDatabase
else:
    Database = TestingDatabase

if sys.platform.startswith('win32'):
    Second_Database = Win32Database
else:
    Second_Database = PosixDatabase

if __name__ == '__main__':
    pass

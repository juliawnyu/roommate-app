import sqlite3

from pymongo import MongoClient
from dotenv import load_dotenv
import os
import bcrypt

load_dotenv()

MONGO_ENV = os.environ.get("MONGO_ENV", "LOCAL")
# MONGO_URL = os.environ.get("MONGO_URL")
DB = "DB"
USERS = "USERS"

# This is our MongoDB manager class to be used for prod
class DB_Manager:
    def __init__(self):
        if MONGO_ENV == "LOCAL":
            self.client = MongoClient()
        elif MONGO_ENV == "REMOTE":
            self.client = MongoClient(MONGO_URL)
        self.db = self.client[DB]
        self.users = self.db[USERS]

    def reset_db(self):
        for collection in self.db.list_collections():
            collection.drop()

    def get_user(self, netID):
        search = self.users.find_one({'netID': netID})
        if search:
            return search
        return False

    def add_user(self, netID, password, grade):
        new_user = {'netID': netID,
                    'password': bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
                    'grade': grade}
        self.users.insert_one(new_user)

    def login_correct(self, netID, password):
        user = self.get_user(netID)
        if bcrypt.checkpw(password.encode(), user['password']):
            return True
        return False

#test code
# if MONGO_ENV == "LOCAL":
#     db = DB_Manager()
    
#     new_user = {'netID': 'kip218',
#                 'password': '1234',
#                 'grade': 'senior'}

#     print("Getting user...")
#     print(db.get_user('kip218'))

#     print("adding user")
#     db.add_user('kip218', '1234', 'senior')

#     print("Getting user...")
#     print(db.get_user('kip218'))

#     print("checking login")
#     print(db.login_correct('kip218', '1234'))
#     print(db.login_correct('kip218', '1232'))


db_file = 'database.db'

# This is a temporary DB class for SQLite3
class DB_Users:
    def __init__(self):
        self.con = sqlite3.connect(db_file, check_same_thread=False)
        self.cur = self.con.cursor()
        self.reset_table()

    # Create new users table - reset table if it already exists
    # Only use for setting up db environment locally for testing
    def reset_table(self):
        self.cur.execute("DROP TABLE IF EXISTS users")
        self.cur.execute("CREATE TABLE users(netID, password, grade)")

    # Fetch all from users table
    def fetch_all(self):
        res = self.cur.execute("SELECT * FROM users")
        return res.fetchall()

    # Add new user into users table
    # Todo - store password hash instead of plaintext
    # Todo - check if user account already exists
    def add_new_user(self, netID, password, grade):
        args = (netID, password, grade)
        try:
            self.cur.execute("INSERT INTO users VALUES (?, ?, ?)", args)
            self.con.commit()
        except Exception as error:
            print(f"Error in add_new_user(): {error}")
            return False
        return True

    # Retrieve user info for login
    def check_login(self, netID, password):
        args = (netID, password)
        try:
            res = self.cur.execute(
                "SELECT * FROM users WHERE netID=? AND password=?", args)
            res = res.fetchall()
        except Exception as error:
            print(f"Error in check_login(): {error}")
            return False

        # only return True if login attempt retrieves a single user account
        if len(res) == 1:
            return True
        else:
            return False

    # Check if user already exists
    def user_exists(self, netID):
        args = (netID)
        try:
            res = self.cur.execute(
                "SELECT * FROM users WHERE netID=?", args)
            res = res.fetchall()
        except Exception as error:
            print(f"Error in check_login(): {error}")
            return False

        # return true if user netID exists in database
        if len(res) >= 1:
            return True
        else:
            return False


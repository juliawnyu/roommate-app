import sqlite3

# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv

# load_dotenv()

# MONGO_ENV = os.environ.get("MONGO_ENV", "LOCAL")
# DB = "DB"
# USERS = "USERS"

# if MONGO_ENV == "LOCAL":
#     client = MongoClient()
#     db = client[DB]
#     new_user = {'username': 'kip218',
#                 'password': '1234'}

#     print("printing db contents")
#     for item in db[USERS].find():
#         print(item)

#     print("adding new user...")
#     db[USERS].insert_one(new_user)

#     print("printing db contents")
#     for item in db[USERS].find():
#         print(item)

#     db[USERS].drop()
# print('done')


db_file = 'database.db'


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

# Testing db setup
# db_users = DB_Users(db_file)
# db_users.reset_table()
# db_users.add_new_user('kip218', 'password123', 'Senior')
# print(db_users.fetch_all_users())

from pymongo import MongoClient
from dotenv import load_dotenv
import os
import bcrypt

load_dotenv()

MONGO_ENV = os.environ.get("MONGO_ENV", "LOCAL")
MONGO_URL = os.environ.get("MONGO_URL")
DB = "DB"
USERS = "USERS"


# This is our MongoDB manager class to be used for prod
class DB_Manager:
    def __init__(self):
        if MONGO_ENV == "LOCAL":
            self.client = MongoClient()
        elif MONGO_ENV == "REMOTE":
            self.client = MongoClient(
                                MONGO_URL,
                                connectTimeoutMS=30000,
                                socketTimeoutMS=None,
                                connect=False,
                                maxPoolsize=1)
        self.db = self.client[DB]
        self.users = self.db[USERS]

    def reset_db(self):
        self.client.drop_database(self.db)

    def get_user(self, netID):
        search = self.users.find_one({'netID': netID})
        if search:
            return search
        return False

    def add_user(self, netID, password, grade):
        new_user = {'netID': netID,
                    'password': bcrypt.hashpw(
                                password.encode(),
                                bcrypt.gensalt()),
                    'grade': grade}
        self.users.insert_one(new_user)

    def add_quiz_results(self, netID, sleep, guests, clean, gender, animal,
                         sharing):
        quiz_results = {
            'sleep': sleep,
            'guests': guests,
            'clean': clean,
            'gender': gender,
            'animal': animal,
            'sharing': sharing,
        }

        self.users.update_one(
            {'netID': netID},
            {'$set': {'quiz_results': quiz_results}}
        )

    def remove_user(self, netID):
        self.users.delete_one({'netID': netID})

    def login_correct(self, netID, password):
        user = self.get_user(netID)
        if bcrypt.checkpw(password.encode(), user['password']):
            return True
        return False

# test code
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

#     print("resetting db")
#     db.reset_db()

#     print("Getting user...")
#     print(db.get_user('kip218'))


# test remote connection
# if MONGO_ENV == "REMOTE":
#     db = DB_Manager()

#     print("Getting user...")
#     print(db.get_user('kip218'))

#     print("checking login")
#     print(db.login_correct('kip218', '1234'))
#     print(db.login_correct('kip218', '1232'))

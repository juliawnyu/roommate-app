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
    
    def get_matched_users(self, netID):
        user_in_session = self.get_user(netID)
        return user_in_session.get('matched_users')

    def get_all(self):
        return list(self.users.find({}))

    def add_user(self, netID, password, grade):
        new_user = {'netID': netID,
                    'password': bcrypt.hashpw(
                                password.encode(),
                                bcrypt.gensalt()),
                    'grade': grade}
        self.users.insert_one(new_user)

    def add_quiz_results(self, netID, sleep, guests, clean, gender, animal,
                         sharing, shower, alcohol, home):
        quiz_results = {
            'sleep': sleep,
            'guests': guests,
            'clean': clean,
            'gender': gender,
            'animal': animal,
            'sharing': sharing,
            'shower': shower,
            'alcohol': alcohol,
            'home': home,
        }

        self.users.update_one(
            {'netID': netID},
            {'$set': {'quiz_results': quiz_results}}
        )

    def add_matched_users(self, netID, matched_users):
        self.users.update_one(
            {'netID': netID},
            {'$set': {'matched_users': matched_users}}
        )

    def remove_user(self, netID):
        self.users.delete_one({'netID': netID})

    def login_correct(self, netID, password):
        user = self.get_user(netID)
        if bcrypt.checkpw(password.encode(), user['password']):
            return True
        return False

    def compare_answers(user_results, other_results):
        '''
        Helper function that directly compares quiz results.
        Loops through both dictionaries and compares answers.
        Returns list containing the keys of the common results.
        '''
        common_answers = []
        for key in user_results:
            if user_results[key] == other_results[key]:
                common_answers.append(key)
        return common_answers

    def compare_users(self, netID):
        '''
        Compares user with others to find matches.
        If 1+ quiz answer is the same, adds them to matched_users dictionary.
        Keys of matched dictionary are netIDs of users they share answers with.
        Key items is the list of common quiz_results keys.
        '''
        user_in_session = self.get_user(netID)
        user_in_session_quiz_results = user_in_session.get('quiz_results')
        users = self.get_all()
        matched_users = {}
        for curr_usr in users:
            if curr_usr is not user_in_session:
                curr_usr_quiz_results = curr_usr.get('quiz_results')
                common_answers = self.compare_answers(
                    user_in_session_quiz_results,
                    curr_usr_quiz_results
                )
                if common_answers:
                    matched_users[curr_usr.get('netID')] = common_answers
                    self.add_matched_users(netID, matched_users)
                else:
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

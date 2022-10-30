# Temporary db setup using sqlite3.
# Once MongoDB is set up, we will change to MongoDB.

import sqlite3


db_file = 'database.db'


class DB_Users:
    def __init__(self):
        self.con = sqlite3.connect(db_file, check_same_thread=False)
        self.cur = self.con.cursor()

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
    def add_new_user(self, netID, password, grade):
        args = (netID, password, grade)
        try:
            self.cur.execute("INSERT INTO users VALUES (?, ?, ?)", args)
            self.con.commit()
        except sqlite3.Error as error:
            print(f"Error adding new user: {error}")
            return error


# Testing db setup
# db_users = DB_Users(db_file)
# db_users.reset_table()
# db_users.add_new_user('kip218', 'password123', 'Senior')
# print(db_users.fetch_all_users())

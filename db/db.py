import sqlite3

db_file = 'database.db'

class DB_Manager:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file)
        self.cur = self.con.cursor()

    # Create new users table - reset table if it already exists
    def create_users_table(self):
        self.cur.execute("DROP TABLE IF EXISTS users")
        self.cur.execute("CREATE TABLE users(netID, password, grade)")

    # Fetch all from users table
    def fetch_all_users(self):
        res = self.cur.execute("SELECT * FROM users")
        return res.fetchall()

    # Add new user into users table
    def add_new_user(self, netID, password, grade):
        args = (netID, password, grade)
        try:
            self.cur.execute("INSERT INTO users VALUES (?, ?, ?)", args)
        except sqlite.Error as error:
            print(f"Error while adding new user: {error}")


# Testing db setup
# db_manager = DB_Manager(db_file)
# db_manager.create_users_table()
# db_manager.add_new_user('kip218', 'password123', 'Senior')
# print(db_manager.fetch_all_users())


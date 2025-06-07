import sqlite3
from config import DATABASE

class DB:
    def __init__(self, database):
        self.database = database
    
    def create_table(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS database (
                                university_id INTEGER PRIMARY KEY,
                                university_name TEXT                              
                            )''')
            conn.commit()
        conn.close()

if __name__ == '__main__':
    manager = DB(DATABASE)
    manager.create_table()
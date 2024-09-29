import os
import pickle
import sqlite3

def bad_sql_query(user_id):
    # Vulnerable query construction
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Directly injecting user input into SQL query (BAD PRACTICE)
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)

    return cursor.fetchall()


def command_exec(filename):
    # Vulnerable to command injection
    os.system(f"cat {filename}")


def vulnerable_deserialize(data):
    # Insecure deserialization
    obj = pickle.loads(data)
    return obj

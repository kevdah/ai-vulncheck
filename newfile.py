import os
import pickle
import sqlite3

def bad_sql_query():
    # Vulnerable query construction
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Directly injecting user input into SQL query (BAD PRACTICE)
    input("Enter user ID:")
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)

    return cursor.fetchall()


def command_exec():
    # Vulnerable to command injection
    input("Enter filename:")
    os.system(f"cat {filename}")


def vulnerable_deserialize(data):
    # Insecure deserialization
    obj = pickle.loads(data)
    return obj

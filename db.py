import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

# tg_id bigint,
# questions blob,
# timezone text,
# history blob

cursor.execute(f'''CREATE TABLE users (
    tg_id bigint,
    timezone text,
    questions blob,
    history blob
)''')

connection.commit()
connection.close()

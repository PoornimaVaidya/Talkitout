import sqlite3

def init_db():
    conn = sqlite3.connect('psychebot.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS chats (id INTEGER PRIMARY KEY, user_input TEXT, bot_response TEXT)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()

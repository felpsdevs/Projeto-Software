import sqlite3

def create_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()
    print("Banco ok.")

if __name__ == "__main__":
    create_db()

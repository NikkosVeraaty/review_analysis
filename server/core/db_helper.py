import sqlite3


def create_reviews_table(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
    ''')
    connection.commit()

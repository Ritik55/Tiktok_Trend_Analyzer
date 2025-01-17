import sqlite3

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('tiktok_trends.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS trends (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                trend_terms TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save_trends(self, trends):
        cursor = self.conn.cursor()
        for trend in trends:
            trend_terms = ','.join(trend)
            cursor.execute('INSERT INTO trends (trend_terms) VALUES (?)', (trend_terms,))
        self.conn.commit()

    def get_recent_trends(self, limit=10):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM trends ORDER BY timestamp DESC LIMIT ?', (limit,))
        return cursor.fetchall()

    def close(self):
        self.conn.close()

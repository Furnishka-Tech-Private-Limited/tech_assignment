import sqlite3
import os

class LeadDB:
    def __init__(self, db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS seen_leads(
              lead_id TEXT PRIMARY KEY
            )
            """
        )
        self.conn.commit()

    def is_seen(self, lead_id):
        cur = self.conn.execute("SELECT 1 FROM seen_leads WHERE lead_id=?", (lead_id,))
        return cur.fetchone() is not None

    def mark_seen(self, lead_id):
        self.conn.execute(
            "INSERT OR IGNORE INTO seen_leads(lead_id) VALUES(?)", (lead_id,)
        )
        self.conn.commit()

# app/checkpoint_store.py

import sqlite3
import json
import os

DB_PATH = "checkpoints.db"

class CheckpointStore:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS checkpoints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id TEXT,
            state_blob TEXT,
            review_url TEXT,
            status TEXT
        );
        """)
        self.conn.commit()

    def save_checkpoint(self, invoice_id, state):
        state_json = json.dumps(state)
        review_url = f"/human-review/review/{invoice_id}"

        cursor = self.conn.execute(
            "INSERT INTO checkpoints (invoice_id, state_blob, review_url, status) VALUES (?, ?, ?, ?)",
            (invoice_id, state_json, review_url, "PENDING")
        )
        self.conn.commit()
        return cursor.lastrowid, review_url

    def list_pending(self):
        rows = self.conn.execute(
            "SELECT id, invoice_id, review_url FROM checkpoints WHERE status='PENDING'"
        ).fetchall()
        return rows

    def get_state(self, checkpoint_id):
        row = self.conn.execute(
            "SELECT state_blob FROM checkpoints WHERE id=?", (checkpoint_id,)
        ).fetchone()

        return json.loads(row[0]) if row else None

    def resolve_checkpoint(self, checkpoint_id, decision):
        self.conn.execute(
            "UPDATE checkpoints SET status=? WHERE id=?",
            (decision, checkpoint_id)
        )
        self.conn.commit()

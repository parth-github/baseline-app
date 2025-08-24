# buggy_calculator_for_mock.py
import requests
import time
import sqlite3


class BuggyCalculator:
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path

    def add(self, a, b):
        """
        Calls an external API to perform addition.
        (Bug: adds +1 to the result)
        """
        resp = requests.get(f"http://math-api.local/add/{a}/{b}")
        result = resp.json()["result"]
        return result + 1  # intentional bug

    def multiply(self, a, b):
        """
        Stores multiplication result in a database before returning.
        """
        result = a * b
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS results (op TEXT, value INT)")
        cur.execute("INSERT INTO results VALUES (?, ?)", ("multiply", result))
        conn.commit()
        conn.close()
        return result

    def current_time(self):
        """
        Returns current epoch time from system clock.
        """
        return int(time.time())

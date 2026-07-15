import sqlite3
from pathlib import Path

db = Path(__file__).resolve().parents[1] / 'db.sqlite3'
print('DB file:', db)
conn = sqlite3.connect(str(db))
cur = conn.cursor()
try:
    cur.execute('SELECT id, username, password, email FROM delivery_customer')
    rows = cur.fetchall()
    if not rows:
        print('No customers found')
    else:
        for r in rows:
            print(r)
except Exception as e:
    print('ERROR', e)
finally:
    conn.close()

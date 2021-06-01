import sqlite3

class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.con = sqlite3.connect(self.db_name)
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()

with DBManager('test.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE stocks
                   (date text, trans text, symbol text, qty real, price real)''')
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    con.commit()
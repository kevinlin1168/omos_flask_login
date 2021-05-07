import sqlite3

def createTable():
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS UserAccounts (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                UserName INTEGER UNIQUE,
                Password TEXT, 
                CreateDate TEXT, 
                ModifiedDate TEXT)''')
    con.commit()
    con.close()

def execSelect(exec):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    result = cur.execute(f'''{exec}''').fetchall()
    con.commit()
    con.close()
    return result

def exec(exec):
    con = sqlite3.connect('sqlite.db')
    cur = con.cursor()
    result = cur.execute(f'''{exec}''')
    con.commit()
    con.close()
    return result
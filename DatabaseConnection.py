import sqlite3 as sql

def connectDatabase():
    conn = sql.connect("Bankacc.db")
    cursor = conn.cursor()
    return (conn , cursor)

def createTable():
    conn , cursor = connectDatabase()
    cursor.execute("""CREATE TABLE IF NOT EXISTS CLIENTS(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               ad text,
               soyad text,
               hesapno integer, 
               bakiye integer
)""")
    conn.commit()
    conn.close()

def newUserInsert(name,surname,accNo,balance):
    conn , cursor  = connectDatabase()
    cursor.execute("""
    INSERT INTO CLIENTS (ad,soyad,hesapno,bakiye) VALUES (?, ?, ?,?)
""",(name,surname,accNo,balance))
    conn.commit()
    conn.close()

def fectDatas():
    conn , cursor = connectDatabase()
    clients= cursor.execute("SELECT * from CLIENTS")
    clientsDatas = clients.fetchall()
    conn.commit()
    conn.close()
    return clientsDatas

def updateBalance(newBalance,balance):
    conn , cursor = connectDatabase()
    cursor.execute("UPDATE CLIENTS SET bakiye = {} WHERE bakiye = {}".format(newBalance,balance))
    conn.commit()
    conn.close()

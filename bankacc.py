import sqlite3 as sql

conn = sql.connect("Bankacc.db")
cursor = conn.cursor()
opendb = cursor.execute("""CREATE TABLE IF NOT EXISTS CLIENTS(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               ad text,
               soyad text,
               hesapno integer, 
               bakiye integer
)""")

clients= conn.execute("SELECT * from CLIENTS")

balance =("""UPDATE CLIENTS SET bakiye = {} WHERE bakiye = {} """)
clients = clients.fetchall()
balance_execute = cursor.execute

def addAcc():
        opendb
        name = input("İsim : ")
        surname = input("Soyisim : ")
        AccNO=input("Hesap NO :")
        balance=int(input("Bakiyeniz : "))
        cursor.execute("""
    INSERT INTO CLIENTS (ad,soyad,hesapno,bakiye) VALUES (?, ?, ?,?)
""",(name,surname,AccNO,balance))
        conn.commit()
        conn.close()
def bankacc():
        opendb
        clients
        for row in clients:
            print(f"\n{row[0]}. Kişi ")
            print("İSİM : ", row[1])
            print("SOYİSİM : ", row[2])
            print("HESAP NO : ", row[3])
            print("HESAP BAKİYESİ : ", row[4],"\n")
            conn.commit()
            conn.close()

def bankAccYat():
    clients
    for row in clients:
        miktar = int(input(f"Sayın {row[1]} {row[2]}, Ne kadar Yatırmak istiyorsunuz : "))
        NewBalance = row[4] + miktar
        print(f"\nSayın {row[1]} {row[2]}, {row[3]} No' lu Hesabınıza {miktar} tutarında bakiyeniz Yatırılmıştır !\n\nYeni Bakiyeniz {NewBalance}\n")
        balance_execute(balance.format(NewBalance,row[4]))
        conn.commit()
        conn.close()

def bankAccCek():
    clients
    for row in clients:
        miktar = int(input(f"Sayın {row[1]} {row[2]} , Ne kadar çekmek istiyorsunuz : "))
        NewBalance = row[4] - miktar
        if row[4]>=miktar: 
            print(f"Sayın {row[1]} {row[2]}, {row[3]} No'lu Hesabınıza {miktar} tutarında para çekim işlemi gerçekleşmiştir!\n\nYeni bakiyeniz {NewBalance}\n")
            balance_execute(balance.format(NewBalance,row[4]))
        else:
            print(f"\nSayın {row[1]} {row[2]}, {row[3]} No' lu hesabınızda yeterli bakiye olmadığı için işleminiz gerçekleştirilemiyor !\n")
            conn.commit()
            conn.close()
             
while True:
    islem = input("\n1- Yeni Hesap ekle\n2- Hesap Görüntüle\n3- Para Yatırma\n4- Para Çekme\n5- Çıkış\n\nYapmak istediğiniz işlem : ")
    if islem == "1" : 
        addAcc()
        continue
    elif islem == "2" :
        bankacc()
        continue
    elif islem == "3":
        bankAccYat()
        continue
    elif islem == "4":
        bankAccCek()
        continue
    if islem =="5":
        break
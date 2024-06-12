from DatabaseConnection import * 

def addAcc():
        createTable()
        name = input("İsim : ")
        surname = input("Soyisim : ")
        accNo=input("Hesap NO :")
        balance=int(input("Bakiyeniz : "))
        newUserInsert(name,surname,accNo,balance)

def bankacc():
    try :
        for row in fectDatas():
                print(f"""
{row[0]}. Kişi
İSİM :  {row[1]}
SOYİSİM :  {row[2]}
HESAP NO :  {row[3]}
HESAP BAKİYESİ :  {row[4]}
""")
    except:
        print("Lütfen kullanıcı ekleyin!")
        addAcc()

def bankAccYat():
    name= input("İsim: ")
    surname = input("Soyisim: ")
    try:
        for row in fectDatas():
            if row[1].capitalize() == name.capitalize() and row[2].capitalize() == surname.capitalize():    
                miktar = int(input(f"Sayın {row[1]} {row[2]}, Ne kadar Yatırmak istiyorsunuz : "))
                NewBalance = row[4] + miktar
                print(f"\nSayın {row[1]} {row[2]}, {row[3]} No' lu Hesabınıza {miktar} tutarında bakiyeniz Yatırılmıştır !\n\nYeni Bakiyeniz {NewBalance}\n")
                updateBalance(NewBalance,row[4])
            else:
                print(f"{row[1]},{row[2]} isminde bir kullanıcı bulunamadı.")
                addAcc()

    except:
        print("\nLütfen kullanıcı ekleyin!")
        addAcc()

def bankAccCek():
    try:
        for row in fectDatas():
            miktar = int(input(f"Sayın {row[1]} {row[2]} , Ne kadar çekmek istiyorsunuz : "))
            NewBalance = row[4] - miktar
            if row[4]>=miktar: 
                print(f"Sayın {row[1]} {row[2]}, {row[3]} No'lu Hesabınıza {miktar} tutarında para çekim işlemi gerçekleşmiştir!\n\nYeni bakiyeniz {NewBalance}\n")
                updateBalance(NewBalance,row[4])
            else:
                print(f"\nSayın {row[1]} {row[2]}, {row[3]} No' lu hesabınızda yeterli bakiye olmadığı için işleminiz gerçekleştirilemiyor !\n")
    except:
        print("Lütfen kullanıcı ekleyin!")
        addAcc()
        
# def main():   
while True:
        islem = input("""
    1- Yeni Hesap ekle
    2- Hesap Görüntüle
    3- Para Yatırma
    4- Para Çekme
    5- Çıkış
    Yapmak istediğiniz işlem : """)
        
        if islem == "1" : 
            addAcc()
        elif islem == "2" :
            bankacc()
        elif islem == "3":
            bankAccYat()
        elif islem == "4":
            bankAccCek()
        elif islem =="5":
            break

# if __name__ == main():
#     main()
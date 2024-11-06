from db import database

db = database()
botCevabi = input("botCevabi: ")
kullaniciCevap1 = input("kullaniciCevap1:  ")
kullaniciCevap2 = input("kullaniciCevap2 : ") 
kullaniciCevap3 = input("kullaniciCevap3 : ") 

if db.insert_new(botCevabi, kullaniciCevap1, kullaniciCevap2, kullaniciCevap3):
    print("recorded")
else:
    print("record failed!")
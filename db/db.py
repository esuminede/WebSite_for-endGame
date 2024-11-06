import sqlite3 
import os

class database():
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__)) #dizini buldu
        self.db_path = os.path.join(self.path, 'kullaniciGirdileri') #dizin ile veritabanı ismini birleştirdi.

    def open_connetction(self):
        try:
            self.con = sqlite3.connect(self.db_path)
            self.cursor = self.con.cursor()
        except:
            print("db connection error")

    def all_search(self):
        self.open_connetction()
        self.cursor.execute("select * from kullaniciGirdileri")
        info = self.cursor.fetchall()
        self.close_connection()
        return info
    
    def bot_answer(self, no):
        self.open_connetction()
        self.cursor.execute("select * from kullaniciGirdileri where no = ?", (no))
        info = self.cursor.fetchall()
        self.close_connection()
        return info
    
    def detailed_search(self, botCevabi, kullaniciCevap1, text):
        text = "'" + text + "'"
        self.open_connetction()
        sql = "select {} from kullaniciGirdileri where {} = {}".format(botCevabi, kullaniciCevap1, text)
        self.cursor.execute(sql)
        info = self.cursor.fetchall()
        self.close_connection()
        return info

    def insert_new(self, botCevabi, kullnaiciCevap1, kullaniciCevap2, kullaniciCevap3):
        try:
            self.open_connetction()
            sql = "insert into kullaniciGirdileri(botCevabi, kullnaiciCevap1, kullaniciCevap2, kullaniciCevap3) values(?, ?, ?)", (botCevabi, kullnaiciCevap1, kullaniciCevap2, kullaniciCevap3)
            self.cursor.execute(sql)
            self.con.commit()
            self.close_connection()
            return 1
        except: 
            return 0
    def close_connection(self):
        self.con.close()
    
    



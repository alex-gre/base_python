
import sqlite3
import datetime
class Ininterface:

    def __init__(self) -> None:
        pass
 #------------------- Ininterface for phone_book table -------------------------       
    def inpname(self):
        self.name = str(input('Name: '))
        return self.name

    def inpphone(self):
        self.n_phone = str(input('Phone: '))
        return self.n_phone

    def inpinfo(self):
        self.info = str(input('Info: '))
        return self.info

#--------------------- for work_org table --------------------
            
    def indatestamp(self):
        self.ddate = str(datetime.date.today())
        return self.ddate

    def inwname(self):
        self.wname = str(input('Введите имя работы: '))
        return self.wname
    
    def  inwinfo(self):
        self.winfo = str(input('Введите доп. информацию: '))
        return self.winfo

class Database:
           
    """Constructor Database"""
    def __init__(self, db_name) -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
 
    """Method create table"""
    def create_table_phbook(self)-> None:
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS phone_book(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                       name VARCHAR(35) NOT NULL, n_phone VARCHAR(14) NOT NULL, info VARCHAR(125))""")
        self.conn.commit() 

    """ Method insert book """                      
    def insert_phbook(self,name,n_phone,info) -> None:
       
       self.cursor.execute("INSERT INTO phone_book (name,n_phone,info) VALUES (?,?,?)",(name,n_phone,info))
       self.conn.commit()

    """ Method clear book """                      
    def clear_phbook(self) -> None:
       self.cursor.execute("DELETE FROM phone_book")
       self.conn.commit()   

    """ Method get book """
    def get_phbook(self) :
        self.cursor.execute("SELECT * FROM phone_book")
        return self.cursor.fetchall()

 #-------------------------- Create Table work_org  --------------------
    """Method create table work_org"""
    def create_table_worg(self)-> None:
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS work_org(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                       ddate text, wname VARCHAR(35) NOT NULL,winfo text)""")
        self.conn.commit()  

 #---------------------------- Insert data work_org----------------
    """ Method insert work_org """                      
    def insert_worg(self,ddate,wname,winfo) -> None:
       
       self.cursor.execute("INSERT INTO work_org (ddate,wname,winfo) VALUES (?,?,?)",(ddate,wname,winfo))
       self.conn.commit()             

    """ Method dump database """                      
    def dump_database(self) -> None:
       with open('dump.sql', 'w') as f:
         for line in self.conn.iterdump():
             f.write('%s\n' % line)
       self.conn.commit()   
    

    """ Method  close connection """
    def close_connection(self):
        self.conn.close()
   
    

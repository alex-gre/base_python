
from moduldb import Ininterface
from moduldb import Database


if __name__=="__main__":
    
    db = Database('organizer.db')
    #db = Database('plants.db')
    inp = Ininterface()
    
    
    def menu():
      print("""
        0 - create new database (Init) or rewrite
        1 - Input contacts organizer.db
        2 - View select contacts 
        3 - Input data work_org
        4 - Delete all contacts  

        8 - Backup database output dump.sql 
       """)

       
menu()
 
    #DEBUG
             
    #db.clear_phbook()

try:
   #  i = int(input('select menu: '))
   #  if (i==0):
   # db.create_table_phbook()
   # db.create_table_worg()

    i = int(input('select menu: '))
    if (i==0):
       db.create_table_worg()

    elif (i==1):
       db.insert_phbook(inp.inpname(),inp.inpphone(),inp.inpinfo())

    elif (i==2):
       db.get_phbook()
       record = db.get_phbook()
       print(record)

    elif (i==3):
       #pass
       db.create_table_worg(inp.indatestamp(),inp.inwname(),inp.inwinfo())

    elif (i==4):
       db.clear_phbook()

    elif (i==8):
       db.dump_database()   
    #DEBUG
    
    #db.insert_phbook(inp.inpname(),inp.inpphone(),inp.inpinfo())
    #db.dump_phbook()
    #db.insert_phbook('Alice','24254215','test record data alice')
    
    db.close_connection()

except Exception as e:
    print('Ошибка ввода ')
    print(e)

      
try:
    # file = open ('test.txt', encoding="utf-8") 
    # s = file.readlines()
    # print(s)
    # #int(s) # искуственно создаем ошибку
    # file.close()

    with open ('test.txt', encoding="utf-8") as file:
        s = file.readlines()
        print(s)
 
except FileNotFoundError:
    print('FileNotFoundError')   
except:
    print('Ошибка при работе с файлом')    

finally:
    print(file.closed)     
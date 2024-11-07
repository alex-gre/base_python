from mcalculate import MatPPR

if __name__ == "__main__":

    mcalc = MatPPR()
    mcalc.topmenuppr()
    
    try:
        n = input('выбор меню :')
        if n == 'n':
            mcalc.inpmenuppr()
            mcalc.outpppr()
        
        else :
            print("Error")    
    
    except Exception as e:
        print('Ошибка ввода!')
        print(e)


       

class MyClass:
    
    # SPECIAL METHODS 
    def __init__(self, m) -> None:
        self.mes = m

    def __call__(self) :
        print(self.mes)


c1 = MyClass("Test 1")
c2 = MyClass("Test 2") 
c1()
c2()       

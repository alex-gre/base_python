class Cat:
    name = None
    age = None
    isHappy = None

 # конструктор который имеет два метода set_data и get_data  
 # и прописаны значения по умолчанию None для того, чтобы можно
 # передовать в конструктор разное количество параметров

    def __init__(self, name = None, age = None, isHappy = None):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):    
        print(self.name, " age: ", self.age, " . Happy: ", self.isHappy)



#bad code
#cat1 = Cat()
#cat1.name = "Barsik"
#cat1.age = 3
#print("Cat1 name "+cat1.name+" age = "+str(cat1.age))

#best code
cat1 = Cat("Barsik ",3,True)
#один параметр в cat2
cat2 = Cat("Tom ")

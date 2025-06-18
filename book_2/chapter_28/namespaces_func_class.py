x = 1 # глобальная переменная

def nester():
    print(x) # по LEGB в глобальную

    class First():
        print(x) # по LEGB в глобальную
        def method1(self):
            print(x)  # по LEGB в глобальную
        def method2(self):
            x=3 # присваивание = локальное имя
            print(x) # по LEGB в ЛОКАЛЬНУЮ

    inst = First()
    inst.method1()
    inst.method2()

print(x)
nester()
print('-'*40)

def nester1():
    y = 2
    print(y)

    class Second():
        y = 3
        print(y)
    
        def method1(self):
            print(y) #!!!!!!!!!!!!! y = 2 НЕ ИЗ КЛАССА!!!
            print(self.y) #!!! y = 3 из класса!!! 


class FirstClass():
    def __init__(self, number):
        self.number = number


class SomeClass(FirstClass):
    print('hello from class')
    some =123

    def __init__(self, name, number):
        # FirstClass.__init__(self, number) # Явное указание переопределения
        super().__init__(number) # Автоматическое указание
        self.name = name
        
    

dd = SomeClass('sfsf', 22)

class CheckInit(SomeClass):
    def __init__(self, name, spam, number):
        super().__init__(name, number)
        self.spam = "spam from CheckInit"      
        
        


aa = CheckInit('ggg', 'eeee', 444)
print(aa.number)
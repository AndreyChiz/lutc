'''Миксины'''


'''вывод списка атрибутов при помощиметода из миксина'''

class ListInstance:
    def __attrnames(self):
        result =''

        for attr in sorted(self.__dict__):
            result += '\t{}={}\n'.format(attr, self.__dict__[attr])
        return result
    
    def __str__(self):
        return '<instaance of {}, addres {}: \n{}>'.format(
            self.__class__.__name__, # имя экземпляра класса
            id(self), # адрес в памяти
            self.__attrnames() 
        )

class Spam(ListInstance):
    def __init__(self):
        self.data = 'food'

x = Spam()

print(x)
print(str(x))

'''Миксин и множественное наследование'''

class Super:
    def __init__(self):
        self.data1 = 'spam'
    def ham(self):
        pass

class Sub(Super, ListInstance):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42

    def spam(self):
        pass

if __name__ == '__main__':

    x = Sub()
    print(x)

    

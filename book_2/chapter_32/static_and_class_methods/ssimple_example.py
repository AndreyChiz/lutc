'''Статические методы и методы класса'''


class Spam:
    '''класс со счётчиком созданных экземпляров'''
    num_instances = 0 #Атрибут класса
    def __init__(self):
        '''При создании экземпляра счётчик увеличивается'''
        Spam.num_instances += 1

    def pritn_num_instances():
        '''статический метод без специального аргуента'''
        print(f'Count of created instaces {Spam.num_instances}')


a = Spam()
b = Spam()
c = Spam()

Spam.pritn_num_instances() # вызов черз класс (нет self, ничего не ожидает и не подучает, по жтому работает)
# a.pritn_num_instances() 
# # !!! экземпляр автоматически передается методу, 
# который не имеет аргумента для его получения !! ошибка

print(a.num_instances)

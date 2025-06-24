"""
если метод__ call__ определен, то Python выполняет его для выражений вызова функций,
применяемых к вашему экземпляру, с передачей ему любых позиционных или ключе­
вых аргументов, которые были отправлены.

Применение:
    - позволяет реализо­вывать объекты, которые соответствуют ожидаемому интерфейсу вызова функций, но
также предохраняют информацию о состоянии и другие активы классов, такие как
наследование.
    * ==> например длля применения объекта в колбеках (при этом состояние внутри объекта будет сохраняться)
"""


from tkinter import Button


class Callee:
    def __call__(self, *pargs, **kargs):
        print("Called:", pargs, kargs)


c = Callee()
c(1, 2, 3)


"""
Сохранение состояния
    - возможно испоьзовать в качесве замены замыканиям
"""


class Callback:
    def __init__(self, color):
        self.color = color # хранимое состояние

    def __call__(self): # передается в колбек
        print("trun", self.color)

    def change_color(self):
        print("trun", self.color) #вариант со связанным методом

cb1 = Callback('blue') # функция - запомненое состояние
cb2 = Callback('green')  # функция - запомненое состояние


button = Button(command = cb1)
button1 = Button(command = cb2)
button_n = Button(command = cb1.change_color) # Использование связанного метода
      

'''Альтернатива на замыкании'''
def callback (color) :
    def oncall () :
        print('turn', color)
    return oncall # Объемлющая область видимости или атрибуты

cb3 = callback('yellow' )
cb3() #При возникновении события выводит turn yellow
button1 = Button(command=cb3)
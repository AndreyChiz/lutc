class Zero: ...
class Neo:...

class First():
    def hello(self):
        self.data = "spam"


class Second(First):
    def hola(self):
        self.data2 = "eggs"


x = Second()
# print(x.__dict__)  # словарь пространства имен экземпляра
# # тут он щёщ пустой
# print(x.__class__)  # ссылка на класс экземпляра

# print(Second.__bases__)  # ссылка только на родительские классы 1 уровня
# # Zero не отображатеся !
# print(First.__bases__)# тут видно два класса
# print(Zero.__bases__) # тут неявно указан object


print(x.__dict__)
y =Second()

x.hello()
print(x.__dict__)

x.hola()
print(x.__dict__)
print(list (Second.__dict__))
print(list(First.__dict__))
print(list(i for i in First.__dict__ if not i.startswith("__")))


print(y.__dict__)


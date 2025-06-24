"""
__ setattr__ - перехватывает все присваивания зна­чений атрибутам

Применение:
    - проверка перед присваиванием

Проблемы:
    - при­сваивание значения любому атрибуту в self внутри__ setattr__ снова вызывает
    __ setattr__ , что потенциально может стать причиной бесконечного цикла рекурсии
        ==> можно избежаь присваивая значения ключам словаря __dict__
"""


class AccessControl:
    def __setattr__(self, attr, value):
        if attr == "age":
            self.__dict__[attr] = value + 10
            # object.__setattr__(self, attr, value + 10)# второй правильный  вариант
        else:
            raise AttributeError(attr + " not allowed")


x = AccessControl()
x.age = 40
print(x.age)  # type: ignore
x.name = "bob"

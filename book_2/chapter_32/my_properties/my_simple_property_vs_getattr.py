from typing import Any


class SetGetAttrs:
    """Реализация чтения и установки значений атрибутов через __getattr__, __setattr__"""

    def __getattr__(self, name):  # При ссылке на неопределенный атрибут
        if name == "age":
            return 40
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):  # При всех операциях присваивания
        if name == " age":
            self.__dict__["_age"] = (
                value  # Или object.__ setattr__ () чтобы избезжать зацикливания
            )
        else:
            self.__dict__[name] = value


x = SetGetAttrs()

# print(x.age)


class SetGetProperty:
    """Реализация чтения и установки значений атрибутов через property"""

    def getage(self):
        print(f"выполнилось {self.getage.__name__}")
        return 40

    def setage(self, value):
        print(f"выполнилось {self.setage.__name__}")
        self._age = value

    age = property(
        getage,
        setage,
        None,
        None,
    )

  

x = SetGetProperty()

print(x.age)  # запускается getage
print(x.__dict__)  # атрибута нет в дикте {}
x.age = 41  # запускается setage устанавливает атрибут _age = 41
print(f"теперь {x.__dict__=}")  # {появился _age=41}
print(x.age)  # запускается getage там по прежнему 40
print(x._age)  # прямое обращение к _age

"""База по properties"""


class SomeGetattr:
    """Реализация получения значения виртуального атрибута через __getattr__"""

    def getage(self):
        return 39

    def __getattr__( # <-- тут нет дополнительного вызова
        self, attrname
    ):  # позволяет классам перехватывать ссылки на неопределенные атрибуты
        if attrname == "age":
            # return 40 # <-- или хардкодим
            return self.getage() # <-- или генерируем
        else:
            raise AttributeError(attrname)


x = SomeGetattr()
print(
    f"Вызов x.age через __getattr__ >>> {x.age=}"
)  # не сущесвующий атрибут но доступный в  __getattr__ (__getattr__ выполняется)
# print(
#     x.name
# )  # не существующий атрибут и  не доступный в __getattr__ (__getattr__ выполняется)


class SomeProperties:
    """Реализация получения значения виртуального атрибута через property"""

    def getage(self):
        return 39

    age = property( # <-- тут дополнительный вызов
        getage,  # метод вызываемый для получения значения
        None,  # метод вызываемый для установки значения
        None,  # метод вызываемый дляудаления значения
        None,  # строка документации
    )


x = SomeProperties()

print(
    f"Вызов x.age через property >>> {x.age=}"
)  # значение из метода getage() через атрибут с property 
# print(x.name)

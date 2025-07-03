from collections.abc import Iterable


class C:
    __slots__ = [
        "a",
        "b",
    ]

    def __getattr__(self, attrname):
        if attrname == "foo":  # см. строка 31
            return 77

    def __dir__(self) -> Iterable[str]:
        """ручное добаление динамичексих атрибутов в dir()"""
        tmp = super().__dir__()
        tmp.append("foo")
        return tmp


x = C()
x.a = 1
print(x.a)
print(x.__dict__)  # у экземпляра класса
# нет __dict__ так как определен __slots__
# поэтому нельзя присваивать новые атрибуты ЭКЗЕМПЛЯРУ

# Но можно через __getattr__()

print(getattr(x, "a"))

# и устанавливать через setattr

setattr(x, "b", 2)
print(x.b)
# setattr(x, 'f', 3) NO!! нет в слотах
# x.f =4 NO!! нет в слотах присваивание невозможно

# и можно настроить динамические атирибуты
print(x.foo)

print(x.__dict__)
print(dir(x))  # Успешно находит слотовые атрибуты


"""Я вное включение __dict__  вклассе где указаны __slots__"""


class DictSlots:
    __slots__ = [
        "q",
        "w",
        "__dict__",
    ]
    e = 3

    def __init__(self):
        self.r = "instance_attr"


print(DictSlots.__slots__)
# print(DictSlots.__dict__)


# x = DictSlots()
# print(x.__dict__) # Теперь есть __dict__ т.к. разрешен в слотах

# x.some = "new_attr" # И можно присвоить новый атрибут ЭКЗЕМПЛЯРУ
# print(x.__dict__) # обработается стандартным образом и попадет в __dict__

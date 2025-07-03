"""Я вное включение __dict__  вклассе где указаны __slots__"""


class DictSlots:
    __slots__ = [
        "q",
        "w",
        "__dict__",  # BAD!!! теперь можно добавлять атрибуты как обычно
    ]
    e = 3

    def __init__(self):
        self.r = "instance_attr"


# print((zz if "__slots__" in (zz := dir(DictSlots)) else "Нет __slots__"), end="\n\n")

print(DictSlots.__slots__, end="\n\n")
print(DictSlots.__dict__, end="\n\n")

x = DictSlots()
print(x.__dict__)  # Теперь есть __dict__ т.к. разрешен в слотах

x.some = "new_attr"  # теперь можно присвоить новый атрибут ЭКЗЕМПЛЯРУ
print(x.__dict__)  # обработается стандартным образом и попадет в __dict__

"""Делегирование"""


class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attrname):
        """класс Wrapped использует(делегирует) вызовы всех методов во встроенный объект object
        при этом добавляет свою логику"""
        print("Trace: " + attrname)
        return getattr(self.wrapped, attrname)


x = Wrapper([1, 2, 3])
x.append(5)
# >>> Trace: append

x = Wrapper({1: "a", 2: "b"})
list(x.keys())
# >>> Trace: keys

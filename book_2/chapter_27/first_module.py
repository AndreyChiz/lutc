class SuperMAinClass:...

class FirstClass():
    some_attr = "что то"

    def display(self):
        print("something_printed")


class SomeClass(SuperMAinClass): 
    def display(self):
        print('displayfrom someclass')

class SecondClass(
    SomeClass,
    FirstClass,
):
    def __init__(self, some_attr):
        self.some_attr = some_attr

    def __add__(self, other):
        return SecondClass(self.some_attr * other)

    def __str__(self):
        return self.some_attr


x = SecondClass("строка")

x += 9


print(*SecondClass.__dict__.items(), sep="\n")
print()
print(*dir(SecondClass), sep="\n")
print()
print(SecondClass.__bases__)
print()
print(SecondClass.__mro__)
print()
print(x.__class__)
print(type(x))
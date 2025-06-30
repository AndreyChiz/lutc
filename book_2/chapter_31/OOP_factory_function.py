"""Фабрика(фабричная функция)

- функция принимающая класс и параметры и генерирующая на основании этого экземпляры

"""


def factory(SomeClass, *args, **kwargs):
    """функция фабрика генерирующая объекты"""
    return SomeClass(*args, **kwargs)


class First:
    def doo_it(self, message):
        print(message)


class Second:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job


instance_one = factory(First)
instance_two = factory(Second, "Artour", "king")
instance_three = factory(Second, name="Jane")

for instance in [
    instance_one,
    instance_three,
    instance_two,
]:
    print(instance.__dict__)

"""
>>> 
{}
{'name': 'Jane', 'job': None}
{'name': 'Artour', 'job': 'king'}
"""
instance_one.doo_it("hi")
print(instance_two.name, instance_two.job)


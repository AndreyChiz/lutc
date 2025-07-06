"""Для подсчёта экземпляров по классам,
лучше задействовать методы класса"""


class OwnInstaneCounter:
    num_instances = 0

    @classmethod
    def count(cls):
        cls.num_instances += 1

    def __init__(self) -> None:
        self.count()


class OwnInstanceCounterChild(OwnInstaneCounter):
    num_instances = 0

    def __init__(self) -> None:
        OwnInstaneCounter.__init__(self)


class EnotherOwnInstanceCounterChild(OwnInstaneCounter):
    num_instances = 0


x = OwnInstaneCounter()
y1, y2 = OwnInstanceCounterChild(), OwnInstanceCounterChild()
z1, z2, z3 = (
    EnotherOwnInstanceCounterChild(),
    EnotherOwnInstanceCounterChild(),
    EnotherOwnInstanceCounterChild(),
)

print(f"""Обращаются каждый к счётчику в своём классе через экземпляр:
{x.num_instances=}
{y1.num_instances=}
{z1.num_instances=}
""")

print(f"""Счётчики каждого класса - обращение напрямую:
{OwnInstaneCounter.num_instances=}
{OwnInstanceCounterChild.num_instances=}
{EnotherOwnInstanceCounterChild.num_instances=}
""")

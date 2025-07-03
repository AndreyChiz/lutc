"""когда нужно поддерживать слоты из роительских классов"""


class SlotsDictNorm:
    __slots__ = ["a", "b", "__dict__"]

    def __init__(self, data):   
        self.c = data


print(SlotsDictNorm.__dict__)

x = SlotsDictNorm(3)

x.a = 1
x.b = 2
x.c = 3

print(f"если в слотах явно казан __dict__ --> {x.__slots__=}")
print(f"поддерживаются и слоты и дикт \n{x.a=}\n{x.b=}\n{x.c=}")


print(
    *[
        str(f"{name}={getattr(x, name)}")
        for name in dir(x)
        if not name.startswith("__")
    ],
    sep="\n",
)

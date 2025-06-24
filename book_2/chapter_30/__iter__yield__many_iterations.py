class Square:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value**2


if __name__ == "__main__":
    print("++++ МНОЖЕСТВЕННАЯ ИТЕРАЦИЯ С ГЕНЕРАТОРОМ++++")

    x = Square(1, 5)

    iter_x = iter(x)  # iter_x и iter1_x ссылки на один объект
    iter1_x = iter(x)

    print(iter_x is iter1_x, "разные объекты")

    # print([i for i in x], "(Исчерпали объект)", sep=" => ")
    # print([i for i in x], "(тут онпустой)", sep=" => ")

    print(next(iter_x))  # 1 общее исчисление
    print(next(iter1_x))  # 4 общее исчисление
    print(next(iter_x))  # 9
    print(next(iter_x))  # 16

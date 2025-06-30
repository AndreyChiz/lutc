"""Ручная реализация абстрактного класса"""


class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(
                data
            )  # суда подставляется метод который нужно определить в наследнике
            # если не переопределить то используется метод родителя(текущего класса)
            # а он вызовет исключение
            self.writer.write(data)

    def converter(self, data):
        assert False, "converter must be defined"


class Uppercase(Processor):
    def converter(self, data):  # требуется в родителском классе
        """convert to uppercase"""
        return data.upper()


class HTMLize:
    def write(self, line):
        print("<h1>{}<h1>".format(line))


if __name__ == "__main__":
    import sys

    "пример 1"
    # создать Uppercase передать объекты с указанным интерфейсом
    # добавление логики через наследование и композицию
    obj = Uppercase(  # наследование
        reader=open("./book_2/chapter_31/somespam.txt"),  # композиция
        writer=sys.stdout,  # композиция
    )
    obj.process()

    "пример 2"
    obj2 = Uppercase(
        reader=open("./book_2/chapter_31/somespam.txt"),
        writer=HTMLize(),  # определили необходимый интерфейс (метод write)
    )

    obj2.process()

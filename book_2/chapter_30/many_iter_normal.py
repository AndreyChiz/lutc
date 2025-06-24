class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped # данные

    def __iter__(self):
        return SkipIterator(self.wrapped)


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped # эти же данные переданные из супперкласса
        self.offset = 0 # состояние в каждом итераторе своё

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
        return item


if __name__ == "__main__":
    # alpha = "adcdef"
    # skipper = SkipObject(alpha)
    # I = iter(skipper)
    # print(next(I), next(I), next(I))

    # for x in skipper:
    #     for y in skipper:
    #         print(x + y, end=" ")
    print("++++ МНОЖЕСТВЕННАЯ ИТЕРАЦИЯ ++++")
    x = SkipObject([1,2,3,4,5])

    iter_x = iter(x) # разные объекты iter_x и iter1_x
    iter1_x = iter(x) 
    print(iter_x is iter1_x, "разны еобъекты ")

    print([i for i in x], "(Исчерпали объект)", sep=" => ")
    print([i for i in x], "(тут он сначала)", sep=" => ")
    
    
    print(next(iter_x)) #1 отдельное исчисление
    print(next(iter1_x))#1 отдельное исчисление
    print(next(iter_x))#3
    print(next(iter_x))#5


    print('++++ЕДИНСТВЕННАЯ ИТЕРАЦИЯ++++')
    from s__iter__next__ import Squares

    x = Squares(1, 5)

    iter_x = iter(x) # iter_x и iter1_x ссылки на один объект
    iter1_x = iter(x) 
    print(iter_x is iter1_x, 'один и тот же объект')
    # print([i for i in x], "(Исчерпали объект)", sep=" => ")
    # print([i for i in x], "(тут онпустой)", sep=" => ")

    print(next(iter_x)) #1 общее исчисление
    print(next(iter1_x)) #4 общее исчисление 
    print(next(iter_x)) #9
    print(next(iter_x)) #16

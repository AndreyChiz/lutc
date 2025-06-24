# Работает только индексирование ==========================================================================
# class Indexer:
#     def __getitem__(self, index): # т.к в index корректно обрабатывается только int
#         return index**2 # нарезание не будет работать

# x = Indexer()
# print(x[2])
# print(x[::-1]) # Не сработает потому что index ожидается целое чило
# чтобы работало нарезание нежно чтобы логика могда обрабатывать объект среза
# return <что_то>[1:3] равносильно <что_то>[slice(1,3)]


# Обеспечение работы срезов ==========================================================================
class First:
    def __init__(self, numb) -> None:
        self.data = list(range(numb))

    def __getitem__(self, next):
        return self.data[
            next
        ]  # Срезы будут работать т.к. data[next] способно обработать data[slice()]


y = First(10)

print(y[1])
# print(y[::-1])
# print(y[slice(None, None, -1)])

# Выгрузка в __getitem__ значений переданных в срез


class SliceNumbsGetter:
    def __getitem__(self, index):
        if isinstance(index, int):
            print("indexing", index)
        else:
            print("slicing___", index.start, index.stop, index.step)


x = SliceNumbsGetter()
x[99]
x[slice(1, 3, 2)]

class IndexSetter:
    data = [100]
    dict_data = {}
    def __setitem__(self, index, value):
        # self.data[index] = value
        self.dict_data[index] = value

ddd = IndexSetter()
# ddd[1:5] = [1,2,3,4,5,6,7]
ddd['key'] = 'value'

print(ddd.data)
print(ddd.dict_data)
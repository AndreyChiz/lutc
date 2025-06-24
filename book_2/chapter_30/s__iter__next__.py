class Squares:
    def __init__(self, start, stop):  # сохранение состояния
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value**2


for i in Squares(1, 5):
    print(i, end=" ")

x = Squares(1, 5)
I = iter(x)

print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
# print(next(I)) #Stop Iteration

# для использования смещения можно сохранить в список
# так как list() итерационный контекст это будет автоматом

x = Squares(1,5)
#x[1] не сработает 
print(list(x)[1], 'элемент списка') 

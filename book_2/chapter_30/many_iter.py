from s__iter__next__ import Squares


print("++++ОДИНОЧНАЯ ИТЕРАЦИЯ++++")

x = Squares(1, 5)
print([i for i in x], "(Исчерпали объект)", sep=" => ")
print([i for i in x], "(тут он пуст)", sep=" => ")

y = Squares(1, 6)
gen_y = (i for i in y)
print(next(gen_y))
print(next(gen_y))
print(next(gen_y))
print("продожение итратора в другом итерационном контексте =>", end=" ")
for i in gen_y:
    print(i, end=" ")
print()
print("итератор gen_y исчерпан",'\n')

"""
Скажем, поскольку текущий метод__ iter__ класса Squares всегда возвращает
self с только одной копией состояния итерации, он обеспечивает одноразовую ите­
рацию; после итерации экземпляр данного класса становится пустым. Повторный
вызов__ iter__ на том же самом экземпляре снова возвращает self независимо от
состояния, в котором он был оставлен. Как правило, для каждой новой итерации пот­
ребуется создавать новый итерируемый объект:"""


print("++++МНОЖЕСТВЕННАЯ ИТЕРАЦИЯ++++")
print('Проблема - создаётся новый список')
print([i for i in Squares(1, 5)])
print([i for i in Squares(1, 5)])

print(100 in Squares(1, 5))
print(1 in Squares(1, 5))

print()
print('Проблема - исчерпывание итератора')
new_x = Squares(1, 5)
duble_x = (tuple(new_x), tuple(new_x))
print(duble_x, "во втором кортеже исерпан", '\n')

print('Проблема - создаётся дополнительный список')
new_list_x = list(Squares(1, 5))
duble_list_x = (tuple(new_list_x), tuple(new_list_x))
print(duble_list_x, "множественная итерация, но создали доп. список")

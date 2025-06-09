lst = [1, 2, 3]
print(lst, id(lst))
lst[:0] = [88]
print(lst, id(lst))
lst = [99] + lst
print(lst, id(lst))
lst.insert(0, 77)
print(lst, id(lst))
lst

lll = [1, "o", 4]


tt = (lst, lll)
print(tt)

dct = {tt: "some"}
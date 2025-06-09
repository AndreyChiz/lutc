# with open('some_file.txt', mode='a+') as file:
#     for line in file:
#         print(line)

# for line in open("some_file.txt"):
#     print(line, end="")

import ast

x = "[1,2,3]1\n"

# Преобразование в список
data = ast.literal_eval(x)

print(data)  # [1, 2, 3]
print(type(data))  # <class 'list'>
lst = [1, 2, 3, 4, 5, 7]
n = len(lst)

for i in range(n // 2):
    lst[i], lst[n - 1 - i] = lst[n - 1 - i], lst[i]

print(lst)  # [5, 4, 3, 2, 1]

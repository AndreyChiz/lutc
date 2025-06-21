 python -m timeit -n 1000 -r 5 -s "L = list(range(100))" "x = L.__len__()"

 python -m timeit -n 1000 -r 5 -s "L = list(range(100))" "x = len(L)"
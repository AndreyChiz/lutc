import some_module_104

names = dir(some_module_104)
for item in range(len(names)):
    print(names[item]) if not names[item].startswith("__") else None


print("")
x = (print(i) for i in dir(str) if not i.startswith("__"))
for i in x:
    ...

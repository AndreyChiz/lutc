import mod2

from mod1 import y, x

print(id(y))
print(id(x))

print(id(mod2.mod1.x))
print(id(mod2.mod1.y))
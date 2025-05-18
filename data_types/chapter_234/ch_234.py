import sys

x = "hello world"
z = b"hello world"
f = list(x)
n = tuple(f)
print(n)

x =  x.replace('l', 'L' , 2)
print(x)
c = bytearray(x, "utf-8")
d = bytearray(x, "ascii")
print(sys.getsizeof(x))
print(sys.getsizeof(z))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(f))
print(sys.getsizeof(n))

# Строка с символами Unicode
text = "😊"

# Преобразование в bytearray через кодирование
byte_array = bytearray(text.encode("utf-8"))
print(byte_array)  #

r = range(10, 20)
print(r[0])  # Выведет 10
print(r[5])  # Выведет 15
print(r[-1])  # Выведет 19
# сортированный словарь

my_dict = {
    "apple": "красный фрукт",
    "car": "транспортное средство",
    "python": "язык программирования",
    "book": "источник знаний",
    "coffee": "бодрящий напиток",
}

for index, key in enumerate(sorted(my_dict)):
    print(f"Индеккс {index}, ключ {key}, значение {my_dict.get(key)}")

# 1. Создать массив где составные числа будут true а  простые false
# 2. Так как мы знаем что 0 и 1 не простые числа, то в массиве будет false
# на этих позичиях.
# 3. Начнем обход с элемента 2 до элемента n+1 так как массив начинается с 0
# 4. false - составное, true простое


def create_wrap_list(num):
    w_list = [True] * (num + 1)
    w_list[:1] = [False, False]
    return w_list


def get_simple_digits(w_list):
    for i in range(2, len(w_list) ):
        # если w_list[2] true то 
        # записываем элемент 2*2, false если он не больше len(wlist)
        # записываем элемент 2*2*2 false
        ... 

w_list = create_wrap_list(10)
get_simple_digits(w_list=w_list)

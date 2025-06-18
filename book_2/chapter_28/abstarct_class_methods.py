from abc import ABCMeta, abstractmethod


class First(metaclass=ABCMeta):
    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        print("some")


class Second(First): ... #Тут абстрактный метод не переопределен


# x = First()  # Нельзя создать экземпляр даже если метод определен
# y = Second()  # Нельзя создать экземпляр пока не переопределеы абстрактные методы

class Second(First):
    def action(self):
        print('метод переопределен, можно создать экземпляр')

y = Second()
y.delegate()


# # По аналогии, ручной вариант
# class First():
#     def delegate(self):
#         self.action()

# class Second(First):
#     def action(self):
#         print('реализация')
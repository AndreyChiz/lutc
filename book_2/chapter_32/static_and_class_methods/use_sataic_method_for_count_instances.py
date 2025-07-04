"""Поведение статических методов при наследовании"""


class InstanceCounter:
    """класс считающий количество созданных экземпляров
    при помощи статического метода"""

    instance_count = 0

    def __init__(self):
        InstanceCounter.instance_count += 1

    @staticmethod
    def print_instance_count():
        print(f"Count of instances is {InstanceCounter.instance_count}")

    # Аналогия с декоратором --> но линтеры ругаются
    # print_instance_count = staticmethod(print_instance_count)


a = InstanceCounter()
b = InstanceCounter()
c = InstanceCounter()

# Один и тот же результат
InstanceCounter.print_instance_count()
a.print_instance_count()

#####################################################################


class InstanceCounerChild(InstanceCounter):
    """наследование и переопределение статического метода"""

    @staticmethod
    def print_instance_count():
        print(f"""переопределенный статический метод""")
        InstanceCounter.print_instance_count()


a = InstanceCounerChild()
b = InstanceCounerChild()

a.print_instance_count()
InstanceCounerChild.print_instance_count()

#####################################################################


class NotRedirectStaticMethod(InstanceCounter):
    """наследование статического метода без переопределения"""


c = NotRedirectStaticMethod()
c.print_instance_count()
NotRedirectStaticMethod.print_instance_count()

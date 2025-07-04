"""Поведение методов класса при наследованиии"""


class InstanceCounter:
    count_instances = 0

    def __init__(self):
        InstanceCounter.count_instances += 1

    @classmethod
    def print_count_instances(cls):
        print(f"Count of instances {cls.count_instances}")


# a = InstanceCounter()
# b = InstanceCounter()
# c = InstanceCounter()

# a.print_count_instances()
# InstanceCounter.print_count_instances()


#######################################################


class InstanceCounerChild(InstanceCounter):
    """наследование и переопределение статического метода"""

    @classmethod
    def print_count_instances(cls):
        print(f"""переопределенный статический метод {cls}""")
        InstanceCounter.print_count_instances()
        


a = InstanceCounerChild()
b = InstanceCounerChild()

a.print_count_instances()


class NotRedirectClassMethod(InstanceCounter): ...


x = InstanceCounter()
y = InstanceCounerChild()
x.print_count_instances()
InstanceCounerChild.print_count_instances()

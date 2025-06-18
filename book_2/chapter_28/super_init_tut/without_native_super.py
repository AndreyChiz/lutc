class MySuper:
    def method(self):
        print("in MySuper.method")


class MySub(MySuper):
    def method(self):
        print("starting Sub. method")
        MySuper.method(self)  #                      <== <== <==
        print("ending Sub.method")

"""
Прямой вызове метода суперкласса. Класс Sub замещает
функцию method суперкласса Super собственной специализированной версией, но
внутри самого замещения MySub обращается к версии, экспортируемой MySuper, чтобы
обеспечить выполнение стандартного поведения.
"""

if __name__ == "__main__":
    print("Test start =>")
    inst_MySuper = MySuper()
    inst_MySuper.method()
    print("--//--//--")

    instance_my_sub = MySub()
    instance_my_sub.method()
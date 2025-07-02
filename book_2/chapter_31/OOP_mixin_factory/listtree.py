"""список атрибутов dir() с указанием классов от
которых они унаследованы"""


class ListTree:
    def __init__(self):
        self.__visited = {}

    def __attrnames(self, obj, ident):
        spaces = " " * (ident + 1)
        result = ""
        for attr in obj.__dict__:
            if attr.startswith("__") and attr.endswith("__"):
                result += spaces + f"{attr}"
            else:
                result += spaces + f"{attr}={getattr(obj, attr)}"
            return result

    def __listclasses(self, aClass, ident):
        dots = "." * ident
        if aClass in self.__visited:
            return f"\n{dots}<Class {aClass.__name__}: addres {id(aClass)}>\n"
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, ident)
            above = ""
            for super in aClass.__bases__:
                return "\n{0}<Class {1}:, addres {2}: {3}{4}{5}>\n".format(
                    dots,
                    aClass.__name__,
                    id(aClass),
                    here,
                    above,
                    dots,
                )
    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclasses(self.__class__, 4)
        return '<Instance of {0}, addres {1}: \n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            here,
            above,
        )
    
if __name__=='__main__':
    import OOP_mixin_factory
    OOP_mixin_factory.tester(ListTree)

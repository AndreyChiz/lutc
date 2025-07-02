'''миксин для вывода атрибутов со всего дерева зависимостей'''

class ListInherited:
    '''dir() для вывода списка атрибутов через str'''
    # def __attrnames(self):
    #     '''каша'''
    #     result = ''
    #     for attr in dir(self):
    #         if attr[:2] == '__' and attr[-2:] == '__':
    #             result += '\t{}\n'.format(attr)
    #         else:
    #             result += '\t{}={}\n'.format(attr, getattr(self, attr))
    #     return result


    def __attrnames(self, ident = ' '*4):
        result = "Unders%s\n%s%%s\nOthers%s\n" % ("-" * 77, ident, "-" * 77)
        undres = []
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                undres.append(attr)
            else:
                display = str(getattr(self, attr))[: 82 - (len(ident) + len(attr))]
                result += '%s%s=%s\n' % (ident, attr, display)
        return result % ', '. join(undres)

    def __str__(self):
        return '<Insrance of {}, addres {}:\n{}>'.format(
            self.__class__.__name__,
            id(self),
            self.__attrnames()
        )
    
if __name__ == '__main__':
    import OOP_mixin_factory
    OOP_mixin_factory.tester(ListInherited)
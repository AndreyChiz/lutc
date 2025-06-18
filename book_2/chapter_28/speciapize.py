'''

'''

class MySuper:
    def method(self):
        print("in MySuper.method")

    def deligate(self):
        self.action()


class MyInheritor(MySuper):
    pass


class MyReplacer(MySuper):
    def method(self):
        print("in MyReplacer.method")


class MyExtander(MySuper):
    def method(self):
        print("starting MyExtander.method")
        MySuper.method(self)
        print("ending Extender.method")


class Provider(MySuper):
    def action(self):
        print("In Provider.action")

if __name__ == '__main__':
    for klass in (MyInheritor, MyReplacer, MyExtander):
        print('\n'+klass.__name__+'...')
        klass().method()

    print('\nProvider ...')
    x =Provider()
    x.deligate()
    
    
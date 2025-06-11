class Persone:
    def __init__(
        self,
        name,
        job: str | None = None,
        pay=0,
    ):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]
    
    def give_raise(self, percent):
        self.pay = int(self.pay *(1+percent))

if __name__ == '__main__':
    bob = Persone('Bob Smith')
    sue = Persone('Sue Jones', job='dev', pay=100000)

    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print()
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.1)
    print(sue.pay)
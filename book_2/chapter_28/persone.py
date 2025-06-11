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
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return "Persone({}, {})".format(self.name, self.pay)


class Manager(Persone):
    # def __init__(self, name, pay):
    #     Persone.__init__(self, name, "mngr", pay)

    def __init__(self, name, pay):
        super().__init__(name, "mngr", pay)

    def give_raise(self, percent, bonus=0.1):
        Persone.give_raise(self, percent + bonus)



if __name__ == "__main__":
    bob = Persone("Bob Smith")
    sue = Persone("Sue Jones", job="dev", pay=100000)

    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob)
    print(bob.last_name(), sue.last_name())
    # sue.give_raise(.1)
    print(sue)
    print()
    tom = Manager("Tom Jones", 50000)
    # tom.give_raise(.1)
    print(tom.last_name())
    print(tom)

    print("--all--")
    for hyuman in (bob, sue, tom):
        hyuman.give_raise(0.1)
        print(hyuman)

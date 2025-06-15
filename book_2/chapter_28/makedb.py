from persone import Persone, Manager

bob = Persone("Bob Smith")
sue = Persone("Sue Jones", job="dev", pay=100000)
tom = Manager("Tom Jones", 50000)

import shelve

db = shelve.open("personedb")
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()


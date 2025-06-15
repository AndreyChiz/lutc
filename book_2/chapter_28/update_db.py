import shelve

db = shelve.open("personedb")


for key in db:
    print(key, "=>", db[key])

sue = db["Sue Jones"]
sue.give_raise(0.1)

db["Sue Jones"] = sue

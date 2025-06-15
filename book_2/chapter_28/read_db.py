import shelve

db = shelve.open("personedb")
print(len(db))
print(list(db.keys()))
bob = db["Bob Smith"]
print(bob.last_name())

for key in db:
    print(key, "=>", db[key])

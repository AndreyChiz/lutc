import sys
from collections import namedtuple

persones = []

for numb, line in enumerate(sys.stdin):
    row = [int(i) if i.isdigit() else i for i in line.strip().split()]
    if not numb:
        Persone = namedtuple("Persone", row)
    else:  
        persones.append(Persone(*row))

for persone in persones:
    print(persone.name ) if persone.id == 3 else None

import sys
import timer

reps = 1000

replslist = list(range(reps))


def forLoop():
    res = []
    for x in replslist:
        res.append(x+10)
    return res


def listComp():
    return [x+10 for x in replslist]


def mapCall():
    return list(map((lambda x: x+10), replslist))


def genExp():
    return list(x+10 for x in replslist)


def genFunc():
    def gen():
        for x in replslist:
            yield x+10

    return list(gen())


print(sys.version)

for test in (forLoop, listComp, mapCall, genExp, genFunc):
    (bestof, (total, result)) = timer.best_of_total(5, 1000, test)
    print("%-9s: %.5f => [%s...%s]" % (test.__name__, bestof, result[0], result[-1]))

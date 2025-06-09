# 647 Расширенная версия но любительский вариант
# для измерения времени выполнения функции

import sys
import time
from typing import Callable


timer = time.time if sys.platform[:3] == "win" else time.time


def total(reps: int, func: Callable, *args, **kwargs):
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps: int, func: Callable, *args, **kwargs):
    best = 2**32
    for i in range(reps):
        start = timer()
        ret = func(*args, **kwargs)
        elapsed = timer() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)


def best_of_total(reps1: int, reps2: int, func: Callable, *args, **kwargs):
    # best_rep = (2*32, None)
    # reps_is = (reps1, reps2)

    # for rep in reps_is:
    #     res = bestof(rep, func, *args, **kwargs)
    #     if best_rep < res:
    #         best_rep = res
    # return best_rep
    return bestof(reps1, total, reps2, func, *args, **kwargs)

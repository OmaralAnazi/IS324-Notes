from random import sample


def ForLoop(s):  # O(1) <- Best overall
    for e in s:
        break
    return e  # e is now an element from s


def IterNext(s):  # O(1)
    return next(iter(s))


def ListIndex(s):  # O(n)
    return list(s)[0]


def PopAdd(s):  # O(1)
    e = s.pop()
    s.add(e)
    return e


def RandomSample(s):  # O(n)
    return sample(s, 1)


def SetUnpacking(s):  # O(n)
    e, *_ = s
    return e

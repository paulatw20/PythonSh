import functools


def increment(a):
    return a + 0.1


def printlist(a):

    return str(a) + " "


temperaturas = [35.0, 35.5, 36.0, 36.5, 37.0, 37.5, 38.0, 38.5, 39.0, 39.5, 40.0, 40.5, 41.0, 41.5, 42.0]
x = map(increment, temperaturas)

tempInc = list(x)

y = map(printlist, tempInc)
print(list(y))

print(functools.reduce(lambda a, b: a + b, temperaturas))
print(functools.reduce(lambda a, b: a + b, temperaturas) / len(temperaturas))



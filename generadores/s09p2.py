def infinite_sequence():
    num = 35.0
    #while True
    while num <= 42.0:
        yield num
        num += 0.5

temperaturas = []

for i in infinite_sequence():
    #print(i, end=" ")
    temperaturas.append(i)
    KeyboardInterrupt

print("\n" + str(temperaturas))








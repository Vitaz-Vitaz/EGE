c = 0

for A in range(-100, 100, 1):
    f = 1
    for x in range(-100, 100, 1):
        for y in range(-100, 100, 1):
            if (((((A < x) or (x ** 2 - 7 * x + 10 > 0))) and (((A >= y) or (y ** 2 + 7 * y + 12 > 0))))) == 0:
                f = 0
    if f == 1:
        c += 1
print(c)
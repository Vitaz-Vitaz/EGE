mi = 99999

for A in range(0, 1000):
    flag = True
    for y in range(0, 1000):
        for x in range(0, 1000):
            if ((4 * x + y < A) or (x < y) or (x >= 22)) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)





mi = 99999

for A in range(0, 1000):
    flag = True
    for y in range(0, 1000):
        for x in range(0, 1000):
            if ((x * y < A) or (x < y) or (9 < x)) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)




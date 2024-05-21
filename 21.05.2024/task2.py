print("a b c d")
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                f = (a <= b) and (b <= (not c)) and ((not c) <= d)
                if f:
                    print(a, b, c, d)
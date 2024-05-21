s = 120
ma = -10000
e = 107
while ma < 100:
    for i in range(0, 100):
        if (i * e) % 120 == 1 and i > ma:
            ma = i
print(ma)

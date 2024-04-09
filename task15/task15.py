import math
k = 0
for a in range(1001):
    f = 0
    for x in range(1, 1001):
        if (math.gcd(420, a) == 2 or math.gcd(a, x) != 12 <= math.gcd(110, x) != 11) == 0:
            f = 1
    if f == 0:
        k += 1
#
print(k)

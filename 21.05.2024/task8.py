def do9(s):
    newS = ''
    while s > 0:
        newS = str(s % 9) + newS
        s = s // 9
    return newS

c = 0
for i in range(1000000, 9999999):
    a = do9(i)
    f1 = int(a[0]) % 2 == 0
    f2 = int(a[-1]) % 3 != 0
    f3 = a.count('6') >= 6
    if f1 and f2 and f3:
        c += 1
print(c)

def do3(s):
    newS = ''
    while s > 0:
        newS = str(s % 3) + newS
        s = s // 3
    return newS


dd = []
for i in range(1, 1000):
    a = do3(i)

    f = ''
    if i % 2 == 0:
        f = '2' + a + do3(int(a[-1]) * 2)
        a = f
    if i % 2 != 0:
        f = do3(int(a[0]) * 2) + a + '2'
        a = f

    dd.append(int(f, 3))

dd.sort()
print(dd)

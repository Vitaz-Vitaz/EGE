f = open("17.txt")
s = f.readlines()
a = []
ma17 = 0
for i in s:
    if int(i) > ma17 and int(i) % 100 == 17:
        ma17 = int(i)
    a.append(i[:-2])
print(ma17)
c = 0
allSuMM = 0
for i in range(len(s) - 3):
    i1 = int(s[i])
    i2 = int(s[i + 1])
    i3 = int(s[i + 2])
    k = 0
    if len(str(i1)) == 4:
        k += 1
    if len(str(i2)) == 4:
        k += 1
    if len(str(i3)) == 4:
        k += 1
    f1 = k == 2
    k1 = 0
    if i1 % 5 == 0:
        k1 += 1
    if i2 % 5 == 0:
        k1 += 1
    if i3 % 5 == 0:
        k1 += 1
    f2 = k1 >= 1
    suMM = (i1 + i2 + i3)
    f3 = suMM > ma17

    if f1 and f2 and f3:
        c += 1
        if suMM > allSuMM:
            allSuMM = suMM
print(c, allSuMM)
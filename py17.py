f = open("17var01.txt")
s = f.readlines()
su47 = []
ans = 0
mi = 999999
for i in s:
    if len(str(int(i))) >= 2:
        if int(i) < mi and int(i) % 100 == 25:
            mi = int(i)

print(mi)
print(s)
for i in range(len(s) - 2):
    k = 0
    if len(str(int(s[i]))) == 2:
        k += 1
    if len(str(int(s[i + 1]))) == 2:
        k += 1
    if len(str(int(s[i + 2]))) == 2:
        k += 1
    f1 = k == 1
    i1 = int(s[i])
    i2 = int(s[i + 1])
    i3 = int(s[i + 2])
    f2 = i1 + i2 + i3 < mi
    if f1 and f2:
        ans += 1
        su47.append((int(s[i + 2]) + int(s[i]) + int(s[i + 1])))
print(ans, max(su47))

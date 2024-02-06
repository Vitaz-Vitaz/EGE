f = open("task10.txt")
s = f.readlines()
ans = []
for i in s:
    d = i.replace("\n", "")
    k = d.split("\t")
    ans.append(k)
print(ans)
ccc = 0
for i in ans:
    gg = 0
    d1 = 0
    ma = -99999
    for j in i:
        if int(j) > ma:
            ma = int(j)
        if i.count(j) == 3:
            gg += 1
        if i.count(j) == 1:
            d1 += 1
    f = gg == 6 and d1 == 2
    f2 = i.count(str(ma)) == 1
    if f and f2:
        ccc += 1
print(ccc)


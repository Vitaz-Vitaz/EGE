f = open("9.txt")
s = f.readlines()
ans = []
for i in s:
    d = i.replace("\n", "")
    k = d.split("\t")
    ans.append(k)
print(ans)
c = 1
for i in ans:
    b = []
    dvoe = 0
    su47 = 0
    su57 = 0
    onee = 0
    for j in i:
        b.append(i.count(j))
        if i.count(j) == 1:
            su57 += int(j)
    for k in b:
        if k == 2:
            dvoe += 1
            su47 = int(i[b.index(k)])
        if k == 1:
            onee += 1

    f = dvoe == 2 and onee == 4
    f22 = su47 >= su57 / 4
    if f and f22:
        print(c)
    c += 1
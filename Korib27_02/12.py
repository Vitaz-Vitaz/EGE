a = []
for n in range(3, 1500):
    s = "1" + n * "2"
    while "12" in s or "322" in s or "222" in s:
        if "12" in s:
            s = s.replace("12", "2", 1)
        if "322" in s:
            s = s.replace("322", "21", 1)
        if "222" in s:
            s = s.replace("222", "3", 1)
    d = list(s)
    r = 0
    for j in d:
        r += int(j)
    a.append(r)
print(max(a))
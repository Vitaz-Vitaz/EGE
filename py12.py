a = []
for n in range(3, 200):
    s = "1" + n * "2"
    while "12" in s or "3322" in s or "2222" in s:
        if "12" in s:
            s = s.replace("12", "33", 1)
        if "2222" in s:
            s = s.replace("2222", "1", 1)
        if "3322" in s:
            s = s.replace("3322", "21", 1)
    d = list(s)
    r = 0
    for j in d:
        r += int(j)
    if r == 218:
        a.append(n)
print(min(a))

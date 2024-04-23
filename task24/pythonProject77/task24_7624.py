f = open("24_7624.txt")
s = f.readline()
q = 'XYZ'
k = 1
ans = 1
for i in range(len(s) - 1):
    if s[i] in q and s[i + 1] in q:
        k = 1
    else:
        k += 1
        ans = max(ans, k)
print(ans)

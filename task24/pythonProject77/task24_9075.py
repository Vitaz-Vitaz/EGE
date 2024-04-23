f = open("24_7094.txt")
s = f.readline()
chet = 'AU'
nechet = 'CDF'
k = 1
ans = 1
i = 0
while i < len(s) - 1:
    if s[i] in nechet and s[i + 1] in chet:
        k += 2
        ans = max(ans, k)
        i += 2
    else:
        k = 0
        i += 1
print(ans)

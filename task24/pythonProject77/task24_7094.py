f = open("24_9075.txt")
s = f.readline()
chet = '02468'
nechet = '13579'
k = 1
ans = 1
for i in range(len(s) - 1):
    if (s[i] in chet and s[i + 1] in nechet) or (s[i] in nechet and s[i + 1] in chet):
        k = 1
    else:
        k += 1
        ans = max(ans, k)
print(ans)

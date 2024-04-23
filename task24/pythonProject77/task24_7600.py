f = open("24_7600.txt")
s = f.readline()
q = 'QRS'
k = 1
ans = 1
for i in range(len(s) - 1):
    if s[i] in q and s[i + 1] in q:
        k = 1
    else:
        k += 1
        ans = max(ans, k)
print(ans)

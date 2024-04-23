f = open("24_8959.txt")
s = f.readline()
ans = 0
k = 0
i = 0
while i < len(s) - 2:
    if s[i] == 'E' and s[i + 1] == 'A':
        k += 2
        ans = max(ans, k)
        i += 2
    elif s[i] == 'N' and s[i + 1] == 'P' and s[i + 2] == 'C':
        k += 3
        ans = max(ans, k)
        i += 3
    else:
        k = 0
        i += 1
print(ans)


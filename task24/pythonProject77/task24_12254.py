f = open("24_12254.txt")
s = f.readline()
ans = 0
k = 0
i = 0
while i < len(s) - 2:
    if s[i] == 'R' and s[i + 1] == 'S' and s[i + 2] == 'Q':
        k += 3
        ans = max(ans, k)
        i += 3
    else:
        k = 0
        i += 1
print(ans)
print("RSQ" * 17)

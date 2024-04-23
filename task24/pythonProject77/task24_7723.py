ans = 0
k = 0
i = 0
while i < len(s) - 1:
    if (s[i] == 'A' and s[i + 1] == 'C') or (s[i] == 'A' and s[i + 1] == 'B'):
        k += 2
        ans = max(ans, k)
        i += 2
    else:
        k = 0
        i += 1
print(ans)

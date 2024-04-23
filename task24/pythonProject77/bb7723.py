f = open("24_7723.txt")
s = f.readline()
a = ['18', '88', '11', '81']
ans = 0
k = 0
i = 0
while i < len(s) - 2:
    if (s[i] + s[i + 1]) in a and s[i + 2] in "DR":
        k += 3
        ans = max(ans, k)
        i += 3
    else:
        k = 0
        i += 1
print(ans)

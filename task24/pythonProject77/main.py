f = open("24_5171.txt")
s = f.readline()
s = s.replace('CA', '1')
ans = 0
k = 0
i = 0
for i in range(len(s)):
    if s[i] == '1':
        k += 2
        ans = max(ans, k)
        i += 2
    else:
        k = 0
print(ans)
# print("CA" * 27)

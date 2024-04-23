f = open("24_9791.txt")
s = f.readline()
h = ['18', '11', '81', '88']
k = 0
ans = 0
i = 0
for i in range(len(s)):
    if s[i] not in h:
        k = 0
    else:
        k += 1
        ans = max(ans, k)

print(ans)

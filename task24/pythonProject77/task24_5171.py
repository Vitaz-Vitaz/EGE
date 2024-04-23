f = open("24_5171.txt")
s = f.readline()
ans = 0
k = 0
i = 0
while i < len(s):
    if s[i] == 'C' and s[i + 1] == 'A':
        k += 2
        ans = max(ans, k)
        i += 2
    else:
        k = 0
        i += 1
print(ans)
# print("CA" * 27)

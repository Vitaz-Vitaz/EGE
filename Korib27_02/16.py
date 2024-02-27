s = [0] * 2027
for i in range(0, 7):
    s[i] = 7
for i in range(7, 2026):
    print(i, s[i])
    s[i] = i + 1 + s[i - 2]
print(s[2024] - s[2020])
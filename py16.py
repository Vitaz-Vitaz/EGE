s = [0] * 2027
s[1] = 5
for i in range(2, 2026):
    print(i, s[i])
    s[i] = 2 * i + 1 + s[i - 1]
print(s[2024] - s[2022])

a = [1] * 3 + [0] * 1000
for i in range(3, 1003):
    if i % 3 == 0:
        a[i] = a[i // 3] + 4 * i
    else:
        a[i] = i * i * i - 26
for i in range(len(a)):
    if a[i] < 300:
        print(i)

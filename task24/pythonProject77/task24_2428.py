f = open("24_2428.txt")
s = f.readline()
ans = 0
k = 0
i = 0
for i in range(1, 100000):
    if "XYZ" * i in s:
        print(i)
print(('YZ' + 22 * "XYZ" + "X") in s)


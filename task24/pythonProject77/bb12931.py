f = open("24_12931.txt")
s = f.readline()
for i in range(1000):
    if "VWXYZ" * i in s:
        print(i)
print('VWXYZ' * 7)

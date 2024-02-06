s = "0123456789ABCDEFGHIJKLM"
mi = 999999
c = 0
for i in s:
    chislo1 = "1" + i + "1" + i + "1" + i + "1" + i + "1"
    chislo2 = "20" + i + "24"
    chislo3 = "1" + i + "235"
    ans = int(chislo1, 23) + int(chislo2, 23) + int(chislo3, 23)
    if ans % 22 == 0:
        if int(i, 23) < mi:
            mi = int(i, 23)
            c = ans // 22
print(c)
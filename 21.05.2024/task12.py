s = '3' + 40 * '4' + 25 * '2' + '3'
while '3' in s:
    if '342' in s:
        s = s.replace('342', '4123', 1)
    if '34' in s:
        s = s.replace('34', '413', 1)
    if '32' in s:
        s = s.replace('32', '13', 1)
    if '33' in s:
        s = s.replace('33', '424', 1)
print(sum(list(map(int, list(s)))))
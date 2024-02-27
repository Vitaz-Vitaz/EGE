def tofree(a):
    n = ''
    while a > 0:
        n = str(a % 3) + n
        a //= 3
    return n


for N in range(1, 10000):
    chet = tofree(N)
    if N % 3 == 0:
        chet += chet[-2:]
    else:
        chet += str(tofree((N%3)*5))
    ans = int(chet, 3)
    if ans > 133:
        print(N)
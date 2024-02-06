def tofour(a):
    n = ''
    while a > 0:
        n = str(a % 4) + n
        a //= 4
    return n


for N in range(1, 10000):
    chet = tofour(N)
    if N % 4 == 0:
        chet += chet[-2:]
    else:
        chet += str(tofour((N%4)*2))
    ans = int(chet, 4)
    if ans < 261:
        print(N)

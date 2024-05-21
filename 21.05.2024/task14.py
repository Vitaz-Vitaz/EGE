alphabet = '0123456789ABCDEFGHIJK'
ma = 0
maX = 0
maY = 0
for x in alphabet:
    for y in alphabet:
        if (int('943697' + x + '21', 21) - int('2' + y + '9253', 21)) % 20 == 0:
            if int(x, 21) - int(y, 21) > ma:
                maX = x
                maY = y
                ma = int(x, 21) - int(y, 21)
print(maX, maY)
print((int('943697' + 'K' + '21', 21) - int('2' + '0' + '9253', 21)) / 20)
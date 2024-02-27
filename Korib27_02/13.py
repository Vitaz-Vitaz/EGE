al = "01"
s = 0
for x1 in al:
    for x2 in al:
        for x3 in al:
            for x4 in al:
                for x5 in al:
                    for x6 in al:
                        for x7 in al:
                            for x8 in al:
                                for x9 in al:
                                    for x10 in al:
                                        ans = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10
                                        if ans.count("1") <= 4:
                                            s += 1
print(s)

al = "ЕКМОПРТЬЮ"
i = 1
aw = 0
for x1 in al:
    for x2 in al:
        for x3 in al:
            for x4 in al:
                for x5 in al:
                    for x6 in al:
                        for x7 in al:
                            for x8 in al:
                                ans = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8

                                if x1 != "Ь" and ans.count("К") == 2 and i % 2 != 0:
                                    aw = i
                                i += 1
print(aw)

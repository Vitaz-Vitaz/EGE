al = "АВИОРТФ"
i = 1
aw = 0
for x1 in al:
    for x2 in al:
        for x3 in al:
            for x4 in al:
                for x5 in al:
                    for x6 in al:
                        ans = x1 + x2 + x3 + x4 + x5 + x6
                        if x1 != "О" and ans.count("Р") == 2 and i % 2 == 0:
                            aw += 1
                        i += 1
print(aw)


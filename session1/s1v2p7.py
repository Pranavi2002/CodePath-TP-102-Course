def nanana_batman(x):
    if x == 0:
        print('"batman!"')
    else:
        i = 1
        ans = ""
        for i in range(x+1):
            ans += "na"
        ans += " batman!"
        print('"' + ans + '"')

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
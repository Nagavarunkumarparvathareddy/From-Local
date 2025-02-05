s = "PYTHON"
i = 0
l = len(s)
while (i < l):
    if s[i] == 'T' or s[i] == 'H':
        i += 1
        continue
    else:
        print(s[i])
        i += 1
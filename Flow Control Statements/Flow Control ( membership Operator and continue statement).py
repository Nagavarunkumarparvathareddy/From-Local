s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
l = len(s)
while (i < l):
    if s[i] in ['A','E','I','O','U']:
        i += 1
        continue
    else:
        print(s[i] , end='')
        i += 1
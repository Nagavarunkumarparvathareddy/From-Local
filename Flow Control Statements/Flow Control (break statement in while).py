s = input().lower()
l = len(s)
i = 0
while (i < l):
    if s[i] == 'b':
        break
    else:
        print(s[i])
        i += 1
else:
    print('I am else part of while')
print('Prog execution completed')
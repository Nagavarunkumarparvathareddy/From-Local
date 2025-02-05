with open('ind vs aus test3.info') as fp:
    data = fp.read()
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    a = []
    chars = 0
    l = str(data).split()
    list1 = list(l)
    for word in list1:
        for char in list(word):
            if char in vowels:
                a.append(word)
                chars += len(word)
                print(word, end=' ')
                break
print('\n'+str(len(a)))
print(chars)
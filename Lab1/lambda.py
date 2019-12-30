def mk_thg(a, b, c):
    if c > 0:
        return lambda a, b: a + b
    else:
        return lambda a, b: -a - b


p = mk_thg(1, 2, 1)
print(p(3,4))

text_list = ['x','xxx','xxxxx','xxxxxxx','']
napis='lala'
f=lambda x:len(x)
print(f(napis))


print(list(map(lambda x:len(x),text_list)))
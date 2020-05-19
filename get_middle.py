def get_middle(s):
    print(len(s))
    i = (len(s)-1//2)
    print(i)
    return s[i:-i] or s


print(get_middle('test'), 'es')
print(get_middle("testing"),"t")
print(get_middle("middle"),"dd")
print(get_middle("A"),"A")
print(get_middle("of"),"of")
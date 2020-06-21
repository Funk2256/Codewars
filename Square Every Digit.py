def square_digits(num):
    strs = str(num)
    cl_lst = []
    for i in strs:
        integer = int(i)**2
        cl_lst.append(integer)
    joins = (''.join(map(str, cl_lst)))
    return int(joins)



print(square_digits(9119))
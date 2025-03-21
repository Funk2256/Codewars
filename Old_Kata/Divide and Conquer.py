def div_con(x):
    str_list = []
    num_list = []
    for item in x:
        if isinstance(item, str):
            str_list.append(int(item))
        else:
            num_list.append(int(item))

    return (sum(num_list) - sum(str_list))


""""
def div_con(lst):
    return sum(n if isinstance(n, int) else -int(n) for n in lst) - not my result
"""

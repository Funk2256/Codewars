def namelist(names):
    print(len(names))
    if len(names) == 0:
        return ''

    if len(names) == 1:
        for x in names:
            return x.get('name')

    if len(names) == 2:
        name_list = []
        for y in names:
            name_list.append(y.get('name'))
        return(f'{name_list[0]} & {name_list[-1]}')

    if len(names) > 2:
        list_name = []
        for name in names:
            list_name.append(name.get('name'))
        str_list =  ", ".join(y["name"] for y in names[0:-1:])
        return(str_list + ' & ' + list_name[-1])


names = [{'name': 'Bart'}]
print(namelist(names))
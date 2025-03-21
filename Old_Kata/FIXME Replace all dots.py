import re


def replace_dots(str):
    return re.sub(r".", "-", str)


print(replace_dots('.--.'))

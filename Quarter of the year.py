def quarter_of(month):
    if month <= 3:
        return 1
    if month <=6:
        return 2
    if month <=9:
        return 3
    if month <=12:
        return 4
    elif month >= 13:
        return ('Bad number :(')
print(quarter_of(11))
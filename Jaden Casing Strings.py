import re

def to_jaden_case(string):
    lis_clear = []
    spl = re.split(r" ", string)
    for x in spl:
        lis_clear.append(x.capitalize())
    delimiter = ' '
    my_str = delimiter.join(lis_clear)
    return my_str

"""to_jaden_case("If There Is Bread Winners, There Is Bread Losers. But You Can'T Toast What Isn'T Real." 
should equal "If There Is Bread Winners, There Is Bread Losers. But You Can't Toast What Isn't Real.")"""

string = "If There Is Bread Winners, There Is Bread Losers. But You Can'T Toast What Isn'T Real."

to_jaden_case(string)

"""b = "If There Is Bread Winners, There Is Bread Losers. But You Can't Toast What Isn't Real."

#print(a)
#print(b)
if a == b:
    print('True')
else:
    print("False")"""
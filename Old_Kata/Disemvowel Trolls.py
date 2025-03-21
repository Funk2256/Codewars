def disemvowel(string):
    list_vowels = ['a', 'e', 'i', 'o', 'u', 'O', 'I']
    list_string = [x for x in string if x not in list_vowels]
    return (''.join(map(str, list_string)))


print(disemvowel('This website is for losers LOL!'))

a = "N ffns bt,\nYr wrtng s mng th wrst I'v vr rd"
b = "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"

if a == b:
    print(True)
if a != b:
    print(False)

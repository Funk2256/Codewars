"""The Story:
Aliens from Kepler 27b have immigrated to Earth! They have learned English and go to our stores,
eat our food, dress like us, ride Ubers, use Google, etc. However, they speak English a little differently.
Can you write a program that converts our English to their Alien English?

Task:
Write a function that receives a lowercase string and converts it from our English to Alien English.
They tend to speak the letter a like o and o like a u.

"hello" ---> "hellu"
"codewars" ---> "cudewors"""


def convert(st):
    new_str = ''
    for i in st:
        if i == 'a':
            new_str += 'o'
        elif i == 'o':
            new_str += 'u'
        else:
            new_str += i
    return new_str


result = convert('codewars')
print(result)

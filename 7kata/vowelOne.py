"""vowelOne
Write a function that takes a string and outputs a strings of 1's and 0's where vowels
become 1's and non-vowels become 0's.

All non-vowels including non alpha characters (spaces,commas etc.) should be included.

Examples:

vowelOne "abceios" -- "1001110"
vowelOne "aeiou, abc" -- "1111100100"""


def vowel_one(s):
    trans_table = str.maketrans('aeiouAEIOU', '1111111111')
    result_table = s.translate(trans_table)
    result = ''.join('1' if char in 'aeiouAEIOU' else '0' for char in s)
    return result


s = 'aasdsdfdgvbdghuii'
result = vowel_one(s)
print(result)

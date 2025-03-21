# Create a function that takes an integer as an argument and returns
# "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = even_or_odd(3)
print(result)

"""Более компактный вариант

def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'
	
"""

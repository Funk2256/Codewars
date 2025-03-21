"""Write a function which reduces fractions to their simplest form!
Fractions will be presented as an array/tuple (depending on the language) of
strictly positive integers, and the reduced fraction must be returned as an array/tuple:

input:   [numerator, denominator]
output:  [reduced numerator, reduced denominator]
example: [45, 120] --> [3, 8]
All numerators and denominators will be positive integers.

Note: This is an introductory Kata for a series... coming soon!"""


def reduce_fraction(fraction):
    numerator = fraction[0]
    denominator = fraction[1]

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    gcd_value = gcd(numerator, denominator)

    # Сокращаем дробь
    reduced_numerator = numerator // gcd_value
    reduced_denominator = denominator // gcd_value

    # Возвращаем сокращенную дробь в виде кортежа
    return (reduced_numerator, reduced_denominator)


result = reduce_fraction((80, 120))
print(result)

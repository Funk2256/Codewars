def solution(numbers):
    # TODO convert int to roman string
    diction_rims_number = {1: 'I', 2: 'V', 3: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    numbers_str = str(numbers)
    for x in numbers_str:
        print(diction_rims_number[x])


print(solution(15))

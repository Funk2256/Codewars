def high_and_low(numbers):
    cl_ls = []

    for x in numbers.split(' '):
        cl_ls.append(int(x))

    cl_ls.sort()
    cl_ls.reverse()

    numbers_one = cl_ls[0]
    numbers_two = cl_ls[-1]
    numbers = f'{numbers_one} {numbers_two}'

    return numbers





high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")  # return "5 1"

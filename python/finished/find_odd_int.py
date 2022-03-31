def find_it(seq):
    numbers = dict()
    for elem in seq:
        if elem in numbers:
            numbers[elem] += 1
        else:
            numbers[elem] = 1
    return next(number for number in numbers
                if numbers[number] % 2 != 0)
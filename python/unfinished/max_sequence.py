#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
def max_sequence(arr):
    if not arr or not all([True if num > 0 else False for num in arr]):
        return 0

print(max_sequence([-1, -2]))

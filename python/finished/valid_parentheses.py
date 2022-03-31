#https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
def valid_parentheses(string):
    valid_count = 0
    for elem in string:
        if elem is '(':
            valid_count += 1
        if elem is ')':
            if valid_count <= 0:
                return False
            valid_count -= 1
    if valid_count == 0:
        return True
    else:
        return False

#Finished
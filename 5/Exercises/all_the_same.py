from sys import exit


collection = [1, 1, 1]

if len(collection) == 0 or len(collection) == 1:
    return True

first_element = collection[0]
i = 1
while i < len(collection):
    if collection[i] != first_element:
        return False
    i += 1
return True


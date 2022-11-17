set1 = {1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 8}
set2 = { 4, 5, 5, 6, 7, 8, 9, 10, 11, 12}

union = set1 | set2
print(f'The union of the two sets is: ', union)

intersection = set1 & set2
print(f'The intersection of the two sets is: ', intersection)

difference = set1 - set2
print(f'The difference of the two sets is: ', difference)

asy_difference = set1 ^ set2
print(f'The asymetric difference of the two sets is: ', asy_difference)


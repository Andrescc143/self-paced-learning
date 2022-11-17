#Code to search and sum all number in the text
import re

text = open('Regular expressions/regex_sum_1070176.txt')
total = 0
for line in text:
    numbers = re.findall('[0-9]+', line)
    numbers = [int(number) for number in numbers]
    total = total + sum(numbers)
print(total)

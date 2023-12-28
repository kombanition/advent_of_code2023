import regex as re
import word2number
from word2number import w2n

numbers = ('one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9')

with open('/home/nik/snap/thonny/current/code_advent_2023/day#1/puzzle_input.txt') as file:
    lines = []
    for line in file:
#        print(line)
        
        lines.append(line)

list = []

for string in lines:

    match = re.findall(numbers, string, overlapped = True)
    for index, number in enumerate(match):        
        
        if len(match[index]) > 1: 
            match[index] = w2n.word_to_num(match[index])
            match[index] = str(match[index])
        
#    print(match)

    number = int((match[0][0] + match[-1][-1]))
    
    list.append(number)
    

print(list)
    
print(sum(list))
    

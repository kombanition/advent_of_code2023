import re
    
with open('/home/nik/Desktop/puzzle_input.txt', 'r') as file:
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)
        if line == None:
            break
list = []

for string in lines:

    regex = '\d+'
    match = re.findall(regex, string)
    number = int((match[0][0] + match[-1][-1]))
    
    list.append(number)
    
print(sum(list))
    

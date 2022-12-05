#!/usr/bin/python3
import string

f = open("./day03/input03.txt")
lines_per_three = []
lines = f.readlines()
stripped_lines = [x.strip() for x in lines]

for i in range(0, len(stripped_lines), 3):
    lines_per_three.append(stripped_lines[i:i+3])

priorities_sum = 0
item_types = list(string.ascii_letters)

for group_of_three in lines_per_three:
    common_item_type = ''.join(set(group_of_three[0]).intersection(group_of_three[1], group_of_three[2]))

    priority = item_types.index(common_item_type) + 1
    priorities_sum += priority

print ("Sum of all priority items: ", priorities_sum)








#!/usr/bin/python3
import string

f = open("./input03.txt")
lines = f.readlines()

priorities_sum = 0
item_types = list(string.ascii_letters)

for linenumber, line in enumerate(lines):
    first_compartment, second_compartment = line[slice(0,len(line)//2)], line[slice(len(line)//2, len(line))]
    common_item_type = ''.join(set(first_compartment).intersection(second_compartment))

    priority = item_types.index(common_item_type) + 1
    priorities_sum += priority

print ("Sum of all priority items: ", priorities_sum)








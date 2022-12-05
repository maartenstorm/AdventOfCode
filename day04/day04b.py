#!/usr/bin/python3

f = open("./day04/input04.txt")
lines = f.readlines()

result = 0
for linenumber, line in enumerate(lines):
        split_line = line.rstrip().split(',',2)
        first_pair = split_line[0].split('-',2)
        second_pair = split_line[1].split('-',2)

        # range(start, end+1) om inclusive te maken
        contain = (any(elem in range(int(first_pair[0]),int(first_pair[1])+1) for elem in range(int(second_pair[0]),int(second_pair[1])+1))
                    or any(elem in range(int(second_pair[0]),int(second_pair[1])+1) for elem in range(int(first_pair[0]),int(first_pair[1])+1)))

        if contain:
            result += 1

print (result)


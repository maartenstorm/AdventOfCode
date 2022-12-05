#!/usr/bin/python3

# translate letters to numbers
shape_number = { 'A': 0, 'B': 1, 'C': 2,
                    'X': 0, 'Y': 1, 'Z': 2 }

# win-lose table. Selectes cell based on selected shapes returns the index of the winning shape
win_lose = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]

my_points = 0
f = open("./input02.txt")
lines = f.readlines()

for linenumber, line in enumerate(lines):
    if line != '':
        line = line.strip()
        elf, me = line[0], line[-1]
        winner = win_lose[shape_number[elf]][shape_number[me]]

        # calculate points
        my_points += (shape_number[me] + 1) # value of the shape is one higher than the index
        if winner == shape_number[me]:
            my_points += 6

        elif winner == shape_number[elf]:
            pass # no points for me

        elif winner == -1:
            my_points += 3 # draw

print ("My total score: ", my_points)

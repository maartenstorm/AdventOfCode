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
        if me == 'X':
            # need to lose
            my_shape = [i for i, value in enumerate(win_lose[shape_number[elf]]) if value == shape_number[elf]]
            my_points += (my_shape[0] + 1) # value of the shape is one higher than the index

        elif me == 'Y':
            # need to draw
            my_shape = [shape_number[elf]]
            my_points += 3
            my_points += (my_shape[0] + 1) # value of the shape is one higher than the index

        elif me == 'Z':
            # need to win
            my_shape = [i for i, value in enumerate(win_lose[shape_number[elf]]) if (value != shape_number[elf] and value != -1)]
            my_points += 6
            my_points += (my_shape[0] + 1) # value of the shape is one higher than the index

print ("My total score: ", my_points)

#        [Q] [B]         [H]
#    [F] [W] [D] [Q]     [S]
#    [D] [C] [N] [S] [G] [F]
#    [R] [D] [L] [C] [N] [Q]     [R]
#[V] [W] [L] [M] [P] [S] [M]     [M]
#[J] [B] [F] [P] [B] [B] [P] [F] [F]
#[B] [V] [G] [J] [N] [D] [B] [L] [V]
#[D] [P] [R] [W] [H] [R] [Z] [W] [S]
# 1   2   3   4   5   6   7   8   9

stacks = [['D', 'B', 'J', 'V'],
          ['P', 'V', 'B', 'W', 'R', 'D', 'F'],
          ['R', 'G', 'F', 'L', 'D', 'C', 'W', 'Q'],
          ['W', 'J', 'P', 'M', 'L', 'N', 'D', 'B'],
          ['H', 'N', 'B', 'P', 'C', 'S', 'Q'],
          ['R', 'D', 'B', 'S', 'N', 'G'],
          ['Z', 'B', 'P', 'M', 'Q', 'F', 'S', 'H'],
          ['W', 'L', 'F'],
          ['S', 'V', 'F', 'M', 'R']]

def move_crates (number_of_crates, stack_from, stack_to):
    count = 0
    while (count < number_of_crates):
        print("stack_from: ",stacks[stack_from])
        print("stack_to: ", stacks[stack_to])

        count += 1
        if stacks[stack_from]:
            crate = stacks[stack_from].pop()
            stacks[stack_to].append(crate)

        print("new stack_from: ",stacks[stack_from])
        print("new stack_to: ", stacks[stack_to])

f = open("./day05/input05.txt")
lines = f.readlines()

for linenumber,line in enumerate(lines):
    if linenumber > 9:
        print(linenumber, line)
        rearrangement_data = []
        for i in line.split():
            if i.isdigit():
                rearrangement_data.append(int(i))

        number_of_crates = rearrangement_data[0]
        stack_from = rearrangement_data[1] - 1
        stack_to = rearrangement_data[2] -1

        move_crates (number_of_crates, stack_from, stack_to)

top_crates = [stack[-1] for stack in stacks]
print ("Top crates: ", top_crates)



#!/usr/bin/python3

f = open("./input01.txt")
lines = f.readlines()
elf_total = []
elf_number = 1
elves = []
for linenumber, line in enumerate(lines):
    line = line.rstrip()
    print(line)
    if line == '':
        print(sum(elf_total))
        elves.append((elf_number, sum(elf_total)))
        elf_total = []
        elf_number = elf_number + 1
    elif line is lines[-1]:
        elf_total.append(int(line))
        elves.append((elf_number, sum(elf_total)))
        elf_total = []
    else:
        elf_total.append(int(line))

elves.sort(key=lambda y:y[1], reverse=True)

print("Elf with most calories is elf no. %i, carrying %i calories" % (elves[0][0], elves[0][1]))

top_three = (elves[:3])

result = 0
for i in top_three:
    result += i[1]

print("Three elves carrying most calories in total:", result)






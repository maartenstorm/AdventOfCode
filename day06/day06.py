#!/usr/bin/python3

def find_duplicate(chars):
    for char in chars:
        if chars.count(char) > 1:
            return True

#input_string = "bvwbjplbgvbhsrlpgdmjqwftvncz" #5
#input_string = "nppdvjthqldpwncqszvftbrmjlhg" #6
#input_string = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" #10
#input_string = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" #11

def find_start(input_string):
    a=0
    start_char = 0
    while a < len(input_string):
        sub_string = input_string[a:4+a]
        print(sub_string)
        if find_duplicate(sub_string):
            # check next
            b=0
            while b < len(sub_string):
                new_sub_string = input_string[a+b:4+a+b]
                print("sub: ",new_sub_string)
                if find_duplicate(new_sub_string) == None:
                    start_char = a + len(sub_string) + 1 + (b-1)
                    return start_char
                b += 1
        a += 1

f = open("./day06/input06.txt")
lines = f.readlines()
print(lines)

for linenumber,line in enumerate(lines):
    input_string = line

print ("START: ",find_start(input_string))


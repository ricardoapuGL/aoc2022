#!/bin/python

from numpy import array, append, sum
TOP_CALORIES_LIST_LEN = 3

top_highest_calories = array([])

curr_elf_calories = 0
    
with open("01.txt") as input:
    # Puzzle 1
    for line in input:
        line = line.strip('\n')
        print(line)
        if not line: # is newline, new elf
            if len(top_highest_calories) < TOP_CALORIES_LIST_LEN:
                top_highest_calories = append(top_highest_calories, [curr_elf_calories])
                top_highest_calories.sort()
            else:
                if curr_elf_calories > top_highest_calories[0]:
                    top_highest_calories[0] = curr_elf_calories
                    top_highest_calories.sort()
            print("top_highest_calories: ", top_highest_calories)
            curr_elf_calories = 0
        else:
            curr_elf_calories += int(line)
            print("curr_elf_calories: ", curr_elf_calories)
    print(f'final top_highest_calories: {top_highest_calories}\n Total: {sum(top_highest_calories, dtype=int)}')
        
input = 'input5.txt'
stack_width = 4  # characters per stack
step2 = True

# initialize stacks
with open(input, 'r') as f:
    number_stacks = len(f.readline()) // stack_width
    stacks = [[] for _ in range(number_stacks)]

with open(input, 'r') as f:
    for line in f.readlines():
        if line.startswith('move'):  # move crates
            words = line.split(' ')
            amount, move_from, move_to = int(words[1]), int(words[3])-1, int(words[5])-1
            move_list = [stacks[move_from].pop() for _ in range(amount)]
            if step2:  # reverse list for step 2
                move_list.reverse()
            stacks[move_to] = stacks[move_to] + move_list
        else:  # fill stacks
            stack_counter = 0
            for stack in range(1, len(line), stack_width):
                if line[stack].isalpha():
                    stacks[stack_counter].insert(0,(line[stack]))
                stack_counter += 1

    print(''.join([stack[-1] for stack in stacks]))

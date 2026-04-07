import random

size = int(input("Enter the tree size: "))

row_num = 1

trunk = ' ' * size + '#'

for i in range(0,size): # how many rows
    row_max_char_length = (2 * row_num - 1)
    spaces = ' ' * (size - i)
    this_row = ''
    for j in range(0,row_max_char_length):
        if random.randint(1,4) == 1:
            this_row += 'o'
            continue
        this_row += '^'


    print(spaces + this_row)
    row_num += 1
    
print(trunk)
print(trunk)


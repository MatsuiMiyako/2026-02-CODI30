import random

size = int(input("Enter the tree size: "))

row_num = 1

trunk = ' ' * (size - 1) + '#'

while size > 0: # how many rows
    row_max_char_length = (2 * row_num - 1)
    spaces = ' ' * (size - 1)
    this_row = ''
    while row_max_char_length > 0:
        if random.randint(1,4) == 1:
            this_row += 'o'
            row_max_char_length -=1
            continue
        this_row += '^'
        row_max_char_length -=1
    
    size -= 1
    print(spaces + this_row)
    row_num += 1
    
print(trunk)
print(trunk)


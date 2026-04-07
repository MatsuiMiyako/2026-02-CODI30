size = int(input("Enter the tree size: "))

row_num = 1

trunk = ' ' * (size -1) + '#'

while size > 0:
    spaces = ' ' * (size - 1)
    branches = (2 * row_num - 1) * '^'
    print(spaces + branches)
    row_num += 1
    size -= 1


print(trunk)
print(trunk)


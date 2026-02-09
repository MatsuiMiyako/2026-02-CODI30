print('Enter the tree size: ')
size = int(input())

i = 1

while i <= size:
    print(' ' * (size - i) + '^' * (2 * i - 1))
    i += 1

for j in range(2):
    print(' ' * 4 + '#')

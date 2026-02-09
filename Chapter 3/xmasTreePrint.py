import random

print('Enter the tree size: ')
size = int(input())

ornament_chance = 1

i = 1

while i <= size:
# 1/4 chance of an ornament being printed instead of a '^', check per every ^:
    line = ''
    for j in range(2 * i - 1):
        if random.randint(1, 4) == ornament_chance:
            line += 'o'
        else:
            line += '^'
    print(' ' * (size - i) + line)
    i += 1


for k in range(2):
    print(' ' * 4 + '#')

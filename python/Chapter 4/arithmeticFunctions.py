def plus_one(number):
    return number + 1

def add(number1, number2):
    total_sum = number1
    for i in range(number2):
        total_sum = plus_one(total_sum)
    return total_sum

print(add(4,3))

def multiply(number1, number2):
    total_product = 0
    for i in range(number2):
        total_product = add(total_product, number1)
    return total_product

print(multiply(4,3))
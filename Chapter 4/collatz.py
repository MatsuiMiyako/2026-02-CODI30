def collatz(number):
    if number % 2 ==0:
        return number // 2
    
    if number % 2 == 1:
        return number * 3 + 1


print("Enter number: ")
try:
    currentNumber = int(input())
    numberList = ""

    while currentNumber != 1:
        currentNumber = collatz(currentNumber)
        numberList += str(currentNumber) + ' '

    print(numberList, sep=' ')
except:
    print("Please enter a integer.")

try:
    number1 = int(input('enter a number'))
    number2 = int(input('enter a number'))
    number3 = number1 + number2
    print(number3)
except ValueError:
    print('Only numbers are allowed')

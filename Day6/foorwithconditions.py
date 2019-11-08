# i want to print 1-100 but skip 30-40

numbers = range(1,101)

for number in numbers:
    if number == 30:
        break
    print(number)

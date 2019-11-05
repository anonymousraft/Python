#creating math table
number = int(input('Enter the number to generate a table\n'))
i = 1
while i <= 10:
    result = number*i
    print( str(number) + ' X ' + str(i) + ' = ' + str(result) )
    i = i + 1
#traffic light program
import time
import random
signal = random.randint(1,3)
lighttoglow = ''
if signal == 1:
    lighttoglow = 'Green'
    print('Light is ' + lighttoglow)
    print('You can move forward')
elif signal == 2:
    lighttoglow = 'Yellow'
    print('Light is ' + lighttoglow)
    print('Please Wait for few minutes')
else:
    lighttoglow = 'Red'
    print('Light is ' + lighttoglow)
    print('Please Stop')




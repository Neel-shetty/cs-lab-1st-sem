
try:
    n = int(input('Enter an integer'))
    quotient = int(100/n)
    print('100/{} = {}'.format(n,quotient))
except Exception as error:
    print(error)
else: 
    print(2*2)
finally:
    print('try catch exited')
# SRS Document, software requirement specification
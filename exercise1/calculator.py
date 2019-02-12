def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


print('Welcome to Python awesome calculator!')
cont = 'y'
while cont == 'y':
    print('What type of calculation do you want to perform?')
    print('Enter 1 for add (+)')
    print('Enter 2 for subtract (-)')
    print('Enter 3 for multiply (*)')
    print('Enter 4 for divide (/)')

    operation = int(input(''))
    first = int(input('Enter the first number: '))
    second = int(input('Enter the second number: '))
    global result

    if operation == 1:
        result = add(first, second)
    elif operation == 2:
        result = sub(first, second)
    elif operation == 3:
        result = mul(first, second)
    elif operation == 4:
        result = div(first, second)
    else:
        print('That is not a valid operation, please try again')

    print('The result is {}'.format(result))

    cont = input('Do you want to do another caluclation (y/n)? ')

print('Thanks for using me! See you soon!')

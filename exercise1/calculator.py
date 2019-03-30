def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def calculate(op, first_num, second_num):
    if op == 1:
        return add(first_num, second_num)
    elif op == 2:
        return sub(first_num, second_num)
    elif op == 3:
        return mul(first_num, second_num)
    else:
        return div(first_num, second_num)


# The program
print('Welcome to Python awesome calculator!')
cont = 'y'
while cont == 'y':
    operation = int(input('What type of calculation do you want to perform? \n'
                          'Enter 1 for add (+) \n'
                          'Enter 2 for subtract (-) \n'
                          'Enter 3 for multiply (*) \n'
                          'Enter 4 for divide (/) \n'))

    if operation not in range(1, 5):
        print('That is not a valid operation, please try again')
        continue

    first = int(input('Enter the first number: '))
    second = int(input('Enter the second number: '))

    print('The result is {}'.format(calculate(operation, first, second)))
    cont = input('Do you want to do another caluclation (y/n)? ')

print('Thanks for using me! See you soon!')

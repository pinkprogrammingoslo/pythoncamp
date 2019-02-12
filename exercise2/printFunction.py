def printStuff(name, town, skill):
    print('This is {} from {}, undefeated in {}'.format(name, town, skill))

run = 'y'
while run == 'y':
    name = input('What is your name? ')
    town = input('What is your home town? ')
    skill = input('What is your skill? ')

    printStuff(name, town, skill)

    run = input('Do you want to do do it again (y/n)? ')

my_file = open('text.txt', 'r+')

# A way to read the whole file at once: print(my_file.read())

# Print the line and the line number
for i, line in enumerate(my_file, 1):
    print('Line {} : {}'.format(i, line))

# \n is "new line" so it will write to a new line
my_file.write('\nHello from Python!')

my_file.close()

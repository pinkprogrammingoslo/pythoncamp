#
# Try it! From day 3
# Remember, most exercises can be solved in multiple ways

#
# Lists, loops and indices
#


# Count from 1 to 10
for x in range(11):
    print(x)

#################################
# Print dog names from list
dog_names = ['Kelvin', 'Ampere', 'Victor']
for name in dog_names:
    print('If I get a dog, I will call it ' + name)

#################################
#
# Get index of item in list (3 solutions)
#

list = [4, 7, 4, 3, 9]
num = 3

# Solution with loop
index = 1
for x in list:
    if num == x:
        print('Index: ' + str(index))
        break
    index = index + 1

# Solution with loop and build-in function enumerate()
for i, y in enumerate(list, 1):
    if num == y:
        print('Index: ' + str(i))
        break

# Solution with built-in function
list.index(num)

#################################

# Print all numbers from 5 to 1
counter = 5
while counter > 0:
    print('The count is: ', counter)
    counter = counter - 1

#
# Function
#

# Print list sorted and ascending
sort_list = [2, 6, 3, 0, 4, 13]
sort_list.sort()
print(sort_list)

# Print dog names comma separated
print(', '.join(dog_names))


# Convert dl to cups
def dl_to_cups(dl):
    return dl / 2.37


print('3 dl is {} cups'.format(dl_to_cups(3)))

# Calculator refactor - see exercise solution

#
# Try it! From day 4 Modules and files
# Remember, most exercises can be solved in multiple ways

# Roll the dice - see module roll_dice.py

# Animals, see modules dog.py, cat.py and animals.py

# Files, see file_test.py

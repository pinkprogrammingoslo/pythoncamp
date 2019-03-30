string = input("Please enter a string to find first unique letter in: ")

unique = False

for i, s in enumerate(string, 0):
    if string.count(s) == 1:
        print("The first unique letter is {} and has index {}".format(s, i))
        unique = True
        break

if not unique:
    print("No unique letter exists in {}".format(string))

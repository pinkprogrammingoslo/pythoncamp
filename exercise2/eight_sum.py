string = input("What numbers to you want to add? use a comma (,) to separate them. ")

# Replace is to remove all unwanted whitespaces
numbers = string.replace(" ", "").split(",")
result = 0
for num in map(int, numbers):
    result = result + num

print("The sum of the numbers {} is {}".format(numbers, result))

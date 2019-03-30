start = int(input("What is the starting number? \n"))
end = int(input("What is the last number? \n"))

numbers = [x for x in range(start, end + 1)]
print(', '.join(map(str, numbers)))

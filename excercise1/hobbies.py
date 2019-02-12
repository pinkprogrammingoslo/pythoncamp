question = 'What do you like to do? '

hobby = input(question)
hobbies = []

while hobby.lower() != 'stop':
    hobbies.append(hobby)
    hobby = input(question)

print('Okay, you like to ' + ', '.join(hobbies))

vowels = ['a', 'e', 'i' 'o', 'u', 'y', 'å', 'æ', 'ø', 'ö', 'ä']

string = input("What do you want word to translate? ").lower()

result = []

for s in string:
    if s in vowels:
        result.append(s)
    else:
        result.append(s)
        result.append('o')
        result.append(s)

print("".join(result))

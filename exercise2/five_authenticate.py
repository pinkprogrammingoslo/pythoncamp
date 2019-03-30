secret = {
    "userOne": "passOne",
    "userTwo": "passTwo",
    "userThree": "passOneThree",
    "userFour": "passFour"
}

print("Welcome to the authenticator")
username = input("Enter your username: ")
password = input("Enter your password: ")

if username in secret and secret[username] == password:
    print("Yeay you are authenticated!")
else:
    print("Oops, you are not authenticated! Try again")

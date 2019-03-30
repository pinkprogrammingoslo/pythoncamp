import random

min_num = 1
max_num = 6

roll_again = input("Roll the dices? (yes or no) \n")
while roll_again == "yes":
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min_num, max_num))
    print(random.randint(min_num, max_num))

    roll_again = input("Roll the dices again? (yes or no) \n")

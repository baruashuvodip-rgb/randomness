import random

dice_roll = []
add_dice = True

while(add_dice):

    number_of_sides = int(input("Enter number of sides: "))
    number_of_dice = int(input("how many dice do you want to roll? "))

    for i in range (0, number_of_dice):
        dice_roll.append(random.randint(1, number_of_sides))

    answer = input("Add more dice? y/n \n")

    if answer == 'n':
        add_dice = False
    elif answer != 'y':
        raise Exception("Invalid Input, answer with y or n")

total = 0

for roll in dice_roll:
    print(roll)
    total+=roll

print("The total rolled is", total)
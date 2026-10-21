import numpy as np

number_of_sides = int(input("Enter number of sides: "))
number_of_dice = int(input("how many dice do you want to roll? "))

dice_roll = np.random.randint(1, number_of_sides, number_of_dice)

print(dice_roll)
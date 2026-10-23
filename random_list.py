from class_random import LinearCongruential as LC

N = int(input("How many numbers do you want? "))

rng = LC()
numbers = rng.random(N)

if N==1:
    print(numbers)
else:
    for num in numbers:
        print(num, "\n")


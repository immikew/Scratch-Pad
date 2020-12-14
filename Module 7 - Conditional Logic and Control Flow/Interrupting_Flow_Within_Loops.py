import random

# roll = random.randint(1, 6)
# while True:
#     print(roll)
#     if roll == 4 or roll == 5:
#         break
#     roll = random.randint(1, 6)


# for i in range(1, 7):
#     if i == 4 or i == 5:
#         continue
#     print(i)


# fruits = 'apples cherries blueberries blackberries'.split()

# for fruit in fruits:
#     if 'peach' in fruit:
#         break
#     print(fruit)
# else:
#     print("peach wasn't found in the fruits")


max_guesses = 3
num_guess = 0
val_check = 'kronos'

while num_guess < max_guesses:
    val = input('Enter your guess: ')
    if val == val_check:
        print('You won!')
        break

    num_guess += 1
else:
    print('You lose :(')

print('Game over')
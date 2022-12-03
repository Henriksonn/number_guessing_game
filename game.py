import random
import time

computer_number = random.randint(1,100)
continue_game = True
user_guesses = []

start_time = time.time()
while(continue_game):
    user_guess= int(input('Guess a number between 1-100:'))
    user_guesses.append(user_guess)
    if user_guess == computer_number:
        print('Exactly! You guessed the number correctly.')
        continue_game = False
    elif user_guess < computer_number:
        print('Wrong. Guess a higher number.')
    elif user_guess > computer_number:
        print('Wrong.Guess a lower number.')
    else:
        print('There has been an error')

end_time = time.time()
print('Game Over.')

sum_of_differences = 0
for n in user_guesses:
   sum_of_differences += abs(n - computer_number)
print(f'Average difference {sum_of_differences/len(user_guesses)}')
print(f'You played for {end_time-start_time} seconds')

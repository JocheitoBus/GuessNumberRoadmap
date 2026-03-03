import random

newGame = True
print('Welcome to the Number Guessing Game!')
while newGame == True:
    print('I\'m thinking of a number between 1 and 100.\n')
    winNum = random.randint(1,100)

    print('Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n')
    difficult = input('Enter your choice: ')

    difficult = int(difficult) - 1
    difName = ['Easy','Medium','Hard']
    difAtempt = [10,5,3]
    print('Great! You have selected the',difName[difficult],'difficulty level.\nLet\'s start the game!\n')
    
    guess = -1
    attemptsLeft = difAtempt[difficult]
    while attemptsLeft > 0:
        attemptsLeft -= 1
        guess = input('Enter your guess: ')
        guess = int(guess)
        if guess == 0:
            print(winNum)
            continue
        if guess == winNum:
            print('Congratulations! You guessed the correct number in',difAtempt[difficult] - attemptsLeft,'attempts.\n')
            break
        else:
            print('Incorrect! The number is','greater' if winNum > guess else 'less','than',guess,'.\n')
    if guess != winNum:
        print('You lost!\n')
    newGame = True if input('Play again?\n1. Yes\n2. No\nEnter your choise: ') == '1' else False
    if newGame == True:
        print('\n\n')

                





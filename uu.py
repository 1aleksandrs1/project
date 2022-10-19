import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computer_Move = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computer_Move = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computer_Move = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computer_Move:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computer_Move == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computer_Move == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computer_Move == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computer_Move == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computer_Move == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computer_Move == 'r':
        print('You lose!')
        losses = losses + 1
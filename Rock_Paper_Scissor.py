import random


def to_get_winner(user_opt, comp_opt):
    if user_opt == comp_opt:
        return "It's a TIE."
    elif (user_opt == 'rock' and comp_opt == 'scissor') or \
            (user_opt == 'scissor' and comp_opt == 'paper') or \
            (user_opt == 'paper' and comp_opt == 'rock'):
        return 1

    return 0


def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n***ROCK-PAPER-SCISSORS***")
        print('1. ROCK')
        print('2. PAPER')
        print('3. SCISSOR')
        print('4. QUIT')

        try:
            user_input = int(input('Select option (1/2/3/4): '))
            if user_input not in [1, 2, 3, 4]:
                print("Invalid Choice. Enter 1 for ROCK, 2 for PAPER, 3 for SCISSOR, or 4 for QUIT.")
                continue
        except ValueError:
            print("Invalid input,Enter a valid input:")
            continue

        if user_input == 4:
            if user_score > computer_score:
                print("\nCongratulations!! You WON the game.")
            elif user_score < computer_score:
                print("\nYou LOST the game, Better Luck Next Time.")
            else:
                print("\nIt's a TIE. Play Again.")
            print("Thank you for  Playing!!\n")
            break

        options = ['rock', 'paper', 'scissor']
        user_opt = options[user_input - 1]
        comp_opt = random.choice(options)
        print(f"\nYour Choice: {user_opt}")
        print(f"Computer's Choice: {comp_opt}")

        result = to_get_winner(user_opt, comp_opt)
        print(result)

        if result:
            user_score += 1
        else:
            computer_score += 1
        print(f'Scores:\nYOU: {user_score}   COMPUTER: {computer_score}')


rock_paper_scissors_game()

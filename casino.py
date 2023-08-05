import random
import matplotlib.pyplot as plt


def spin_roulette():
    """
    Simulate spinning a roulette wheel. Returns the color that the ball lands on.
    """
    outcome = random.choices(
        population=['Red', 'Black', 'Green'],
        weights=[48.6, 48.6, 2.8],
        k=1
    )
    return outcome[0]

def play_game(money, bet_percentage):
    """
    Simulates a game where the player bets a percentage of their money on red every time,
    and also keeps track of the highest amount of money the player ever has, the total number
    of bets, and the bet number where the player had the highest amount of money.

    Arguments:
    money -- the initial amount of money the player has
    bet_percentage -- the percentage of their money that the player bets each time

    Returns: None
    """
    money_history = [money]  # Start with the initial amount of money
    starting_money_amount = money
    highest_money = money
    highest_money_bet_number = 0
    total_bets = 0

    while money > 1:
        money_history.append(money)  # Save the money after each bet
        total_bets += 1
        bet = money * (bet_percentage / 100)
        print(f"Bet number {total_bets}: The player bets {bet} on Red.")
        money -= bet

        outcome = spin_roulette()
        print(f"The ball landed on {outcome}.")

        if outcome == 'Red':
            print("The player wins!")
            money += bet * 2
            if money > highest_money:
                highest_money = money
                highest_money_bet_number = total_bets
        else:
            print("The player loses.")
        print(money)     

    print("The game is over.")
    print(f"the player started with {starting_money_amount}")
    print(f"at percentege {bet_percentage}")
    print(f"The player made a total of {total_bets} bets.")
    print(f"The highest amount of money the player had was {highest_money}.")
    print(f"This occurred on bet number {highest_money_bet_number}.")
        # Plotting the graph
    plt.plot(money_history)
    plt.xlabel('Bet Number')
    plt.ylabel('Money Amount')
    plt.title(f'Player Money Over Time Starting With {starting_money_amount} with bet perc of {bet_percentage} ')
    # Save the plot
    filename = f"player_money_{starting_money_amount}_{bet_percentage}.png"
    plt.savefig(filename)

def roulette_terminal():
    while True:
        money = float(input("Enter the initial amount of money you have: "))
        bet_percentage = float(input("Enter the percentage of money you want to bet each time: "))
        play_game(money, bet_percentage)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
roulette_terminal()
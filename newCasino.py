import random
import matplotlib.pyplot as plt
import numpy as np

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
def play_game_with_exit(money, bet_percentage, max_bets, target_profit_percentage,stop_loss_percentage):
    total_bets = 0
    starting_money = money
    target_profit = starting_money * (1 + target_profit_percentage / 100)
    stop_loss = starting_money * (stop_loss_percentage / 100)


    while money > 1 and total_bets < max_bets and money < target_profit and money > stop_loss:
        total_bets += 1
        bet = money * (bet_percentage / 100)
        money -= bet

        outcome = spin_roulette()
        if outcome == 'Red':
            money += bet * 2

    return money
def roulette_simulation():
    while True:
        money = int(input("Enter the initial amount of money you have: "))
        bet_percentage = int(input("Enter the percentage of money you want to bet each time: "))
        max_bets = int(input("Enter the maximum number of bets (exit after X bets): "))
        target_profit_percentage = int(input("Enter the target profit percentage (exit after X% profit): "))
        amount_of_plays = int(input("Enter the amount of times you want to run this sim: "))
        stop_loss_percentage = int(input("Enter the percentege of stop loss (for example if stoploss = 20 than it will exit the sim at 20perc of your starting money): "))

        final_money = []
        for _ in range(amount_of_plays):
            money_left = play_game_with_exit(money, bet_percentage, max_bets, target_profit_percentage,stop_loss_percentage)
            final_money.append(money_left)

        average_money_left = np.mean(final_money)
        print(f"Average money left after {amount_of_plays} simulations: {average_money_left}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

roulette_simulation()
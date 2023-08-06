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

def play_game(money, bet_percentage,games):
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
    return highest_money,highest_money_bet_number

def roulette_terminal():
    while True:
        money = int(input("Enter the initial amount of money you have: "))
        bet_percentage = int(input("Enter the percentage of money you want to bet each time: "))
        amount_of_plays = int(input("Enter the amount of times you want to run this sim: "))
        highest_money = []
        highest_money_bet_numbers = []
        for game in range(amount_of_plays):
            highest_money_value, highes_money_bet = play_game(money, bet_percentage, game)
            highest_money.append(highest_money_value)
            highest_money_bet_numbers.append(highes_money_bet)
        
        amount_of_plays_without_profit = 0
        amount_of_plays_with_atleast_10_profit = 0
        amount_of_plays_with_atleast_20_profit = 0
        amount_of_plays_with_atleast_30_profit = 0
        amount_of_plays_with_atleast_40_profit = 0
        amount_of_plays_with_atleast_50_profit = 0
        amount_of_plays_with_atleast_60_profit = 0
        amount_of_plays_with_atleast_70_profit = 0
        amount_of_plays_with_atleast_80_profit = 0
        amount_of_plays_with_atleast_90_profit = 0
        amount_of_plays_with_atleast_100_profit = 0
        for index, money_in_game in enumerate(highest_money):
            if money == highest_money[index]:
                amount_of_plays_without_profit += 1
            if money*1.10 < highest_money[index]:
                amount_of_plays_with_atleast_10_profit += 1 
            if money*1.20 < highest_money[index]:
                amount_of_plays_with_atleast_20_profit += 1
            if money*1.30 < highest_money[index]:
                amount_of_plays_with_atleast_30_profit += 1
            if money*1.40 < highest_money[index]:
                amount_of_plays_with_atleast_40_profit += 1
            if money*1.50 < highest_money[index]:
                amount_of_plays_with_atleast_50_profit += 1
            if money*1.60 < highest_money[index]:
                amount_of_plays_with_atleast_60_profit += 1
            if money*1.70 < highest_money[index]:
                amount_of_plays_with_atleast_70_profit += 1
            if money*1.80 < highest_money[index]:
                amount_of_plays_with_atleast_80_profit += 1
            if money*1.90 < highest_money[index]:
                amount_of_plays_with_atleast_90_profit += 1
            if money*2 < highest_money[index]:
                amount_of_plays_with_atleast_100_profit += 1                                  
        highest_money_average = np.mean(highest_money)
        highest_bet_num_average = np.mean(highest_money_bet_numbers)           
        print(f"amount of plays without profit: {amount_of_plays_without_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 10% profit: {amount_of_plays_with_atleast_10_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 20% profit: {amount_of_plays_with_atleast_20_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 30% profit: {amount_of_plays_with_atleast_30_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 40% profit: {amount_of_plays_with_atleast_40_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 50% profit: {amount_of_plays_with_atleast_50_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 60% profit: {amount_of_plays_with_atleast_60_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 70% profit: {amount_of_plays_with_atleast_70_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 80% profit: {amount_of_plays_with_atleast_80_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 90% profit: {amount_of_plays_with_atleast_90_profit}/{amount_of_plays}")
        print(f"amount of plays without atleast 100% profit: {amount_of_plays_with_atleast_100_profit}/{amount_of_plays}")
        print(f'highest winning avg = {highest_money_average}')
        print(f'avg bet for highest value avg= {highest_bet_num_average}')
        plt.plot(highest_money)
        plt.xlabel('Game Number')
        plt.ylabel('Highest Profit')
        plt.title('Payouts')
        # Save the plot
        filename = f"test with {amount_of_plays}"
        plt.savefig(filename)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
roulette_terminal()
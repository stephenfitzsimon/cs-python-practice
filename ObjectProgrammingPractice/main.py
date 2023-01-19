from player import Player
from highestRoll import HighestRoll
def main():
    
    print("Welcome to the casino! Here we play the highest roll\n")
    name = input("Introduce yourself! What's your name? ")
    player = Player(name)
    print(f"Welcome {player.name}! Let's play!")
    while True:
        print()
        print(player)
        game = HighestRoll()
        print(game)
        bet = player.bet_money()
        game.make_bet(player_bet = bet)
        game.player_roll_die()
        player.add_winnings(game.determine_winner())
        continue_play = input("Would you like to stop playing? Press y to stop, any to continue: ")
        if continue_play == 'y' or player.wallet <= 0:
            print("Thanks for playing! Final player stats")
            print(player)
            break




if __name__ == '__main__':
    main()
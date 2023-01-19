from random import randint

class HighestRoll:

    def __init__(self):
        self.playerroll = None
        self.houseroll = randint(1,6)
        self.bet = None

    def __repr__(self):
        return "This game takes a bet by the player and if the player rolls\na die that is higher than the house, they win their bet x2 \notherwise they lose their bet. In case of a tie, the bet is returned."

    def make_bet(self, player_bet):
        self.bet = player_bet

    def player_roll_die(self):
        while (True):
            draw = input("Press y to roll: ")
            if draw == 'y':
                self.playerroll = randint(1,6)
                break
    
    def determine_winner(self):
        print(f"Player: {self.playerroll}")
        print(f"House: {self.houseroll}")
        if self.playerroll == self.houseroll:
            print("It's a tie! return bet")
            return self.bet
        elif self.playerroll > self.houseroll:
            print(f"Player won! return ${self.bet*2}")
            return self.bet*2
        elif self.playerroll < self.houseroll:
            print(f"House won! You lose ${self.bet}!")
            return -1*self.bet
        else:
            print("something went wrong")
            return -1
    
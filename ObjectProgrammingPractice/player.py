class Player:

    def __init__(self, name):
        self.name = name
        self.wallet = 1000
        self.outcomes = []
        self.total_games_played = 0

    def __repr__(self) -> str:
        return f"{self.name} has ${self.wallet} in their wallet. Their win rate is: {self.calculate_win_rate()}."

    def bet_money(self):
        while (True):
            bet = int(input("Please enter a bet: "))
            if bet <= self.wallet and bet > 0:
                self.wallet -= bet
                return bet
            else:
                print(f"You only have ${self.wallet}!")

    def add_winnings(self, winnings):
        self.wallet = winnings + self.wallet
        self.total_games_played += 1
        if winnings <= 0:
            self.outcomes.append(False)
        else:
            self.outcomes.append(True)

    def calculate_win_rate(self):
        if self.total_games_played != 0:
            return sum(self.outcomes)/self.total_games_played
        else:
            return "No games played yet!"
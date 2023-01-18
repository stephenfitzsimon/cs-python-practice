class Player:

    def __init__(self, name):
        self.name = name
        self.wallet = 1000
        self.outcomes = []
        self.total_games_played = 0

    def __repr__(self) -> str:
        return f"{self.name} has ${self.wallet} in their wallet. Their win rate is: {self.calculate_win_rate()}."

    def bet_money(self, bet):
        self.wallet -= bet

    def add_winnings(self, winnings):
        self.wallet += winnings

    def calculate_win_rate(self):
        if self.total_games_played != 0:
            return sum(self.outcomes)/self.total_games_played
        else:
            return None
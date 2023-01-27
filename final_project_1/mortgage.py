class Mortgage:

    def __init__(self, interest_rate, term, principal, label = None):
        self.interest_rate = interest_rate/12
        self.term = term
        self.principal = principal
        self.label = label

    def __repr__(self, acc = 2):
        if self.label is not None:
            return f"Martgage {self.label} has a monthly payment of ${round(self.calculate_monthy_payment(), acc)}"

    def calculate_monthy_payment(self):
        if self.interest_rate == 0:
            return self.principal / self.term
        else:
            top = (self.interest_rate*self.principal*(1+self.interest_rate)**self.term)
            bottom = ((1+self.interest_rate)**self.term-1)
            return top/bottom
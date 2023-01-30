from mortgage import Mortgage

def main():
    mortgage_lst = []
    while True:
        print_menu()
        user_in = int(input("Enter a selection >"))
        if user_in == 3:
            break
        elif user_in == 1 :
            mortgage = make_mortgage()
            mortgage_lst.append(mortgage)
        elif user_in == 2:
            print_mortgages(mortgage_lst)

def print_menu():
    menu = '''
    This is the Mortgage calculator

    Choose one of the following options:
    1 - Enter new mortgage
    2 - Compare entered mortgages
    3 - Exit
    '''
    print(menu)

def make_mortgage():
    interest = float(input("Enter interest rate as a float >"))
    term = int(input("Enter term in months >"))
    prinicpal = float(input("Enter mortgage principal >"))
    name = input("Enter a label for the mortgage >")
    return Mortgage(interest, term, prinicpal, name)

def print_mortgages(lst):
    for m in lst:
        print(m)

if __name__ == '__main__':
    main()
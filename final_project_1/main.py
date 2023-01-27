from mortgage import Mortgage

def main():
    while True:
        print_menu()
        user_in = int(input("Enter a selection >"))
        if user_in == 3:
            break

def print_menu():
    menu = '''
    This is the Mortgage calculator

    Choose one of the following options:
    1 - Enter new mortgage
    2 - Compare entered mortgages
    3 - Exit
    '''
    print(menu)

if __name__ == '__main__':
    main()
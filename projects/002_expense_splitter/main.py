
# 1. Create the function
def calculate_split(total_amount: float, number_of_people: int, currency: str,share_data:list = []) -> None:
    # 2. Validate the amount of people
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than one.')
    if len(share_data) != number_of_people:
        print('Something went wrong while splitting by share...\nSplitting even Now...\n')
        share_data = [100/number_of_people for _ in range(number_of_people)]
    # 3. Perform the calculation
    # share_per_person: float = total_amount / number_of_people

    # 4. Format the results and display them
    print(f'Total expense: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')
    # print(f'Each person should pay: {currency}{share_per_person:,.2f}')
    for i in range(number_of_people):
        print(f'Share of person {i}: {currency}{total_amount*share_data[i]/100:,.2f}')
        



# 5. Create a main entry point
def main() -> None:
    # 6. Try to get the user input and perform the calculation
    try:
        total_amount: float = float_input('Enter the total amount of the expense: ')
        number_of_people: int = int(input('Enter the number of people sharing the expense: '))
        share_data:list = list()
        choice:str = input('Wanna add Expenses ? (Y\\N) ')
        if choice.lower() == 'y' or choice.lower() == 'yes':
            while True:
                share_data:list = list()
                for _ in range(number_of_people):
                    share_data.append(float_input('Enter share : '))
                if sum(share_data) == 100:
                    break
                else:
                    print('Please re-enter share data or press Enter to Continue without share... \n')
                    share_data = []

        # Call the function to calculate and display expenses
        calculate_split(total_amount, number_of_people, currency='€',share_data=share_data)

    except ValueError as e:
        print(f'Error: {e}')

def float_input(*argv) ->float :
    while(True):
        try:
            opr = float(input(argv[0]))
            break
            
        except:
            print('Invalid input')
    
    return opr

# 7. Run the script
if __name__ == '__main__':
    main()


"""
Homework:
1. Edit the script to give the user the option to enter uneven splits, such as 20%, 40%, 40%.
2. Make it so that if the user encounters an error, the program nicely asks them to try again with
a proper value.

"""
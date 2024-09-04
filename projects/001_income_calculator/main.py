# 1. Create a function to calculate finances
def calculate_finances(monthly_income: float, tax_rate: float, currency: str,other_expenses: tuple = ()) -> None:
    # 2. Do the math for each field
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    print(other_expenses)
    monthly_expenses: float = sum(other_expenses)
    monthly_balance: float = monthly_net_income-monthly_expenses
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    yearly_expenses: float = monthly_expenses*12
    yearly_balance: float = yearly_net_income-yearly_expenses

    # 3. Format the information nicely for the user
    print('--------------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Monthly expenses: {currency}{monthly_expenses:,.2f}')
    print(f'Monthly balance: {currency}{monthly_balance:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print(f'Yearly expenses: {currency}{yearly_expenses:,.2f}')
    print(f'Yearly balance: {currency}{yearly_balance:,.2f}')
    print('--------------------------------')


# 4. Create a main entry point for the program
def main() -> None:
    # 5. Gather user input
    # monthly_income: float = float(input('Enter your monthly income: '))
    # tax_rate: float = float(input('Enter your tax rate (%): '))
    monthly_income: float = float_input('Enter your monthly income: ')
    tax_rate: float = float_input('Enter your tax rate (%): ')
    other_expenses: dict = dict()
    choice:str = input('Wanna add Expenses ? (Y\\N) ')
    if choice.lower() == 'y' or choice.lower() == 'yes':
        while(True):
            expense_type:str = input('Enter the expense type or Enter to Finish...\n')
            if len(expense_type) != 0:
                expense = float_input('Enter expense per month : ')
                other_expenses[expense_type] = expense
                expense_type = ''
            else:
                break
        

    # 6. Call the function
    calculate_finances(monthly_income, tax_rate, currency='KR',other_expenses=other_expenses.values())

def float_input(*argv) ->float :
    while(True):
        try:
            opr = float(input(argv[0]))
            break
            
        except:
            print('Invalid input')
    
    return opr

# 7. Run the script
if __name__ == "__main__":
    main()

"""
Homework:
DONE:1. Edit the script so that users can also enter their expenses (eg. rent, food, gym memberships) so they
can see how much they have left over each month.
DONE:2. Recreate the user input section to safely handle users inserting the wrong type without 
crashing the program.

"""

# 1. Import necessary functionality
import json
import requests
from requests import Response, RequestException


# 2. Load the rates from a JSON file
def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)


# 3. Create the function
def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    # 4. Make sure the user input is lowered
    base = base.lower()
    to = to.lower()

    # 5. Get the dictionaries
    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to) 

    # 6. Return the rates
    if from_rates is not None and to_rates is not None:
        return amount * (to_rates['rate'] / from_rates['rate'])  
    else:
        try:

            if base == 'eur' and from_rates is None:
                return amount * to_rates['rate']  
            elif to == 'eur' and to_rates is None:
                return amount * from_rates['inverseRate']  
            else:
                display_error()
                return 0
        except TypeError as e:
            display_error()
            return 0
'''HOMEWORK-3 Conversion using API'''

#function to call API and collect rates
def get_rate(base : str ) -> dict[str,float] :
    try:
        response : Response = requests.get(f'https://open.er-api.com/v6/latest/{base.upper()}')
        content = json.loads(response.content)
        return content['rates']
    except RequestException as exp:
        print(f'ERROR : {exp}')
        return None
    

#function to convert from web conversion rates

def convert_online(amount: float, base: str, to: str) -> float: 
    rates: dict[str,float] = get_rate(base)
    if rates is not None:
        try:
            return amount * rates[to.upper()]
        except KeyError:
            print(f'Conversion {base.upper()} -> {to.upper()} cannot be finished...')
            return 0      

def display_error() ->None:
            rates: dict[str, dict] = load_rates('projects/006_currency_converter/rates.json')
            for rate in rates:
                print(f'{rates[rate]['name']} - {rates[rate]['alphaCode']}')
            print('\n\nERROR : Inalid currency...\nAvailable currencies are listed above')

# 7. Create a main entry point
def main() -> None:
    # 8. Load the rates
    rates: dict[str, dict] = load_rates('projects/006_currency_converter/rates.json')

    # 9. Get the result
    amount: float = float(input('Enter the amount to be converted\n'))
    base:str =(input('Enter the amount to be converted\n'))
    to:str =(input('Enter the amount to be converted\n'))

    result: float = convert(amount=amount, base = base,to = to,rates=rates)
    print(f'{result:,.2f}' if result is not None else 'ERR')
    print('Online Conversion')
    result = convert_online(amount=amount, base = base,to = to)
    print(f'{result:,.2f}')


# 10. Run the script
if __name__ == '__main__':
    main()

"""
Homework:
1. Right now it works fine if you insert a rate that exists, but make it so that if the user
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options.
2. Edit the script so that the "to" currency can also be specified as euro. 
3. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API. 
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script. 

"""

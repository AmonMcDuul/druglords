import PySimpleGUI as sg
import random


def get_data():
    data = []
    drug_data = list(map(list, drugs.items()))
    for drug in drug_data:
        data.append([drug[0], drug[1]['Price'], drug[1]['Owned']])
    return data


def price_random():
    for drug in drugs:
        if price_very_high():
            percentage = 1 + (random.randint(50, 100) / 100)
            sg.cprint(drug + ' price is very high!')
        elif price_very_low():
            percentage = 1 - (random.randint(25, 75) / 100)
            sg.cprint(drug + ' price is very low!')
        else:
            percentage = 1 + (random.randint(-25, 25) / 100)
        drugs[drug]['Price'] = int(origdrugs[drug]['Price'] * percentage)
    return get_data()


def price_very_high():
    if random.randint(1, 20) == 1:
        return True
    return False


def price_very_low():
    if random.randint(1, 20) == 1:
        return True
    return False


def owned():
    result = 0
    for i in get_data():
        result += i[2]
    return result


# drug stats
def owned_update(string, drug, amount):
    if string == 'buy':
        drugs[drug]['Owned'] += amount
    elif string == 'sell':
        drugs[drug]['Owned'] -= amount
    return get_data()


    # drug stats
drugs = {'Weed': {'Price': 50, 'Owned': 0}, 'Hash': {
    'Price': 150, 'Owned': 0}, 'Heroin': {'Price': 250, 'Owned': 0}}
origdrugs = {'Weed': {'Price': 50, 'Owned': 0}, 'Hash': {
    'Price': 150, 'Owned': 0}, 'Heroin': {'Price': 250, 'Owned': 0}}
headings = ['Drug', 'Price', 'Owned']
data = get_data()

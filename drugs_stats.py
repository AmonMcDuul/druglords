import random


def get_data(dicts):
    data = []
    drug_data = list(map(list, drugs.items()))
    for drug in drug_data:
        data.append([drug[0], drug[1]['Price'], drug[1]['Owned']])
    return data


def price_random():
    for drug in drugs:
        percentage = random.randint(-10, 10) / 100
        drugs[drug]['Price'] = int(drugs[drug]['Price'] * (1 + percentage))
    return get_data(drugs)


def owned():
    result = 0
    for i in get_data(drugs):
        result += i[2]
    return(str(result) + ' / 100')


# drug stats
def owned_update(string, drug, amount):
    if string == 'buy':
        drugs[drug]['Owned'] += amount
    elif string == 'sell':
        drugs[drug]['Owned'] -= amount
    return get_data(drugs)

    # drug stats
drugs = {'Weed': {'Price': 50, 'Owned': 0}, 'Hash': {
    'Price': 150, 'Owned': 0}, 'Heroin': {'Price': 250, 'Owned': 0}}
headings = ['Drug', 'Price', 'Owned']
data = get_data(drugs)

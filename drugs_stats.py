import random

# available drugs
drugs = {'Weed': 50, 'Hash': 100, 'Heroin': 250}
headings = ['Drug', 'Price']
data = list(map(list, drugs.items()))


def price_random():
    for drug in drugs:
        percentage = random.randint(-10, 10) / 100
        drugs[drug] = int(drugs[drug] * (1 + percentage))
    data = list(map(list, drugs.items()))
    return data

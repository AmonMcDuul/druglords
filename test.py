def get_data(dict):
    data = []
    drug_data = list(map(list, drugs.items()))
    for drug in drug_data:
        data.append([drug[0], drug[1]['Price'], drug[1]['Owned']])
    return data


def owned():
    result = 0
    for i in data:
        result += i[2]
    return(result)


    # drug stats
drugs = {'Weed': {'Price': 50, 'Owned': 0}, 'Hash': {
    'Price': 150, 'Owned': 0}, 'Heroin': {'Price': 250, 'Owned': 0}}
headings = ['Drug', 'Price', 'Owned']
data = get_data(drugs)

import drugs_stats as ds
from main import balance


def update_balance(string, drug, amount):
    global balance
    data = ds.get_data()
    for d in data:
        if d[0] == drug:
            if string == 'buy':
                balance -= d[1] * amount
            elif string == 'sell':
                balance += d[1] * amount
    return balance


def get_balance():
    return balance


def balance_colour():
    if balance >= 0:
        color = 'green'
    else:
        color = 'red'
    return color

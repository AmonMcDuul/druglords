import drugs_stats as ds
from main import balance, loan, interest_loan


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


def update_balance_shop(amount):
    global balance
    balance = balance - amount
    return


def get_balance():
    global balance
    global loan
    result = balance + loan
    return result


def balance_colour():
    if balance >= 0:
        color = 'green'
    else:
        color = 'red'
    return color


def shop_price_colour(amount):
    if balance - amount >= 0:
        color = 'green'
    else:
        color = 'red'
    return color


def set_loan(new_loan):
    global loan
    loan = new_loan
    return


def get_loan():
    global loan
    return loan


def set_interest_loan(int_loan):
    global interest_loan
    interest_loan = int_loan
    return


def get_interest_loan():
    global interest_loan
    return interest_loan


def loan_interest():
    global interest_loan
    new_loan = interest_loan + (interest_loan*0.015)
    result = "{:.2f}".format(new_loan)
    interest_loan = float(result)
    return


def pay_loan():
    x = get_balance()
    y = get_interest_loan()
    r = x-y
    if r > 0:
        update_balance_shop(y)
        set_interest_loan(0)
        return True
    else:
        return False

import PySimpleGUI as sg
import drugs_stats as ds
import bank_account as ba


def max_to_buy(drug):
    r = ds.get_data()
    for i in r:
        if i[0] == drug:
            return (int(ba.get_balance()/i[1]))


def buy_view(drug):
    maxi = max_to_buy(drug)
    layout = [[sg.Text('Buy screen yoyo')],
              [sg.Slider(key='-NUM-',
                         range=(0, maxi),
                         default_value=0,
                         size=(20, 15),
                         orientation='horizontal',
                         font=('Helvetica', 12))],
              [sg.Button('Buy')]]
    buy_window = sg.Window('Buy', layout)

    while True:
        event, values = buy_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Buy':
            # sg.cprint(drug, int(values['-NUM-']))
            ds.owned_update('buy', drug, int(values['-NUM-']))
            ba.update_balance('buy', drug, int(values['-NUM-']))
            break
    buy_window.close()


def sell_view(drug, maxi):
    layout = [[sg.Text('Sell screen yoyo')],
              [sg.Slider(key='-NUM-',
                         range=(1, maxi),
                         default_value=0,
                         size=(20, 15),
                         orientation='horizontal',
                         font=('Helvetica', 12))],
              [sg.Button('Sell')]]
    sell_window = sg.Window('Buy', layout)

    while True:
        event, values = sell_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Sell':
            # sg.cprint(drug, int(values['-NUM-']))
            ds.owned_update('sell', drug, int(values['-NUM-']))
            ba.update_balance('sell', drug, int(values['-NUM-']))
            break
    sell_window.close()

import PySimpleGUI as sg
import drugs_stats as ds


def buy_view(drug):
    layout = [[sg.Text('Buy screen yoyo')],
              [sg.Slider(key='-NUM-',
                         range=(1, 100),
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
            sg.cprint(drug, int(values['-NUM-']))
            ds.owned_update('buy', drug, int(values['-NUM-']))
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
            sg.cprint(drug, int(values['-NUM-']))
            ds.owned_update('sell', drug, int(values['-NUM-']))
            break
    sell_window.close()

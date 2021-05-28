import PySimpleGUI as sg
import drugs_stats as ds

drugs = {'wiet': 50, 'hash': 100, 'subbranch': 200}
BAR_MAX = 10
i = 0

# drug price changer


def change_drug_price(price):
    return price+10


# Table data
data = [['Weed', '50'], ['Hash', '100'], ['Boobs', '200']]
headings = ['Drug', 'Price']

top_layout = [[sg.Button('Shop', key='-SHOP-'), sg.Button('Poopie',
                                                          key='-NONE-'), sg.Button('Poops', key='-NONE-')]]

left_layout = [[sg.Table(values=ds.data, headings=ds.headings,
                         auto_size_columns=False,
                         col_widths=[20, 10],
                         justification='left',
                         num_rows=6,
                         key='-TABLE-',
                         row_height=20,
                         hide_vertical_scroll=True,
                         enable_events=True)],
               [sg.Button('Buy', key='-BUY-')]]

right_layout = [[sg.Text('Bugaloo')],
                [sg.MLine(key='-ML-', size=(40, 8))],
                [sg.Text('Progress')],
                [sg.ProgressBar(BAR_MAX, orientation='h',
                                size=(20, 20), key='-PROG-')],
                [sg.Button('Next day', key='-NEXTDAY-')]]


combined_layout = [sg.vtop([sg.Col(top_layout, element_justification='l')]),
                   [sg.Column(left_layout), sg.Column(right_layout)],
                   [sg.OK()]]


window = sg.Window('Druglordzz', combined_layout)
sg.cprint_set_output_destination(window, '-ML-')


def buy_view(drug):
    layout = [[sg.Text('Buy screen yoyo')]]
    buy_window = sg.Window('Buy', layout)

    while True:
        event, values = buy_window.read()
        if event == sg.WIN_CLOSED:
            break
    buy_window.close()


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values['-TABLE-']:
        sg.cprint(ds.data[int(values['-TABLE-'][0])][0])
    if event == '-NEXTDAY-':
        i += 1
        window['-PROG-'].update(i)
    if event == '-BUY-' and len(values['-TABLE-']) == 1:
        buy_view()

window.close()

import PySimpleGUI as sg
import drugs_stats as ds

sg.theme('DarkGrey9')

BAR_MAX = 10
progress = 0


def change_drug_price(price):
    return price+10


character_layout = [[sg.Image('poppetje.png'), sg.Text(
    'Textje'), sg.Text('Textje'), sg.Text('Textje')]]

submenu_layout = [[sg.Button('Shop', key='-SHOP-'), sg.Button('Poopie',
                                                              key='-NONE-'), sg.Button('Poops', key='-NONE-')]]


left_layout = [[sg.Text('Drugaloo')],
               [sg.Table(values=ds.data, headings=ds.headings,
                         auto_size_columns=False,
                         col_widths=[20, 10],
                         justification='left',
                         num_rows=max(6, len(ds.data)),
                         key='-TABLE-',
                         row_height=20,
                         hide_vertical_scroll=bool(max(6, len(ds.data)) <= 6),
                         enable_events=True)],
               [sg.Button('Buy', key='-BUY-')]]


right_layout = [[sg.Text('Bugaloo')],
                [sg.MLine(key='-ML-', size=(40, 8))],
                [sg.Text('Progress')],
                [sg.ProgressBar(BAR_MAX, orientation='h',
                                size=(20, 20), key='-PROG-')],
                [sg.Button('Next day', key='-NEXTDAY-')]]


combined_layout = [sg.vtop([sg.Col(character_layout, element_justification='l')]),
                   sg.vtop([sg.Col(submenu_layout, element_justification='l')]),
                   [sg.Column(left_layout), sg.Column(right_layout)],
                   [sg.OK()]]


window = sg.Window('Druglordzz', combined_layout)
sg.cprint_set_output_destination(window, '-ML-')

################
# # BUY VIEW


def buy_view(drug):
    layout = [[sg.Text('Buy screen yoyo')],
              [sg.Slider(range=(1, 100),
                         default_value=0,
                         size=(20, 15),
                         orientation='horizontal',
                         font=('Helvetica', 12))],
              [sg.Button('Buy'), sg.Button('Sell')]]
    buy_window = sg.Window('Buy', layout)

    while True:
        event, values = buy_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == sg.WIN_CLOSED:
            break
    buy_window.close()

###################


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values['-TABLE-']:
        sg.cprint(ds.data[int(values['-TABLE-'][0])][0])
    if event == '-NEXTDAY-':
        window['-TABLE-'].update(values=ds.price_random())
        progress += 1
        window['-PROG-'].update(progress)
    if event == '-BUY-' and len(values['-TABLE-']) == 1:
        buy_view(ds.data[int(values['-TABLE-'][0])][0])

window.close()

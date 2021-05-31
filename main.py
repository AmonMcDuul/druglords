import PySimpleGUI as sg
import drugs_stats as ds
import trading as tr
import bank_account as ba

sg.theme('DarkGrey9')

BAR_MAX = 10
progress = 0
balance = 10000


def main_screen():
    character_layout = [[sg.Image('poppetje.png')]]

    character_stats = [[sg.Text('Name: ', size=(7, 1)), sg.Text('Piemeltje')],
                       [sg.Text('Age: ', size=(7, 1)), sg.Text('12')],
                       [sg.Text('Inventory: ', size=(7, 1)), sg.Text(
                           ds.owned(), size=(10, 1), key='-INV-')],
                       [sg.Text('BankAccount!: ', size=(10, 1)), sg.Text(balance, text_color=ba.balance_colour(), key='-BALANCE-')]]

    character_items = [[sg.Text('Weapon: ', size=(7, 1)), sg.Text('Vuisten')],
                       [sg.Text('Armor: ', size=(7, 1)),
                        sg.Text('Bodywarmer')],
                       [sg.Text('Dinges: ', size=(7, 1)), sg.Text('Danges')],
                       [sg.Text('')]]

    submenu_layout = [
        [sg.Button('Shop'), sg.Button('Poopie'), sg.Button('Poops')]]

    left_layout = [[sg.Text('Drugaloo')],
                   [sg.Table(values=ds.data, headings=ds.headings,
                             auto_size_columns=False,
                             col_widths=[20, 10, 6],
                             justification='left',
                             num_rows=max(6, len(ds.data)),
                             key='-TABLE-',
                             row_height=20,
                             hide_vertical_scroll=bool(
                                 max(6, len(ds.data)) <= 6),
                             enable_events=True)],
                   [sg.Button('Buy'), sg.Button('Sell')]]

    right_layout = [[sg.Text('Bugaloo')],
                    [sg.MLine(key='-ML-', size=(40, 8))],
                    [sg.Text('Progress')],
                    [sg.ProgressBar(BAR_MAX, orientation='h',
                                    size=(20, 20), key='-PROG-')],
                    [sg.Button('Next day', key='-NEXTDAY-')]]

    combined_layout = [[sg.Col(character_layout), sg.Col(character_stats), sg.Col(character_items)],
                       sg.vtop(
                           [sg.Col(submenu_layout, element_justification='l')]),
                       [sg.Col(left_layout), sg.Col(right_layout)]]

    window = sg.Window('Druglordzz', combined_layout)
    sg.cprint_set_output_destination(window, '-ML-')
    return window


def main():
    global progress
    window = main_screen()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if values['-TABLE-']:
            sg.cprint(
                'Trade ' + str(ds.data[int(values['-TABLE-'][0])][0]) +
                ' for $' + str(ds.data[int(values['-TABLE-'][0])][1]) + '?')
        if event == '-NEXTDAY-':
            window['-TABLE-'].update(values=ds.price_random())
            progress += 1
            if progress > 10:
                progress = 0
                sg.popup('Game endend. You have earned: ', ba.get_balance())
            window['-PROG-'].update(progress)
        if event == 'Buy' and len(values['-TABLE-']) == 1:
            tr.buy_view(ds.data[int(values['-TABLE-'][0])][0])
            window['-TABLE-'].update(values=ds.get_data())
            window['-INV-'].update(ds.owned())
            window['-BALANCE-'].update(ba.get_balance(),
                                       text_color=ba.balance_colour())

            sg.cprint(
                'You bought ' + str(ds.data[int(values['-TABLE-'][0])][0]))
        if event == 'Sell' and len(values['-TABLE-']) == 1:
            tr.sell_view(ds.data[int(values['-TABLE-'][0])][0],
                         ds.drugs[ds.data[int(values['-TABLE-'][0])][0]]['Owned'])
            window['-TABLE-'].update(values=ds.get_data())
            window['-INV-'].update(ds.owned())
            window['-BALANCE-'].update(ba.get_balance(),
                                       text_color=ba.balance_colour())

            sg.cprint(
                'You sold ' + str(ds.data[int(values['-TABLE-'][0])][0]))
        if event == 'Poops':
            sg.cprint('Fartypoops')

    window.close()


if __name__ == '__main__':
    main()

import PySimpleGUI as sg
import drugs_stats as ds
import trading as tr
import bank_account as ba
import shop as sh
import character as ch
import character_selection as cs
import loans as lo
import events as ev
import tictactoe as tt
import word_battle as wb
import database as db
import loading_game as lg
import end_game as eg
from pong_game.pong import run_game
from invader_game.alien_invasion import run_alien

# from pygame import mixer
# mixer.init()
# mixer.music.load('song.mp3')
# mixer.music.play()

sg.theme('DarkGrey9')

progress = 0
balance = 100
loan = 5000
interest_loan = 0


def main_screen(name, age, pic, days):

    character_layout = [[sg.Image(pic, key='-PROFILE_PIC-')]]

    character_stats = [[sg.Text('Name: ', size=(7, 1)), sg.Text(name, key='-NAME-')],
                       [sg.Text('Age: ', size=(7, 1)),
                        sg.Text(age, key='-AGE-')],
                       [sg.Text('Inventory: ', size=(7, 1)), sg.Text(
                           ds.owned(), size=(10, 1), key='-INV-')],
                       [sg.Text('BankAccount!: ', size=(10, 1)), sg.Text(
                           ba.get_balance(), text_color=ba.balance_colour(), key='-BALANCE-')],
                       [sg.Text('Health')], [sg.ProgressBar(max_value=ch.get_health(), orientation='h',
                                                            size=(20, 20), key='-HEALTH-', bar_color=('Red', 'White'))]]

    character_items = [[sg.Text('Weapon: ', size=(7, 1)), sg.Text(ch.get_weapon(), key='-WEAP-')],
                       [sg.Text('Armor: ', size=(7, 1)),
                        sg.Text(ch.get_armor(), size=(15, 1), key='-ARM-')],
                       [sg.Text('Dinges: ', size=(7, 1)), sg.Text('Danges')],
                       [sg.Text('Loan: ', size=(7, 1)), sg.Text(
                           loan, size=(10, 1), text_color='Red', key='-LOAN-')],
                       [sg.Text('Armor')], [sg.ProgressBar(100, orientation='h',
                                                           size=(20, 20), key='-ARMBAR-', bar_color=('Blue', 'White'))]]

    submenu_layout = [
        [sg.Button('Shop'), sg.Button('Loans'), sg.Button('Tic Tac Cock'), sg.Button('Word battle'), sg.Button('HP'), sg.Button('Pong!'), sg.Button('Invasion!')]]

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
                   [sg.Button('Buy'), sg.Button('Sell')],
                   [sg.Text('')]]

    right_layout = [[sg.Text('Inventory')],
                    [sg.Table(values=ds.data, headings=ds.headings,
                              auto_size_columns=False,
                              col_widths=[20, 10, 6],
                              justification='left',
                              num_rows=max(6, len(ds.data)),
                              key='-TABLEINV-',
                              row_height=20,
                              hide_vertical_scroll=bool(
                                  max(6, len(ds.data)) <= 6),
                              enable_events=True)],
                    [sg.Text('Progress')],
                    [sg.ProgressBar(days, orientation='h',
                                    size=(20, 20), key='-PROG-')]]

    travel_layout = [[sg.Button('Place1', key='-ND1-'),
                      sg.Button('Place2', key='-ND2-')],
                     [sg.Button('Place3', key='-ND3-'),
                      sg.Button('Place4', key='-ND4-')],
                     [sg.Button('Place5', key='-ND5-'),
                      sg.Button('Place6', key='-ND6-')]
                     ]

    info_layout = [[sg.MLine(key='-ML-', size=(70, 8))]]

    combined_layout = [[sg.Col(character_layout), sg.Col(
        character_stats), sg.Col(character_items)],
        sg.vtop(
        [sg.Col(submenu_layout, element_justification='l')]),
        sg.vtop(
        [sg.Col(info_layout), sg.Col(travel_layout)]),
        sg.vtop(
        [sg.Col(left_layout), sg.Col(right_layout)])]

    window = sg.Window('Druglordzz', combined_layout).Finalize()
    sg.cprint_set_output_destination(window, '-ML-')
    return window


def main(name, age, pic, days):
    global progress
    window = main_screen(name, age, pic, days)
    lg.loading_game()
    window.find_element('-HEALTH-').update(100)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'HP':
            ch.set_health(1)
            window['-HEALTH-'].update(ch.get_health())
            # eand event !=  ---- is gedaan zodat tekst alleen geprint wordt als drugs geselecteerd wordt.
        if values['-TABLE-'] and event not in ['Buy', 'Sell']:
            sg.cprint(
                'Trade ' + str(ds.data[int(values['-TABLE-'][0])][0]) +
                ' for $' + str(ds.data[int(values['-TABLE-'][0])][1]) + '?')
        if event in ['-ND1-', '-ND2-', '-ND3-', '-ND4-', '-ND5-', '-ND6-']:
            window['-TABLE-'].update(values=ds.price_random())
            ba.loan_interest()
            window['-LOAN-'].update(ba.get_interest_loan())
            window['-BALANCE-'].update(ba.get_balance(),
                                       text_color=ba.balance_colour())
            progress += 1
            ev.event_cop()
            window['-HEALTH-'].update(ch.get_health())
            window['-ARMBAR-'].update(ch.get_armornr())
            if progress > 10:
                progress = 0
                result = ba.get_balance() - ba.get_interest_loan()
                sg.popup('Game ends. You have earned: ', result)
                window.close()
                eg.endgame(name, result)
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
        if event == 'Shop':
            sh.shop_view()
            window['-WEAP-'].update(ch.get_weapon())
            window['-ARM-'].update(ch.get_armor())
            window['-BALANCE-'].update(ba.get_balance(),
                                       text_color=ba.balance_colour())
            window['-ARMBAR-'].update(ch.get_armornr())
        if event == 'Loans':
            lo.loan_selection()
            window['-LOAN-'].update(ba.get_interest_loan())
            window['-BALANCE-'].update(ba.get_balance(),
                                       text_color=ba.balance_colour())
        if event == 'Tic Tac Cock':
            tt.tic_selection()
            window['-BALANCE-'].update(ba.get_balance(),
                                       text_color=ba.balance_colour())
        if event == 'Word battle':
            wb.word_battle()
        if event == 'Pong!':
            try:
                run_game()
            except:
                pass
        if event == 'Invasion!':
            try:
                run_alien()
            except:
                pass
    window.close()


if __name__ == '__main__':
    # main()
    db.create_db()
    cs.char_selection()

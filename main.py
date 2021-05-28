import PySimpleGUI as sg

choices = ('Wiet', 'Hash', 'subbranch')
BAR_MAX = 10
i = 0

left_layout = [[sg.Text('Drugaloo')],
               [sg.Listbox(choices, size=(15, len(choices)), key='-DRUG-', enable_events=True)]]

right_layout = [[sg.Text('Bugaloo')],
                [sg.MLine(key='-ML-', size=(40, 8))],
                [sg.Text('Progress')],
                [sg.ProgressBar(BAR_MAX, orientation='h', size=(20,20), key='-PROG-')],
                [sg.Button('Next day', key='-NEXTDAY-')]]

combined_layout = [[sg.Column(left_layout), sg.Column(right_layout)],
                   [sg.OK()]]

window = sg.Window('Druglordzz', combined_layout)
sg.cprint_set_output_destination(window, '-ML-')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values['-DRUG-']:
        sg.cprint('farts')
    if event == '-NEXTDAY-':
        i+=1
        window['-PROG-'].update(i)
window.close()

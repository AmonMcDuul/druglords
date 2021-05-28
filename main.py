import PySimpleGUI as sg

choices = ('Wiet', 'Hash', 'Piemel Testje')

left_layout = [[sg.Text('Drugaloo')],
               [sg.Listbox(choices, size=(15, len(choices)), key='-DRUG-', enable_events=True)]]

right_layout = [[sg.Text('Bugaloo')],
                [sg.MLine(key='-ML-', size=(40, 8))]]

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
window.close()

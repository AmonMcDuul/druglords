import PySimpleGUI as sg
import drugs_stats as ds

BAR_MAX = 10
i = 0


left_layout = [[sg.Text('Drugaloo')],
               [sg.Table(values=ds.data, headings=ds.headings,
                         auto_size_columns=False,
                         col_widths=[20, 10],
                         justification='left',
                         num_rows=6,
                         key='-TABLE-',
                         row_height=20,
                         hide_vertical_scroll=True,
                         enable_events=True)]]

right_layout = [[sg.Text('Bugaloo')],
                [sg.MLine(key='-ML-', size=(40, 8))],
                [sg.Text('Progress')],
                [sg.ProgressBar(BAR_MAX, orientation='h',
                                size=(20, 20), key='-PROG-')],
                [sg.Button('Next day', key='-NEXTDAY-')]]

combined_layout = [[sg.Column(left_layout), sg.Column(right_layout)],
                   [sg.OK()]]

window = sg.Window('Druglordzz', combined_layout)
sg.cprint_set_output_destination(window, '-ML-')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values['-TABLE-']:
        sg.cprint(ds.data[int(values['-TABLE-'][0])][1])
    if event == '-NEXTDAY-':
        i += 1
        window['-PROG-'].update(i)
window.close()

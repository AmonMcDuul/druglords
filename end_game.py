import PySimpleGUI as sg
import database as db
import character_selection as cs


def endgame(name, end_score):
    db.insert_db_drug_lords(name, end_score)

    layout = [[sg.Text('Score:')],
              [sg.Text(end_score)],
              [sg.Table(values=db.select_db_drug_lords(), headings=['Name', 'Score'],
                        auto_size_columns=False,
                        col_widths=[20, 10, 6],
                        justification='left',
                        num_rows=max(10, 10),
                        key='-TABLEINV-',
                        row_height=20,
                        hide_vertical_scroll=True)],
              [sg.Button('Exit'), sg.Button('New game')],
              ]

    window = sg.Window('Frug lorss scoreboard!',
                       layout, finalize=True)

    while True:
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'New game':
            window.close()
            cs.char_selection()
    window.close()

import PySimpleGUI as sg
import main
import skincolor as sc

count = 1
avatar = 'img//avatar_orig.png'


def character_view():
    character_layout = [[sg.Text('Make ya gangsta yo')],
                        [sg.Text('Name: '), sg.Input(
                            'Poopiebuts', key='-NAME-')],
                        [sg.Text('Age: '), sg.Input(key='-AGE-')],
                        [sg.Button('<'), sg.Image(
                            avatar, key='-IMG-'), sg.Button('>')],
                        [sg.Text('Want a mustache?'), sg.Button('|||||')],
                        [sg.Button('10 days', key='-10-'), sg.Button('30 days', key='-30-'), sg.Button(
                            '60 days', key='-60-'), sg.Button('90 days', key='-90-'), sg.Button('120 days', key='-120-')]
                        ]
    character_window = sg.Window('Shoppa', character_layout)
    return character_window


def char_selection():
    character_window = character_view()
    while True:
        event, values = character_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-10-':
            character_window.close()
            main.main(values['-NAME-'], values['-AGE-'], 'img\\avatar.png', 10)
        if event == '-30-':
            character_window.close()
            main.main(values['-NAME-'], values['-AGE-'], 'img\\avatar.png', 30)
        if event == '-60-':
            character_window.close()
            main.main(values['-NAME-'], values['-AGE-'], 'img\\avatar.png', 60)
        if event == '-90-':
            character_window.close()
            main.main(values['-NAME-'], values['-AGE-'], 'img\\avatar.png', 90)
        if event == '-120-':
            character_window.close()
            main.main(values['-NAME-'], values['-AGE-'],
                      'img\\avatar.png', 120)
        if event == '>':
            character_window['-IMG-'].update(sc.rand_tone())
        if event == '<':
            character_window['-IMG-'].update(sc.rand_tone())
        if event == '|||||':
            character_window['-IMG-'].update(sc.add_mustache())
    character_window.close()

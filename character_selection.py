import PySimpleGUI as sg
import main
import skincolor as sc

count = 1
playtime = ['30', '60', '90']
avatar = 'img//avatar_orig.png'

# def picture_picker(n):
#     global count
#     if n == 2:
#         count += 1
#         if count == 6:
#             count = 1
#     if n == 1:
#         count -= 1
#         if count == 0:
#             count = 5
#     picture = ('img//' + str(count)+'poppetje.png')
#     return picture


def character_view():
    character_layout = [[sg.Text('Make ya gangsta yo')],
                        [sg.Text('Name: '), sg.Input(key='-NAME-')],
                        [sg.Text('Age: '), sg.Input(key='-AGE-')],
                        [sg.Button('<'), sg.Image(
                            avatar, key='-IMG-'), sg.Button('>')],
                        [sg.Text('choose playtime: '), sg.Combo(playtime)],
                        [sg.Button('Go deal some drugs yo', key='-GO-')]
                        ]
    character_window = sg.Window('Shoppa', character_layout)
    return character_window


def char_selection():
    character_window = character_view()
    while True:
        event, values = character_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-GO-':
            character_window.close()
            main.main(values['-NAME-'], values['-AGE-'], 'img\\avatar.png')
        if event == '>':
            character_window['-IMG-'].update(sc.rand_tone())
        if event == '<':
            character_window['-IMG-'].update(sc.rand_tone())
    character_window.close()

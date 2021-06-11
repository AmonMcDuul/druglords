import PySimpleGUI as sg
import character as ch
import random


def event_cop():
    if random.randint(1, 5) == 1:
        cop_selection()


def cop_view():
    pic = "img\\cop.png"
    cop_layout = [[sg.Text('Your under arrest, buddy!')], [
        sg.Image(pic, key='-PROFILE_PIC-')],
        [sg.Button('Fight'), sg.Button('Run'), sg.Button('Bribe')]
    ]
    cop_window = sg.Window('Copper attack!', cop_layout)
    return cop_window


def fight():
    global health
    weapon = ch.get_weapon()
    if weapon == 'Vuistah':
        if random.randint(1, 5) == 1:
            sg.PopupQuickMessage('You have escaped!')
            return True
    elif weapon == 'Knife':
        if random.randint(1, 5) in (1, 2):
            sg.PopupQuickMessage('You have escaped!')
            return True
    elif weapon == 'Gun':
        if random.randint(1, 5) in (1, 2, 3):
            sg.PopupQuickMessage('You have escaped!')
            return True
    elif weapon == 'Ak47':
        if random.randint(1, 5) in (1, 2, 3, 4):
            sg.PopupQuickMessage('You have escaped!')
            return True
    armor = ch.get_armornr()
    if random.randint(1, 3) == 1:
        sg.PopupQuickMessage('DA COPPA SHOT YAAAA!!! KABLOWIE!')
        if armor > 0:
            ch.set_armornr(-25)
        else:
            ch.set_health(25)
    else:
        sg.PopupQuickMessage(
            'Cops shot but missed ya, cops are still after you bebe boy')
    return False


def run():
    if random.randint(1, 5) == 1:
        sg.PopupQuickMessage('You have escaped!')
        return True
    if random.randint(1, 3) == 1:
        sg.PopupQuickMessage('DA COPPA SHOT YAAAA!!! KABLOWIE!')
        if armor > 0:
            ch.set_armornr(-25)
        else:
            ch.set_health(25)
    else:
        sg.PopupQuickMessage(
            'Cops shot but missed ya, cops are still after you bebe boy')
    return False


def bribe():
    if random.randint(1, 2) == 1:
        return True
    return False


def cop_selection():
    cop_window = cop_view()
    while True:
        event, values = cop_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Fight':
            if fight():
                break
        if event == 'Run':
            if run():
                break
    cop_window.close()

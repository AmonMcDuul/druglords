import PySimpleGUI as sg
import random


def event_cop():
    if random.randint(1, 5) == 1:
        cop_selection()


def cop_view():
    pic = "img\\cop.png"
    cop_layout = [[sg.Text('Your under arrest, buddy!')], [
        sg.Image(pic, key='-PROFILE_PIC-')]]
    cop_window = sg.Window('Copper attack!', cop_layout)
    return cop_window


def cop_selection():
    cop_window = cop_view()
    while True:
        event, values = cop_window.read()
        if event == sg.WIN_CLOSED:
            break
    cop_window.close()

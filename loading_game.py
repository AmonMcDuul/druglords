import PySimpleGUI as sg


def loading_game():
    for i in range(1000):   # this is your "work loop" that you want to monitor
        sg.OneLineProgressMeter('One Line Meter Example', i + 1, 1000, 'key')

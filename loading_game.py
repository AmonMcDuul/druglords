import PySimpleGUI as sg


def loading_game():
    for i in range(200):   # this is your "work loop" that you want to monitor
        sg.OneLineProgressMeter('One Line Meter Example', i + 1, 200, 'key')

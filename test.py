import PySimpleGUI as sg

for i in range(1000):
    sg.OneLineProgressMeter('One Line Meter Example', i + 1, 1000, 'key')

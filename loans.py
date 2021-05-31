import PySimpleGUI as sg


def loan_view():
    loan_layout = [[sg.Text('Get ya loan yo bitch ass')],
                   ]
    loan_window = sg.Window('Loans', loan_layout)
    return loan_window


def loan_selection():
    loan_window = loan_view()
    while True:
        event, values = loan_window.read()
        if event == sg.WIN_CLOSED:
            break
    loan_window.close()

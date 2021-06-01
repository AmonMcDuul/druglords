import PySimpleGUI as sg
import bank_account as ba

loanshark = 'img\\loanshark.png'


def loan_view():
    loan_layout = [[sg.Text('Get ya loan yo bitch ass')],
                   [sg.Image(loanshark)],
                   [sg.Slider(key='-NUM-',
                              tick_interval=5000,
                              range=(0, 10000),
                              default_value=0,
                              size=(20, 15),
                              orientation='horizontal',
                              font=('Helvetica', 12))],
                   [sg.Text('Rate 1.5%')],
                   [sg.Button('Loan'), sg.Button('Pay back')]]
    loan_window = sg.Window('Loans', loan_layout)
    return loan_window


def loan_selection():
    loan_window = loan_view()
    while True:
        event, values = loan_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Loan':
            ba.set_loan(values['-NUM-'])
            ba.set_interest_loan(values['-NUM-'])
            break
    loan_window.close()

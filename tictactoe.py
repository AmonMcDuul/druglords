import PySimpleGUI as sg
import numpy as np
import random
import bank_account as ba

player_x = 'Red'
player_o = 'Blue'
player_none = 'White'


def checkbox(n):
    boxes = []
    key = 1
    for j in range(1, (n//3)+1):
        temp = []
        for i in range(1, (n//3)+1):
            temp.append(
                sg.Button('', button_color=player_none, enable_events=True, key=f"-BOX{key}-", size=(4, 2)))
            key += 1
        boxes.append(temp)
    return boxes


def tic_view():
    tic_layout = [[sg.Text('Ur in trouble now, mister!')], [sg.Frame(
        'Tic tac toe or die!', checkbox(9), font='Helvetica', title_color='Black')]]
    tic_window = sg.Window('Tic tac toe bitch!', tic_layout)
    return tic_window


def tic_selection():
    tic_window = tic_view()
    arr = np.zeros((3, 3), dtype=str)
    while True:
        event, values = tic_window.read()
        if event == sg.WIN_CLOSED:
            break
        for k in range(1, 10):
            if event == f"-BOX{k}-":
                entry = enter(arr, (k-1) // 3, (k+2) % 3, "X")
                if entry == False:
                    break
                tic_window[f'-BOX{k}-'].update(button_color=player_x)
                move = ai_move(arr)
                if move != False:
                    tic_window.FindElement(
                        f"-BOX{move}-").Update(button_color=player_o)
                    if solve_check(arr):
                        tic_window.close()
                        break
                else:
                    if solve_check(arr):
                        tic_window.close()
                        break
                    win_check("D")
                    tic_window.close()
                    break
    tic_window.close()


# tic-tac-toe-logic
def enter(arr, x, y, value):
    if arr[x, y] != 'X' and arr[x, y] != 'O':
        arr[x, y] = value
        return arr
    else:
        sg.Popup('Bad move!')
        return False


def solve_check(arr):
    for value in ["X", "O"]:
        x_count_col = np.count_nonzero(arr == value,  axis=0)
        x_count_row = np.count_nonzero(arr == value,  axis=1)

        arr_diag1 = arr.diagonal()
        arr_diag2 = np.fliplr(arr).diagonal()

        if max(x_count_row) == 3 or max(x_count_col) == 3 or np.count_nonzero(arr_diag1 == value) == 3 or np.count_nonzero(arr_diag2 == value) == 3:
            win_check(value)
            return True
    return False


def win_check(value):
    arr = np.zeros((3, 3), dtype=str)
    if value == "X":
        win_toe()
        return sg.Popup('You win badboy Jim!')
    elif value == "O":
        lose_toe()
        return sg.Popup('You lose Bruce!')
    elif value == "D":
        draw_toe()
        return sg.Popup('Its-a-draw!')

# AI


def ai_move(arr):
    zero_pos = np.argwhere(arr == '')
    try:
        rand_pos = random.choice(zero_pos)
        arr[rand_pos[0], rand_pos[1]] = "O"
        number = (rand_pos[0]*3) + (rand_pos[1]+1)
        return number
    except:
        return False


def lose_toe():
    ba.balance *= 0.9


def win_toe():
    ba.balance *= 1.1


def draw_toe():
    ba.balance *= 0.98

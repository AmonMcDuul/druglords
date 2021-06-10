import threading
import time
import PySimpleGUI as sg
import random
import database as db


def random_word():
    list_words = ['kneusje', 'poeperik', 'langzaam', 'jan willem', 'stinkt', 'naar billen',
                  'jantje beton', 'bad boyzx', 'retecoolspel', 'februari farts', 'windjes', 'monument', 'hahahiho', 'supemannetje', 'knurft', 'mieters']
    x = random.randint(0, len(list_words)-1)
    return list_words[x]


def scoreboard(name, end_score):
    db.insert_db_word_battle(name, end_score)

    layout = [[sg.Text('Score:')],
              [sg.Text(end_score)],
              [sg.Table(values=db.select_db_word_battle(), headings=['Name', 'Score'],
                        auto_size_columns=False,
                        col_widths=[20, 10, 6],
                        justification='left',
                        num_rows=max(10, 10),
                        key='-TABLEINV-',
                        row_height=20,
                        hide_vertical_scroll=True)],
              [sg.Button('Exit')],
              ]

    window = sg.Window('Word battle scoreboard!',
                       layout, finalize=True)

    while True:
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()


def long_operation_thread(seconds, window):
    progress = 0
    print('Thread started - will sleep for {} seconds'.format(seconds))
    for i in range(int(seconds * 10)):
        time.sleep(.1)
        progress += 100 / (seconds * 10)
        window.write_event_value('-PROGRESS-', progress)


def word_battle():
    word_to_battle = 'Word battle bitches!'
    score = 0
    layout = [[sg.Text('Word battle, TO THE DEATH!!!')],
              [sg.Text(
                  'Je hebt 15 seconden de tijd om zoveel mogelijk woorden over te typen!!!')],
              [sg.Text('Name: '), sg.Input('Voer naam in', key='-NAME-')],
              [sg.Button('Start game')],
              [sg.Text(text=word_to_battle, font='Default 18', key='-WTB-'),
               sg.Input(key='-W1-')],
              [sg.Text('Score:')],
              [sg.Text(score, key='-SCO-')],
              [sg.Text('Work progress'), sg.ProgressBar(
                  100, size=(20, 20), orientation='h', key='-PROG-')],
              [sg.Button('Exit')],
              ]

    window = sg.Window('Word battle biatschaz!',
                       layout, finalize=True)

    timeout = thread = None

    while True:
        event, values = window.read(timeout=timeout)
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == ('Start game') and len(values['-NAME-']) > 1 and not thread:
            thread = threading.Thread(target=long_operation_thread, args=(
                float(15), window), daemon=True)
            word_to_battle = random_word()
            word_to_battle_change = word_to_battle
            window['-WTB-'].update(word_to_battle)
            thread.start()
        elif word_to_battle == values['-W1-']:
            word_to_battle = random_word()
            word_to_battle_change = word_to_battle
            window['-WTB-'].update(word_to_battle)
            window['-W1-'].update('')
            score += 1
            window['-SCO-'].update(score)
        elif values[event] > 99:
            break
        elif event == '-PROGRESS-':
            window['-PROG-'].update_bar(values[event], 100)
        elif event == '-THREAD-':
            thread.join(timeout=0)
            sg.popup_animated(None)
            thread, message, progress, timeout = None, '', 0, None
            window['-PROG-'].update_bar(0, 0)
    window.close()
    scoreboard(values['-NAME-'], score)

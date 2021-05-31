import PySimpleGUI as sg
import main
import drugs_stats as ds
import bank_account as ba
import character as ch

weapon_icon = 'weapon.png'
armor_icon = 'armor.png'
fart_icon = 'fart.png'


def shop_view():
    shop_layout = [[sg.Text('Get to da Shoppa')],
                   [sg.SimpleButton('', image_filename=weapon_icon, image_size=(
                       100, 100), image_subsample=2, border_width=1, key='-WEAPON-'), sg.SimpleButton('', image_filename=armor_icon, image_size=(
                           100, 100), image_subsample=2, border_width=1, key='-ARMOR-'), sg.SimpleButton('', image_filename=fart_icon, image_size=(
                               100, 100), image_subsample=2, border_width=1)]]
    shop_window = sg.Window('Shoppa', shop_layout)

    while True:
        event, values = shop_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-WEAPON-':
            weapon_view()
            break
        if event == '-ARMOR-':
            armor_view()
            break
    shop_window.close()


def weapon_view():
    weapon_shop_layout = [[sg.Text('Weapon shop')],
                          [sg.SimpleButton('', image_filename=weapon_icon, image_size=(
                              100, 100), image_subsample=2, border_width=1, key='-WEAPON1-')]]
    weapon_shop_window = sg.Window('Shoppa', weapon_shop_layout)

    while True:
        event, values = weapon_shop_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-WEAPON1-':
            ch.weapon_bought('Gun')
            break
    weapon_shop_window.close()


def armor_view():
    armor_shop_layout = [[sg.Text('Armor shop')],
                         [sg.SimpleButton('', image_filename=armor_icon, image_size=(
                             100, 100), image_subsample=2, border_width=1, key='-ARMOR1-')]]
    armor_shop_window = sg.Window('Shoppa', armor_shop_layout)

    while True:
        event, values = armor_shop_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-ARMOR1-':
            ch.armor_bought('Bulletproof vest')
            break
    armor_shop_window.close()

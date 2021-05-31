import PySimpleGUI as sg
import main
import drugs_stats as ds
import bank_account as ba
import character as ch

weapon_shop_icon = 'img\\weapon.png'
armor_shop_icon = 'img\\armor.png'
fart_icon = 'img\\fart.png'

knife_icon = 'img\\knife.png'
gun_icon = 'img\\weapon.png'
ak_icon = 'img\\ak.png'

vest_icon = 'img\\vest.png'
armor_icon = 'img\\armor.png'
knight_icon = 'img\\knightarmor.png'


def shop_view():
    shop_layout = [[sg.Text('Get to da Shoppa')],
                   [sg.SimpleButton('', image_filename=weapon_shop_icon, image_size=(
                       100, 100), image_subsample=2, border_width=1, key='-WEAPON-'), sg.SimpleButton('', image_filename=armor_shop_icon, image_size=(
                           100, 100), image_subsample=2, border_width=1, key='-ARMOR-'), sg.SimpleButton('', image_filename=fart_icon, image_size=(
                               100, 100), image_subsample=2, border_width=1, key='-FART-')]]
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
        if event == '-FART-':
            sg.popup('You aint no buying no farts dawg!')
    shop_window.close()


def weapon_view():
    weapon_shop_layout = [[sg.Text('Weapon shop')],
                          [sg.SimpleButton('', image_filename=knife_icon, image_size=(
                              100, 100), image_subsample=2, border_width=1, key='-KNIFE-'), sg.SimpleButton('', image_filename=gun_icon, image_size=(
                                  100, 100), image_subsample=2, border_width=1, key='-GUN-'), sg.SimpleButton('', image_filename=ak_icon, image_size=(
                                      100, 100), image_subsample=2, border_width=1, key='-AK-')]]
    weapon_shop_window = sg.Window('Shoppa', weapon_shop_layout)

    while True:
        event, values = weapon_shop_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-KNIFE-':
            ch.weapon_bought('Knife')
            break
        if event == '-GUN-':
            ch.weapon_bought('Gun')
            break
        if event == '-AK-':
            ch.weapon_bought('Ak47')
            break
    weapon_shop_window.close()


def armor_view():
    armor_shop_layout = [[sg.Text('Armor shop')],
                         [sg.SimpleButton('', image_filename=vest_icon, image_size=(
                             100, 100), image_subsample=2, border_width=1, key='-VEST-'), sg.SimpleButton('', image_filename=armor_icon, image_size=(
                                 100, 100), image_subsample=2, border_width=1, key='-ARMOR-'), sg.SimpleButton('', image_filename=knight_icon, image_size=(
                                     100, 100), image_subsample=2, border_width=1, key='-KNIGHT-')]]
    armor_shop_window = sg.Window('Shoppa', armor_shop_layout)

    while True:
        event, values = armor_shop_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-VEST-':
            ch.armor_bought('Vest')
            break
        if event == '-ARMOR-':
            ch.armor_bought('Kevlar')
            break
        if event == '-KNIGHT-':
            ch.armor_bought('Knight armor')
            break
    armor_shop_window.close()

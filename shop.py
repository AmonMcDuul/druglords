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
                   [sg.SimpleButton('1000', image_filename=weapon_shop_icon, image_size=(
                       100, 100), image_subsample=2, border_width=1, key='-WEAPON-'), sg.SimpleButton('', image_filename=armor_shop_icon, image_size=(
                           100, 100), image_subsample=2, border_width=1, key='-ARMOR-'), sg.SimpleButton('', image_filename=fart_icon, image_size=(
                               100, 100), image_subsample=2, border_width=1, key='-FART-')]]

    while True:
        shop_window = sg.Window('Shoppa', shop_layout)
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
            break
    shop_window.close()


def weapon_view():
    knife_layout = [[sg.Text('Knife')],
                    [sg.SimpleButton('', image_filename=knife_icon, image_size=(
                        100, 100), image_subsample=2, border_width=1, key='-KNIFE-')],
                    [sg.Text('1000,00', text_color=ba.shop_price_colour(1000))]]

    gun_layout = [[sg.Text('Gun')],
                  [sg.SimpleButton('', image_filename=gun_icon, image_size=(
                      100, 100), image_subsample=2, border_width=1, key='-GUN-')],
                  [sg.Text('5000,00', text_color=ba.shop_price_colour(5000))]]

    ak_layout = [[sg.Text('AK47')],
                 [sg.SimpleButton('', image_filename=ak_icon, image_size=(
                     100, 100), image_subsample=2, border_width=1, key='-AK-')],
                 [sg.Text('10000,00', text_color=ba.shop_price_colour(10000))]]

    weapon_shop_layout = [
        [sg.Col(knife_layout), sg.Col(gun_layout), sg.Col(ak_layout)]]

    while True:
        weapon_shop_window = sg.Window('Weapon shop', weapon_shop_layout)
        event, values = weapon_shop_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-KNIFE-':
            if can_buy(1000):
                ch.weapon_bought('Knife')
                ba.update_balance_shop(1000)
            else:
                sg.popup('You aint got no money fool!')
            break
        if event == '-GUN-':
            if can_buy(5000):
                ch.weapon_bought('Gun')
                ba.update_balance_shop(5000)
            else:
                sg.popup('You aint got no money fool!')
            break
        if event == '-AK-':
            if can_buy(10000):
                ch.weapon_bought('Ak47')
                ba.update_balance_shop(10000)
            else:
                sg.popup('You aint got no money fool!')
            break
    weapon_shop_window.close()
    shop_view()


def armor_view():
    vest_layout = [[sg.Text('Vest')],
                   [sg.SimpleButton('', image_filename=vest_icon, image_size=(
                       100, 100), image_subsample=2, border_width=1, key='-VEST-')],
                   [sg.Text('1000,00', text_color=ba.shop_price_colour(1000))]]

    armor_layout = [[sg.Text('Kevlar')],
                    [sg.SimpleButton('', image_filename=armor_icon, image_size=(
                        100, 100), image_subsample=2, border_width=1, key='-ARMOR-')],
                    [sg.Text('5000,00', text_color=ba.shop_price_colour(5000))]]

    knight_layout = [[sg.Text('Knight armor')],
                     [sg.SimpleButton('', image_filename=knight_icon, image_size=(
                         100, 100), image_subsample=2, border_width=1, key='-KNIGHT-')],
                     [sg.Text('10000,00', text_color=ba.shop_price_colour(10000))]]

    armor_shop_layout = [
        [sg.Col(vest_layout), sg.Col(armor_layout), sg.Col(knight_layout)]]

    while True:
        armor_shop_window = sg.Window('Shoppa', armor_shop_layout)
        event, values = armor_shop_window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-VEST-':
            if can_buy(1000):
                ch.armor_bought('Vest')
                ba.update_balance_shop(1000)
                ch.set_armornr(25)
            else:
                sg.popup('You aint got no money fool!')
            break
        if event == '-ARMOR-':
            if can_buy(5000):
                ch.armor_bought('Kevlar')
                ba.update_balance_shop(5000)
                ch.set_armornr(60)
            else:
                sg.popup('You aint got no money fool!')
            break
        if event == '-KNIGHT-':
            if can_buy(10000):
                ch.armor_bought('Knight armor')
                ba.update_balance_shop(10000)
                ch.set_armornr(100)
            else:
                sg.popup('You aint got no money fool!')
            break
    armor_shop_window.close()
    shop_view()


def can_buy(n):
    balance = ba.get_balance()
    if balance - n >= 0:
        return True
    else:
        return False

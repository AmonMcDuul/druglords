import PySimpleGUI as sg

weapon = 'Vuistah'
armor = 'Blote buikjah'
health = 100
armornr = 0


def set_health(n):
    global health
    health -= n
    return health


def get_health():
    global health
    return health


def get_weapon():
    global weapon
    return weapon


def weapon_bought(n):
    global weapon
    weapon = n
    return weapon


def get_armor():
    global armor
    return armor


def armor_bought(n):
    global armor
    armor = n
    return armor


def get_armornr():
    global armornr
    return armornr


def set_armornr(n):
    global armornr
    armornr += n
    if armornr >= 100:
        armornr = 100
    print(armornr)
    return armornr

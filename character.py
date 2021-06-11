import PySimpleGUI as sg

weapon = 'Vuistah'
armor = 'Blote buikjah'
health = 100


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

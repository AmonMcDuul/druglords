from sqlite3 import connect


def create_db():
    ''' create database if one does not already exist '''
    with connect('drugwars.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS word_battle(id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")


def insert_db_word_battle(name, score):
    with connect('drugwars.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO word_battle VALUES(NULL, ?, ?)", (name, score))
            return True
        except:
            sg.popup_error(
                'het luktnieee')
            return False


def select_db_word_battle():
    with connect('drugwars.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "select name, score from word_battle order by score desc")
        row = cursor.fetchone()
        if row == None:
            lijst = [('', '')]
            return lijst
        lijst = []
        lijst.append(row)
        for i in cursor:
            lijst.append(i)
        print(lijst)
        return lijst

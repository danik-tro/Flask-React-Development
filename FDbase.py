import sqlite3

class FdataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT title FROM  mainmenu'''

        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except:
            print('Ошибка чтения из DB')
        return []

        
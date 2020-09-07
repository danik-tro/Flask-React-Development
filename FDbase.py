import sqlite3

class FdataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenu(self):
        sql = '''SELECT * FROM  mainmenu'''

        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()

            result = [dict(row) for row in res]
            print(result)
            if result:
                return result

        except:
            print('Ошибка чтения из DB')
        return []

        
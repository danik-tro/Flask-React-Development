import sqlite3
import time
import math


class FdataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def returnResult(self, fetchall):
        return [dict(row) for row in fetchall]



    def getMenu(self):
        sql = '''SELECT * FROM  mainmenu'''

        try:
            self.__cur.execute(sql)
            

            result = self.returnResult(self.__cur.fetchall())
            print(result)
            if result:
                return result

        except:
            print('Ошибка чтения из DB')
        return []

    def addPost(self, title, text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)",
                        (title, text, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления статьи в БД" + str(e))
            return False
        
        return True

        
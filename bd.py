from flask import Flask, render_template, request, g, flash
import sqlite3
import os
from FDbase import FdataBase

"""
    ! g - контекст приложения
"""
"""
    ! Configuration
"""
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'sghowh2hg82gh09g20gh2hgohg90whewkjdhoiwjf092'


"""
    ! Creating app
"""
app = Flask(__name__)
app.config.from_object(__name__)

#! Path to DB
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))


"""
    ! Connecting to db
"""
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])

    return conn


def run_sql(name_script):
    db = connect_db()
    with app.open_resource(name_script, mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


"""
    ! Creating db
"""
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


"""
    ! Соединение с DB
"""
def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


"""
    ! Разрывание связи с DB
"""
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()
    

@app.route('/')
def index():
    db = get_db()

    dbase = FdataBase(db)
    return render_template('index.html', menu=dbase.getMenu())

"""
    ! В шаблонах html в url_for нужно писать не жесткие пути
    ! А функцию представления, как в случае с фукнцией addPost

    * Путь /add_post, но функция представления addPost()
"""
@app.route('/add_post', methods=['POST', "GET"])
def addPost():
    db = get_db()
    dbase = FdataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'])

            if not res:
                flash('Ошибка добавления статьи', category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash('Ошибка добавления статьи', category='error')
    return render_template('add_post.html', menu=dbase.getMenu(), title='Добавление статьи')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, g
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
    """tmp = dbase.getMenu()
    tmp[0]['url'] = '/'
    tmp[1]['url'] = 'add_post'
    print(tmp)"""
    return render_template('index.html', menu=dbase.getMenu())



if __name__ == '__main__':
    app.run(debug=True)
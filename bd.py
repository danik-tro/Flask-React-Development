from flask import Flask, render_template, request
import sqlite3
import os

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
    conn.row_factory = sqlite3.Row

    return conn

"""
    ! Creating db
"""
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


@app.route('/self')
def self():
    return "Hello, world!"


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

"""
! В templates - хранятся шаблоны.
! В static - все статические зависимости, вроде JS&CSS
! render_template - возвращает шаблон
"""

@app.route('/')
def index():
    return render_template("hello.html", title="Start page")

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template(
        'hello.html', name=name,
        title=name if name else "Hello page"
        )


if __name__ == "__main__":
    app.run(debug=True)
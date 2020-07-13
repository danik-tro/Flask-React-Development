from flask import Flask, render_template

app = Flask(__name__)

"""
! В templates - хранятся шаблоны.
! В static - все статические зависимости, вроде JS&CSS
! render_template - возвращает шаблон
* url_for - возвращает контекст запроса. ЮРЛ текущего подключения

! Искусственное создание контекста
*with app.test_request_context():
*    print(url_for('about'))


* @app.route('/<name>') - <name> - динамический маршрут

? <path:name> - path: означает, что весь путь, что будет
? записан в строке, будет отображаться

!path: - любые символы
!int: - только числа
!float - только числа с плавающей точкой

! Статические файлы
? url_for('static', filename = "css/styles.css")
? templates
? static
?    |
?    |____css
?          |
?          |__styles.css
"""

@app.route('/')
def index():
    x = [1,2,3,4]
    return render_template(
        "index.html",
        title="Start page",
        menu=x)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    
    return render_template(
        'index.html', name=name,
        title=name if name else "Привет мир",
        menu=[]
        )


if __name__ == "__main__":
    app.run(debug=True)
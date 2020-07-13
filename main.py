from flask import Flask, render_template, url_for, request

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

menu = [
    {"name" : "Установка", "url" : "install-flask"},
    {"name" : "Первое приложение", "url" : "first-app"},
    {"name" : "Обратная связь", "url" : "contact"}
    ]

@app.route('/')
def index():
    
    return render_template(
        "index.html",
        menu=menu)

@app.route('/about/')
@app.route('/about/<name>')
def about(name="Про Flask"):
    
    return render_template(
        'about.html', name=name,
        title="Flask",
        menu=menu
        )

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        print(request.form)

    return render_template("contact.html", title="Обратная связь", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
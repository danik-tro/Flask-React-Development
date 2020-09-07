from flask import (Flask,
    render_template, url_for, request,
    flash, redirect, session, abort)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sghowh2hg82gh09g20gh2hgohg90whewkjdhoiwjf092'#Произвольные символы. Чем тяжелее, тем лучше

"""
    ! для активации виртуальной среды - source ./venv/bin/source
"""



"""
! В templates - хранятся шаблоны.
! В static - все статические зависимости, вроде JS&CSS
! render_template - возвращает шаблон
* url_for - возвращает контекст запроса. ЮРЛ текущего подключения

! url_for('/profile', [параметры для юрл])

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
    {"name": "Авторизация", "url" : "login"},
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



"""
    * @app.route('/path....', methods=['GET', 'POST'..])
    * def name_function():
    *    if request.method == 'POST':
    *       print(request.form) # выведет на экран
    *                   словарь формы с ее аргументами            
    ! Данный шаблон илюстрирует, как нужно создавать маршруты для 
    ! Функций, где может быть get или post запросы
"""

"""
    ! Функция abort - возвращает код с ошибкой и прерывает сессию
    ! Пример: abort(401) - странице будет возвращена ошибка с кодом 401

    ! redirect - перенаправление на страницу
"""



@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash("Сообщение оптравлено", category='success')
        else:
            flash("Ошибка отправки", category='error')

    return render_template("contact.html", title="Обратная связь", menu=menu)



@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'selfedu' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Авторизация', menu=menu)


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'Профиль пользователя: {username}'

@app.errorhandler(401)
def page401(error):
    return f'Ошибка с кодом {error}'


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
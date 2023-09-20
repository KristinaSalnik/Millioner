from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html> c
    <head>
        <title> Сальник Кристина Андреевна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <footer>
            &copy; Кристина Сальник, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title> Сальник Кристина Андреевна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
            Flask - фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков
            минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.Flask - фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков
            минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </header>
          <a href="/menu" target="_blank" >Меню</a>
            <h2>Реализованные роуты</h2>
            <ul>
                <li>
                    <a href="/lab1/oak.jpg" target="_blank" >/lab1/oak.jpg - oak.jpg</a>
                </li>
                <li>
                    <a href="/lab1/logo.png" target="_blank" >/lab1/logo.png - logo.png</a>
                </li>
                <li>
                    <a href="/lab1/python.png" target="_blank" >/lab1/python.png - python.png</a>
                </li>
                <li>
                    <a href="/lab1/kot.jpg" target="_blank" >/lab1/kot.jpg - kot.jpg</a>
                </li>
            </ul>
        <footer>
            &copy; Кристина Сальник, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route('/lab1/oak.jpg')
def oak():
    return'''
<!doctype html>
<html>
     <head>
        <title>Сальник Кристина Андреевна, лабораторная 1</title>
    </head>
     <body>
     <link rel="stylesheet" href="'''+ url_for('static', filename="oak.jpg")+'''">
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>
          <h1>Дуб</h1>
          <img src=''' + url_for('static', filename='oak.jpg') + '''>
    <footer>
    &copy; Сальник Кристина, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''

@app.route('/lab1/logo.png')
def student():
    return'''
    <!doctype html>
<html>
     <head>
        <title>Сальник Кристина Андреевна, лабораторная 1</title>
        <link rel="stylesheet" href="'''+ url_for('static', filename ="logo.png")+'''">
    </head>
     <body>
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>
          <h1>Сальник Кристина Андреевна</h1>
          <img src=''' + url_for('static', filename='logo.png') + '''>
    <footer>
    &copy; Сальник Кристина, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''

@app.route('/lab1/python.png')
def python():
    return'''
    <!doctype html>
<html>
     <head>
        <title>Сальник Кристина Андреевна, лабораторная 1</title>
        <link rel="stylesheet" href="'''+ url_for('static', filename = "python.png")+'''">
    </head>
     <body>
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>
          <p>Python, согласно данным из Google – язык программирования высокого уровня общего назначения.
          Обладает типизацией динамического строгого характера. Имеет автоматическое управление памятью, за счет чего осуществляется
          повышение производительности контента, написанного на нем.</p>
          
          <p>Python – объектно-ориентированный язык программирования, пользующийся спросом у большинства
          современных разработчиков. Коды, написанные на нем, достаточно легко читать.</p>
          
          <p>Python - это простой в освоении, но мощный и универсальный язык сценариев,
          что делает его привлекательным для разработки приложений.</p>
          <img src=''' + url_for('static', filename='python.png') + '''>
    <footer>
    &copy; Сальник Кристина, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''

@app.route('/lab1/kot.jpg')
def kot():
    return'''
    <!doctype html>
<html>
     <head>
        <title>Сальник Кристина Андреевна, лабораторная 1</title>
        <link rel="stylesheet" href="'''+ url_for('static', filename='kot.jpg')+'''">
    </head>
     <body>
     <header>
     НГТУ, ФБ, Лабораторная работа 1
     </header>
          <p>Я нашла фотографию кошки. Ту, что первая попалась. Так как уже очень устала.</p>
          
          <p>Делаю лабораторную в 2 ночи. А все потому, что обычно днем не хватает времени даже на нормальный обед. И сейчас просто сижу и пишу бред из головы</p>
          
          <p>Просьба не воспринимать буквально или близко к сердцу. Я почти сплю)))</p>
          <img src=''' + url_for('static', filename='kot.jpg') + '''>
    <footer>
    &copy; Сальник Кристина, ФБИ-14, 3 курс, 2023
    </footer>
    </body>
</html>
'''

@app.route('/lab2/example')
def example():
    name = 'Salnik Kristina'
    course = '3 курс'
    group = 'фби-14'
    fruits = [
        {'name':'яблоки', 'price': 100},
        {'name':'груши', 'price': 120},
        {'name': 'апельсины', 'price':80},
        {'name': 'мандарины', 'price':95},
        {'name': 'манго', 'price':312}
        ]
    return render_template('example.html', name=name, course=course, group=group, fruits=fruits)
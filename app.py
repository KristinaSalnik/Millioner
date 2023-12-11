from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from Db import db
from Db.models import users, articles
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = '123'
user_db = 'kris_knowledge_base_orm'
host_ip = '127.0.0.1'
host_port = '5432'
database_name = 'knowledge_base_orm'
password = '123'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password}@{host_ip}:{host_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


login_manager = LoginManager()
login_manager.login_view = 'lab6.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_users(user_id):
    return users.query.get(int(user_id))

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)


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
    Book = [
        {'name': 'Пушкин А.С.', 'book_name': 'Метель', 'genre': 'драмма', 'num': 300},
        {'name': 'Булгаков', 'book_name': 'Мастер и Маргарита', 'genre': 'драмма', 'num': 3980},
        {'name': 'Пушкин А.С.', 'book_name': 'Метель', 'genre': 'драмма', 'num': 676},
        {'name': 'Грибоедов', 'book_name': 'Горе от ума', 'genre': 'драмма', 'num': 300},
        {'name': 'Замятин', 'book_name': 'Мы', 'genre': 'классика', 'num': 67},
        {'name': 'Достоевский', 'book_name': 'Идиот', 'genre': 'драмма', 'num': 3333},
        {'name': 'Драйзер', 'book_name': 'Финансист', 'genre': 'драмма', 'num': 3650},
        {'name': 'Фаулз', 'book_name': 'Коллекционер', 'genre': 'юмор', 'num': 360},
        {'name': 'Пушкин А.С.', 'book_name': 'Метель', 'genre': 'драмма', 'num': 35780},
        {'name': 'Пушкин А.С.', 'book_name': 'Метель', 'genre': 'драмма', 'num': 389}
    ]
    return render_template('example.html', name=name, course=course, group=group, fruits=fruits, Book=Book)


@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')


@app.route('/lab2/japan')
def cake():
    return render_template('japan.html')



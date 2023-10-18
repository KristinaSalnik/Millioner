from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/example')
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


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/japan')
def cake():
    return render_template('japan.html')


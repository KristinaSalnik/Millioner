from flask import redirect, render_template, request, Blueprint
import psycopg2

lab5 = Blueprint("lab5", name)

def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_Kris",
        user="Kristina_knowledge_base",
        password="123")
    
    return conn:

def dbConnect(Cursor, connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5')
def main():
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users;")

    result = cur.fetchall()

    print(result)

    dbClose(cur, conn)

    return "go to console"
from flask import Flask, render_template, request,redirect
import pymysql.cursors
from pprint import pprint as print

app = Flask(__name__)

conn = pymysql.connect(
    database="jspooner_todos" ,
    user="jspooner",
    password="243565207",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor,
)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form["todo"]
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO`todos`(`description`) VALUES ('{new_todo}') ")
        cursor.close()
        conn.commit()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `todos` ORDER BY `complete`")

    results = cursor.fetchall()
    cursor.close()
    return render_template("todo.html.jinja",todo=results )


@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index}")
    cursor.close()
    conn.commit()

    return redirect('/')

@app.route('/complete_todo/<int:todo_index>', methods=['POST'])
def complete_todo(todo_index):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE")
    cursor.close()
    conn.commit()

    return redirect('/')
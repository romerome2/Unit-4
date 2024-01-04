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
cursor = conn.cursor()

cursor.execute("SELECT`description` FROM `todos`")

results = cursor.fetchall()
print(results)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form["todo"]
        todo.append(new_todo)
    return render_template("todo.html.jinja",todo=todo )
todo = [
    "get money",
    "eat food"
]


@app.route('/delete_todo/<int:todo_index>', methods=['POST'])
def todo_delete(todo_index):
   del todo[todo_index]
   return redirect('/')
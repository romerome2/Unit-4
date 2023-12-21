from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['GET, Post'])
def index():
    new_todo = request.form["todo"]
    return render_template("todo.html.jinja",todo=todo )
todo = [
    "get money",
    "eat food"
]


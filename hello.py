from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html.jinja")

@app.route('/ping')
def  ping():
    return "<h1>Pong</h1>"

app.route('/hello/<name>')
def Name(name):
    return f"hello{name}"                                          
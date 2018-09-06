
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name="friend"):
    return render_template('hello.html', name = name)

@app.route('/stuff')
def list_page():
    stuff = ["Dogs", "Kids", "Wind", "Dust", "Towels"]
    return render_template('list.html', name = "Stuff", items = stuff, title = True)

@app.route('/form')
def form_page():
    return render_template('form.html')

@app.route('/post_list', methods=['POST'])
def post_list():
    mylist = [request.form['first'], request.form['second'], request.form['thrid']]
    return render_template('list.html', name = "My List", items = mylist, title = True)

@app.route('/bye')
def bye_world():
    return 'Bye from Flask!'
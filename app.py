from flask import Flask, render_template, request, url_for, redirect
import pymongo
from pymongo.server_api import ServerApi

app = Flask(__name__)
pa = False

if pa:
    client = pymongo.MongoClient(
        "mongodb+srv://jessevervaartns:JuFEqbPW6R0fNoj1@ns-bot-lim.t6tgwce.mongodb.net/?retryWrites=true&w=majority",
        server_api=ServerApi('1'), connectTimeoutMS=30000, socketTimeoutMS=None, connect=False, maxPoolsize=1)
else:
    client = pymongo.MongoClient(
        "mongodb+srv://jessevervaartns:JuFEqbPW6R0fNoj1@ns-bot-lim.t6tgwce.mongodb.net/?retryWrites=true&w=majority",
        server_api=ServerApi('1'))

db = client.test
todos = db.todos

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)


if __name__ == '__main__':
    app.run(host='192.168.2.14', port=60065, debug=True)

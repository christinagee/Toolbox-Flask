"""
Flask App Code - Christina Gee
"""
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        ninja = request.form['ninja']
        if (name != '' and age != '' and ninja != ''):
            return render_template('profile.html', name=name, age=age,
                                   ninja=ninja)

        else:
            return render_template('error.html')


if __name__ == '__main__':
    (app.run(debug=True))

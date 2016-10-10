from flask import Flask, request, render_template
'''
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='x' and password=='x':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad un or pw', username=username)

if __name__ == '__main__':
    app.run()
'''

app = Flask(__name__)
from app import views

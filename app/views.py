from flask import Flask
from flask import request, render_template
"""
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()
"""

from app import app
@app.route('/')
@app.route('/index')
def index():
    user={'nickname':'MMiguel'}
    #######事例#######
    #return '''
    #<html>
    #<head>
    #    <title>home</title>
    #</head>
    #<body>
    #    <h1>hi,''' + user['nickname'] + '''</h1>
    #</body>
    #</html>
    #'''
    posts = [
        {
            'author': {'nickname': 'MMiguel'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The movie was so cool!'
        }
    ]
    return render_template('index1.html',
                           title = 'Home-xhy',
                           user = user,
                           posts = posts)
from flask import *
from flask import render_template
from app.db.createDB import createTable, exec, execSelect
from datetime import datetime

def create_app(app_env=None):
    flask_app = Flask(__name__)
    createTable()
    return flask_app

def passwordToMD5(password):
        import hashlib
        if password == None:
            return None
        else:
            m = hashlib.md5(password.encode(encoding='utf-8'))
            return m.hexdigest()


app = create_app()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("index.html")
    username = request.form['username']
    password = request.form['password']
    md5Password = passwordToMD5(password)
    result = execSelect(f'''SELECT Password FROM UserAccounts WHERE UserName = '{username}' ''')
    if(len(result) == 0):
        return render_template("index.html", error="username or password error")
    else:
        if(md5Password == result[0][0]):
            print('login success')
            return redirect(url_for("index"))
        else:
            return render_template("index.html", error="username or password error")
        


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    username = request.form['username']
    password = request.form['password']
    md5Password = passwordToMD5(password)
    result = execSelect(f'''SELECT UserName FROM UserAccounts WHERE UserName = '{username}' ''')
    if(len(result) > 0):
        return render_template("register.html", error="username duplicate")
    else:
        exec(f''' INSERT INTO UserAccounts (UserName, Password, CreateDate, ModifiedDate) VALUES ('{username}', '{md5Password}', '{datetime.now()}', '{datetime.now()}')''')
        return redirect(url_for("index"))



# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "<h1>Hello, Nouman!</h1>"

# @app.route('/user/<name>')
# def user(name):
# 	return '<h1>Hello, {0}!</h1>'.format(name)

# if __name__ == '__main__':
#     app.run(debug=True,host="0.0.0.0")



from flask import Flask
from flask_sqlalchemy import SQLAlchemy #from flask.ext.sqlalchemy import SQLAlchemy
import os,socket

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
db = SQLAlchemy(app)
hostname = socket.gethostname() 

@app.route('/')
def index():
    return 'Hello, World' #%s!\n' % hostname

@app.route('/db')
def dbtest():
    try:
        db.create_all()
    except Exception as e:
        return e.message + '\n'
    return 'Database Connected from %s!\n' % hostname 

if __name__ == '__main__':
     app.run(debug=True,host="0.0.0.0")
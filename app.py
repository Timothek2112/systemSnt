from flask import Flask
from flask import request
import mysql.connector
from mysql.connector import Error
import pymysql



app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/query')

def query():
    language = request.args.get('language')
    return language


if __name__ == '__main__':
    app.run(debug=True,port= 5000)
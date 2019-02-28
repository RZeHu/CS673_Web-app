#!/bin/env python
from flask.ext.mysql import MySQL
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'cs673'
app.config['MYSQL_DATABASE_PASSWORD'] = 'cs673password'
app.config['MYSQL_DATABASE_DB'] = 'cs673'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

conn = mysql.connect()
cursor =conn.cursor()

from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)

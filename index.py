from flask import Flask
from flask import jsonify
from flask import g
from flask import render_template
import random
from flask_mysqldb import MySQL


DATABASE = 'database.db'

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "test"
app.config['JSON_AS_ASCII'] = False

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/n3')
def render_n3_page():
    return render_template('n3.html')

@app.route('/question/<level>')
def get_question(level='1'):
    cur = mysql.connection.cursor()
    command = 'select distinct(q.id), q.question, o.option, q.answer, q.reason, o.id from question q left join options o on q.id = o.question_id where level = "{}" order by rand()'.format(level)
    print command
    cur.execute(command)
    rows = cur.fetchall()
    data = {}
    data["id"] = rows[0][0]
    data["question"] = rows[0][1]
    data["answer"] = rows[0][3]
    data["reason"] = rows[0][4]
    data["options"] = []
    for row in rows:
        data["options"].append({'option': row[2], 'id': row[5]})
    return jsonify(data)

#@app.route('/question/<id>')
#def post_answer(is_correct=None):
    #Store


if __name__ == '__main__':
    app.run()

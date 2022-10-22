from flask import Flask, render_template, request

import pymssql

app = Flask(__name__, template_folder='templates', static_folder='templates/layui')


@app.route('/')
def index():
    return render_template('studentlogin.html')


def databasequery(query):
    db = pymssql.connect(host="LocalHost", user="mysql", password='88888888', database="AdventureWorks2019")
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchone()
    db.close()
    return data


@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        student_name = request.args.get('student_name')
        # studentlist = []
        # studentlist.append(student_name)
        # return render_template('quiz.html', data=student_name)
        return render_template('quiz.html', data=student_name)


@app.route('/query', methods=['GET', 'POST'])
def studentqueryenter():
    if request.method == 'GET':
        student_query = request.args.get('student_query')
        datafromdatabase = databasequery(student_query)
        return render_template('result.html', data=datafromdatabase)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

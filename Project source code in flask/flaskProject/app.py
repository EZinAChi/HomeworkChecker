from flask import Flask, render_template, request

import pymssql

app = Flask(__name__, template_folder='templates', static_folder='templates/layui')


@app.route('/')
def index():
    studentqueryenter()
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

        return render_template('quiz.html', data=student_name)


@app.route('/query', methods=['GET', 'POST'])
def studentqueryenter():
    if request.method == 'GET':
        student_query = request.args.get('student_query')
        datafromdatabase1 = databasequery("SELECT * FROM Person.address")
        datafromdatabase2 = databasequery(student_query)

        return render_template('result.html', data=compareresult(datafromdatabase1, datafromdatabase2))

def compareresult(query1, query2):
    if query1 == query2:
        return 1
    else:
        return 0



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

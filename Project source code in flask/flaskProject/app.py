from flask import Flask, render_template, request

import pymssql
from pymssql import Answer, Deduction, Feedback, Practical, Question, Result, Students, Teacher

app = Flask(__name__, template_folder='templates', static_folder='templates/layui')


@app.route('/')
def index():
    return render_template('menu.html')


# The function to link the database and to count the number of item outputted
def countqueryitems(query):
    db = pymssql.connect(host="LocalHost", user="mysql", password='88888888', database="AdventureWorks2019")
    cursor = db.cursor()
    cursor.execute(query)
    # data = cursor.fetchone()
    data = cursor.fetchall()
    q = 0
    for queryitem in data:
        q += 1
    db.close()
    # return data
    return q


# route to port /studentlogin for pulling studentlogin page to front end
@app.route('/studentlogin')
def studentlogin():
    return render_template('studentlogin.html')

@app.route('/teacherlogin')
def teacherlogin():
    return render_template('teacherlogin.html')


# route to port /student for transferring student_name from studentlogin page and pulling quiz page to front end
@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        student_name = request.args.get('student_name')

        return render_template('quiz.html', data=student_name)

# route to port /student for transferring student_name from studentlogin page and pulling quiz page to front end
@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == 'GET':
        teacher_name = request.args.get('teacher_name')

        return render_template('quizmanage.html')


# route to port /query for transferring student_query from quiz page and calculate the mark
@app.route('/query', methods=['GET', 'POST'])
def studentqueryenter():
    if request.method == 'GET':
        student_query = request.args.get('student_query')
        datafromdatabase1 = countqueryitems(
            "SELECT COUNT(*) AS transCount, SUM(Quantity) AS avgQuantity,  AVG(ActualCost) AS avgCost FROM Production.TransactionHistoryArchive")
        datafromdatabase2 = countqueryitems(student_query)

# print for testing
        print(datafromdatabase1)
        print(datafromdatabase2)
        print(student_query)

        return render_template('result.html', data=compareresult(datafromdatabase1, datafromdatabase2))

# calculate the mark
def compareresult(query1, query2):
    if query1 == query2:
        return 1
    else:
        return 0

#  connect to main database
def connectHWCdb():
    db = pymssql.connect(host="LocalHost", user="mysql", password='88888888', database="HomeworkChecker")
    return db

#  insert data to Students table
def insertstudent(studentid, email, password, firstName, lastName):

    db = connectHWCdb()

    label = ['studentID', 'email', 'password', 'firstName', 'lastName']
    content = [studentid, email, password, firstName, lastName]

    sql = 'insert into {0} ({1},{2},{3},{4}) values({5},"{6}","{7}","{8}","{9}")'.format(Students,label[0],label[1],
          label[2],label[3],label[4],content[0],content[1],content[2],content[3],content[4])
    result = db.execute(sql)
    db.commit()
    return  True if result else False

#  insert data to Result table
def insertresult(studentid, questionid, totalmark):

    db = connectHWCdb()

    label = ['studentID', 'questionID', 'totalMark']
    content = [studentid, questionid, totalmark]

    sql = 'insert into {0} ({1},{2}) values({3},"{4}","{5}")'.format(Result,label[0],label[1],
          label[2],label[3],label[4],content[0],content[1],content[2],content[3],content[4])
    result = db.execute(sql)
    db.commit()
    return  True if result else False

#  read data from Students table
def readstudent():

    db = connectHWCdb()

    sql = 'select * from {0}'.format(Students)
    result = db.execute(sql)
    return list(result)

#  run the main program
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

from flask import Flask, render_template, request

import pymssql

app = Flask(__name__, template_folder='templates', static_folder='templates/layui')


@app.route('/')
def index():
    #  test connection:
    print(connectHWCdb())
    print(connectAWdb())

    #  access main menu
    return render_template('menu.html')


#  connect to main database
def connectHWCdb():
    db = pymssql.connect(host="LocalHost", user="mysql", password='88888888', database="HWC")
    cursor = db.cursor()
    return cursor

#  connect to target database
def connectAWdb():
    db = pymssql.connect(host="LocalHost", user="mysql", password='88888888', database="AdventureWorks2019")
    cursor = db.cursor()
    return cursor


# route to port /studentlogin for pulling studentlogin page to front end
@app.route('/studentlogin')
def studentloginpage():
    return render_template('studentlogin.html')


# route to port /teacher for pulling teacherlogin page to front end
@app.route('/teacherlogin')
def teacherloginpage():
    return render_template('teacherlogin.html')


# route to port /student for transferring student_name from studentlogin page and pulling quiz page to front end
@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        student_email = request.args.get('student_email')
        student_password = request.args.get('student_password')

        print(student_email, student_password)
        print(passwordcheck(student_email, student_password))

        if passwordcheck(student_email, student_password):
            return render_template('quiz.html')
        else:
            return render_template('studentlogin.html', data=True)


def passwordcheck(email, password):
    db = connectHWCdb()
    sql = "select {0} from {1} WHERE email = '{2}'".format("password", "Student", email)
    result = db.execute(sql)

    print(result)

    if password == result:
        return True
    else:
        return False


# route to port /teacher for transferring student_name from studentlogin page and pulling quiz page to front end
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


# Marking
# The function to link the database and to count the number of item outputted
def countqueryitems(query):
    cursor = connectAWdb()
    cursor.execute(query)
    # if need the first item code: data = cursor.fetchone(), if need all item, code: data = cursor.fetchall()
    data = cursor.fetchall()
    q = 0
    for queryitem in data:
        q += 1
    db.close()
    # return data
    return q


# calculate the mark
def compareresult(query1, query2):
    if query1 == query2:
        return 1
    else:
        return 0


#  insert data to Students table
def insertstudent(studentid, email, password, firstName, lastName):
    db = connectHWCdb()

    label = ['studentID', 'email', 'password', 'firstName', 'lastName']
    content = [studentid, email, password, firstName, lastName]

    sql = 'insert into {0} ({1},{2},{3},{4}) values({5},"{6}","{7}","{8}","{9}")'.format("Students", label[0], label[1],
                                                                                         label[2], label[3], label[4],
                                                                                         content[0], content[1],
                                                                                         content[2], content[3],
                                                                                         content[4])
    result = db.execute(sql)
    db.commit()
    return True if result else False


#  read data from Students table
def readstudent():
    db = connectHWCdb()

    sql = 'select * from {0}'.format("Students")
    result = db.execute(sql)
    return list(result)


#  update student data
def updatestudent(studentid, email, password, firstName, lastName):
    db = connectHWCdb()

    label = ['studentID', 'email', 'password', 'firstName', 'lastName']
    content = [studentid, email, password, firstName, lastName]

    sql = 'update Students set {0} ({1},{2},{3},{4}) values({5},"{6}","{7}","{8}","{9}" where studentID = {10})'.format(
        label[0], label[1],
        label[2], label[3], label[4],
        content[0], content[1],
        content[2], content[3],
        content[4], label[0])
    result = db.execute(sql)
    db.commit()
    return True if result else False


#  insert data to Result table
def insertresult(studentid, questionid, totalmark):
    db = connectHWCdb()

    label = ['studentID', 'questionID', 'totalMark']
    content = [studentid, questionid, totalmark]

    sql = 'insert into {0} ({1},{2}) values({3},"{4}","{5}")'.format("Result", label[0], label[1],
                                                                     label[2], label[3], label[4], content[0],
                                                                     content[1], content[2], content[3], content[4])
    result = db.execute(sql)
    db.commit()
    return True if result else False


#  read data from Question table
def readquestion(prac_num):
    db = connectHWCdb()

    sql = 'select {0} from {1} where {2}'.format("question", "Question", "questionID =")
    result = db.execute(sql)
    return list(result)


@app.route('/practical', methods=['GET', 'POST'])
def practicalsection():
    if request.method == 'GET':
        prac_num = request.args.get('pracnum')

    if prac_num == 1:
        return render_template('quiz.html', )


#  run the main program
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

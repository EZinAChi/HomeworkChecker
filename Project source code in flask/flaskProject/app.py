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


#  Database connection
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


#  Page transaction
#  route to port /studentlogin for pulling studentlogin page to front end
@app.route('/studentlogin')
def studentloginpage():
    return render_template('studentlogin.html')


#  route to port /teacher for pulling teacherlogin page to front end
@app.route('/teacherlogin')
def teacherloginpage():
    return render_template('teacherlogin.html')


# @app.route('/quiz', methods=['GET', 'POST'])
# def movebacktoselec():
#     back = request.args.get('back')
#     if back == 1:
#         return render_template('quizselection.html')


#  route to port /practical for pulling correct quiz page to front end
@app.route('/quiz', methods=['GET', 'POST'])
def practicalsection():
    if request.method == 'GET':
        quiz_num = request.args.get('qnum')

    if int(quiz_num) == 1:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        quiz_num = 1
        return render_template('quiz.html', quiz_num=quiz_num, q1=str(q1)[2:-3], q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3])
    elif int(quiz_num) == 6:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        quiz_num = 2
        return render_template('quiz.html', quiz_num=quiz_num, q1=str(q1)[2:-3], q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3])
        return render_template('quizselection.html', data=0)
    elif int(quiz_num) == 11:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        quiz_num = 3
        return render_template('quiz.html', quiz_num=quiz_num, q1=str(q1)[2:-3], q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3])
        return render_template('quizselection.html', data=0)
    elif int(quiz_num) == 16:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        quiz_num = 4
        return render_template('quiz.html', quiz_num=quiz_num, q1=str(q1)[2:-3], q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3])

    elif int(quiz_num) == 21:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        quiz_num = 5
        return render_template('quiz.html', quiz_num=quiz_num, q1=str(q1)[2:-3], q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3])

    return render_template('quizselection.html')


#  select the question quiz required
def selectquestion(qnum):
    db = connectHWCdb()
    sql = "select question from Question where questionID = {}".format(qnum)
    try:
        db.execute(sql)
        return db.fetchall()[0]
    except Exception as e:
        return "##No Question###"


#  Login
#  route to port /student for transferring student login data from studentlogin page and do password checking
@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        student_email = request.args.get('student_email')
        student_password = request.args.get('student_password')

        # testing
        print(student_email, student_password)
        print(passwordcheck(student_email, student_password, "Student"))

        if passwordcheck(student_email, student_password, "Student"):
            return render_template('quizselection.html')
        else:
            return render_template('studentlogin.html', data=True)


#  route to port /teacher for transferring teacher login data from teacherlogin page and do password checking
@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == 'GET':
        teacher_email = request.args.get('teacher_email')
        teacher_password = request.args.get('teacher_password')

        # testing
        print(teacher_email, teacher_password)
        print(passwordcheck(teacher_email, teacher_password, "Teacher"))

        if passwordcheck(teacher_email, teacher_password, "Teacher"):
            return render_template('quiz.html')
        else:
            return render_template('teacherlogin.html', data=True)


#  check if password correct and if user exist
def passwordcheck(email, password, user):
    db = connectHWCdb()

    sql = "select 1 from {} where email='{}' and password='{}'".format(user, email, password)
    db.execute(sql)
    if db.fetchall():
        return True
    else:
        return False


#  Quiz
#  route to port /query for transferring student_query from quiz page and calculate the mark
@app.route('/query', methods=['GET', 'POST'])
def studentqueryenter():
    if request.method == 'GET':
        student_query1 = request.args.get('student_query1')
        student_query2 = request.args.get('student_query2')
        student_query3 = request.args.get('student_query3')
        student_query4 = request.args.get('student_query4')
        student_query5 = request.args.get('student_query5')
        querylist = [student_query1, student_query2, student_query3, student_query4, student_query5]

        i = 1
        for i in 5:
            querylist[i - 1]
        datafromdatabase1 = countqueryitems(
            "SELECT COUNT(*) AS transCount, SUM(Quantity) AS avgQuantity,  AVG(ActualCost) AS avgCost FROM Production.TransactionHistoryArchive")
        datafromdatabase2 = countqueryitems(student_query)

        # print for testing
        print(datafromdatabase1)
        print(datafromdatabase2)

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
def insertresult(studentID, quizID, totalmark, feedBack):
    db = connectHWCdb()

    label = ['studentID', 'quizID', 'totalmark', feedBack]
    content = [studentID, quizID, totalmark, feedBack]

    sql = 'insert into {0},{1},{2},{3} values({4},{5},{6},{7})'.format("Result", label[0], label[1],
                                                                       label[2], label[3], content[0],
                                                                       content[1], content[2], content[3])
    result = db.execute(sql)
    db.commit()
    return True if result else False


#  read data from Question table
def readquestion(prac_num):
    db = connectHWCdb()

    sql = 'select {0} from {1} where {2}'.format("question", "Question", "questionID =")
    result = db.execute(sql)
    return list(result)


#  run the main program
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

# request.json.get
# make_response(json_encode(data), http_code,
#       {'Content-Type': 'application/json; charset=utf-8'})

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
    return cursor, db


#  connect to target database
def connectAWdb():
    db = pymssql.connect(host="LocalHost", user="mysql", password='88888888', database="AdventureWorks2019")
    cursor = db.cursor()
    return cursor, db


#  Page transaction
#  route to port /studentlogin for pulling studentlogin page to front end
@app.route('/studentlogin')
def studentloginpage():
    return render_template('studentlogin.html')


#  route to port /teacher for pulling teacherlogin page to front end
@app.route('/teacherlogin')
def teacherloginpage():
    return render_template('teacherlogin.html')


#  route to port /quizmanage for pulling quizselection page to front end
@app.route('/quizmanage')
def quizmanagepage():
    return render_template('quizselection.html', data=10001)


#  route to port /quizmanage/manage for pulling quizselection page to front end
@app.route('/quizmanagepage', methods=['GET', 'POST'])
def quizmanage():
    qnum = request.args.get("qnum")
    return render_template('quizmanage.html', qnum=qnum)


@app.route('/menu')
def menupage():
    return render_template('menu.html')


#  route to port /practical for pulling correct quiz page to front end
@app.route('/quiz', methods=['GET', 'POST'])
def practicalsection():
    if request.method == 'GET':
        quiz_num = request.args.get('qnum')
        email = request.args.get('email')

    if int(quiz_num) == 1:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        question_num = int(quiz_num)
        quiz_num = 1
        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(question_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, q1=str(q1)[2:-3],
                               q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3], email=email)
    elif int(quiz_num) == 6:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        question_num = int(quiz_num)
        quiz_num = 2

        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(question_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, q1=str(q1)[2:-3],
                               q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3], email=email)
    elif int(quiz_num) == 11:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        question_num = int(quiz_num)
        quiz_num = 3

        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(question_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, q1=str(q1)[2:-3],
                               q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3], email=email)
    elif int(quiz_num) == 16:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        question_num = int(quiz_num)
        quiz_num = 4

        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(question_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, q1=str(q1)[2:-3],
                               q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3], email=email)

    elif int(quiz_num) == 21:
        q1 = selectquestion(int(quiz_num))
        q2 = selectquestion(int(quiz_num) + 1)
        q3 = selectquestion(int(quiz_num) + 2)
        q4 = selectquestion(int(quiz_num) + 3)
        q5 = selectquestion(int(quiz_num) + 4)

        question_num = int(quiz_num)
        quiz_num = 5

        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(question_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, q1=str(q1)[2:-3],
                               q2=str(q2)[2:-3],
                               q3=str(q3)[2:-3], q4=str(q4)[2:-3], q5=str(q5)[2:-3], email=email)

    return render_template('quizselection.html')


#  select the question quiz required
def selectquestion(qnum):
    cursor, db = connectHWCdb()
    sql = "select question from Question where questionID = {}".format(qnum)
    try:
        cursor.execute(sql)
        return cursor.fetchall()[0]
    except Exception as e:
        return "##No Question###"

@app.route('/saveQuestion', methods=['GET', 'POST'])
def saveQuestion():

    qnum = request.args.get('qnum')

    q1 = request.args.get('q1')
    q2 = request.args.get('q2')
    q3 = request.args.get('q3')
    q4 = request.args.get('q4')
    q5 = request.args.get('q5')

    qa1 = request.args.get('qa1')
    qa2 = request.args.get('qa2')
    qa3 = request.args.get('qa3')
    qa4 = request.args.get('qa4')
    qa5 = request.args.get('qa5')

    qList = [q1, q2, q3, q4, q5]
    qaList = [qa1, qa2, qa3, qa4, qa5]
    print(qList)

    for i in range(5):
        if quizOpencheck(qnum+i):
            print(quizOpencheck(qnum+i))
            print(insertQuestion(qnum+i, qList[i], qaList[i]))

        else:
            print(updateQuestion(qnum+i, qList[i], qaList[i]))

    return render_template('quizselection.html', qnum=qnum)



#  Login
#  route to port /student for transferring student login data from studentlogin page and do password checking
@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        student_email = request.args.get('student_email')
        student_password = request.args.get('student_password')

        # testing
        print(passwordCheck(student_email, student_password, "Student"))

        if passwordCheck(student_email, student_password, "Student"):
            return render_template('quizselection.html', data=10000, email=student_email)
        else:
            return render_template('studentlogin.html', data=10002)


#  route to port /teacher for transferring teacher login data from teacherlogin page and do password checking
@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if request.method == 'GET':
        teacher_email = request.args.get('teacher_email')
        teacher_password = request.args.get('teacher_password')

        # testing
        print(passwordCheck(teacher_email, teacher_password, "Teacher"))

        if passwordCheck(teacher_email, teacher_password, "Teacher"):
            return quizmanagepage()
        else:
            return render_template('teacherlogin.html', data=10003)


#  check if password correct and if user exist
def passwordCheck(email, password, user):
    cursor, db = connectHWCdb()

    sql = "select 1 from {} where email='{}' and password='{}'".format(user, email, password)
    cursor.execute(sql)
    if cursor.fetchall():
        return True
    else:
        return False


#  Quiz
#  route to port /query for transferring student_query from quiz page and calculate the mark
@app.route('/query', methods=['GET', 'POST'])
def studentQueryenter():
    if request.method == 'GET':
        student_query1 = request.args.get('student_query1')
        student_query2 = request.args.get('student_query2')
        student_query3 = request.args.get('student_query3')
        student_query4 = request.args.get('student_query4')
        student_query5 = request.args.get('student_query5')
        question_num = request.args.get('question_num')
        quiz_num = request.args.get('quiz_num')
        student_email = request.args.get('email')

        querylist = [student_query1, student_query2, student_query3, student_query4, student_query5]

        question_num = int(question_num)
        quiz_num = int(quiz_num)

        totalmark = 0
        for i in range(5):
            datafromdatabase1 = countQueryitems(selectSampleAnswer(question_num + i))
            print(datafromdatabase1)

            datafromdatabase2 = countQueryitems(querylist[i])
            print(datafromdatabase2)

            totalmark += compareResult(datafromdatabase1, datafromdatabase2)
            insertAnswer(question_num + i, readstudentID(student_email), querylist[i],
                         compareResult(datafromdatabase1, datafromdatabase2))

        insertResult(readstudentID(student_email), quiz_num, totalmark, 'no feedback')
        # print for testing
        #     print(datafromdatabase1)
        #     print(datafromdatabase2)

        return render_template('result.html', data=totalmark)


def selectSampleAnswer(qnum):
    cursor, db = connectHWCdb()
    sql = "select answer from Question where questionID='{}'".format(qnum)
    try:
        cursor.execute(sql)
        result = str(cursor.fetchall()[0])[2:-4]
        # print(result)
        return result
    except Exception as e:
        return "##No Answer###"

    # cursor.execute(sql)
    # result = cursor.fetchall()[0][0]
    # print(result)
    # return result


# Marking
# The function to link the database and to count the number of item outputted
def countQueryitems(query):
    cursor, db = connectAWdb()
    try:
        cursor.execute(query)
        # if need the first item code: data = cursor.fetchone(), if need all item, code: data = cursor.fetchall()
        data = cursor.fetchall()
        # print(data)
        q = 0
        for queryitem in data:
            q += 1
        # return data
        return q
    except Exception as e:
        return 0

    # testing
    # print(query)
    # cursor.execute(query)
    # data = cursor.fetchall()
    # q = 0
    # for queryitem in data:
    #     q += 1
    # return q


# calculate the mark
def compareResult(query1, query2):
    if query1 == query2 & query1 != '':
        return 1
    else:
        return 0


def readstudentID(email):
    cursor, db = connectHWCdb()

    sql = "select * from {} where email='{}'".format("Student", email)

    cursor.execute(sql)
    result = cursor.fetchall()[0][0]
    return result


def quizFinishcheck(id, quiz_num):
    cursor, db = connectHWCdb()

    sql = "select 1 from Result where studentID='{}' and quizID='{}'".format(id, quiz_num)
    cursor.execute(sql)
    if cursor.fetchall():
        return True
    else:
        return False


def quizOpencheck(qnum):
    cursor, db = connectHWCdb()

    sql = "select 1 from Question where questionID='{}'".format(qnum)
    cursor.execute(sql)
    if cursor.fetchall():
        return False
    else:
        return True


def checkString(str):
    returnStr = ""
    try:
        if str.index("'") != -1:
            returnStr = str.replace("'", "''")
            str = returnStr

        return str
    except Exception as e:
        return str


#  insert data to Answer table
def insertAnswer(questionID, studentID, answer, mark):
    cursor, db = connectHWCdb()

    label = ['questionID', 'studentID', 'answer', 'mark']
    content = [questionID, studentID, answer, mark]

    sql = "insert into Answer ({0},{1},{2},{3}) values({4},{5},'{6}',{7})".format(label[0], label[1],
                                                                                  label[2], label[3], content[0],
                                                                                  content[1], checkString(content[2]),
                                                                                  content[3])
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


# insert data to Result table
def insertResult(studentID, quizID, totalmark, feedback):
    label = ['studentID', 'quizID', 'totalmark', 'feedback']
    content = [studentID, quizID, totalmark, feedback]

    sql = "insert into Result ({0},{1},{2},{3}) values({4},{5},{6},'{7}')".format(label[0], label[1],
                                                                                  label[2], label[3],
                                                                                  content[0], content[1],
                                                                                  content[2], content[3])
    cursor, db = connectHWCdb()
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


def insertQuestion(questionID, question, answer):
    cursor, db = connectHWCdb()

    label = ['questionID', 'question', 'answer']
    content = [questionID, question, answer]

    sql = 'insert into Question ({0},{1},{2}) values({3},"{4}","{5}" where studentID = {6})'.format(
        label[0], label[1],
        label[2], content[0], content[1],
        content[2], content[0])
    print(sql)
    result = cursor.execute(sql)
    db.commit()
    return True if result else False

#  insert data to Students table
def insertStudent(studentid, email, password, firstName, lastName):
    cursor, db = connectHWCdb()

    label = ['studentID', 'email', 'password', 'firstName', 'lastName']
    content = [studentid, email, password, firstName, lastName]

    sql = 'insert into {0} ({1},{2},{3},{4}) values({5},"{6}","{7}","{8}","{9}")'.format("Students", label[0], label[1],
                                                                                         label[2], label[3], label[4],
                                                                                         content[0], content[1],
                                                                                         content[2], content[3],
                                                                                         content[4])
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


def updateQuestion(questionID, question, answer):
    cursor, db = connectHWCdb()

    label = ['questionID', 'question', 'answer']
    content = [questionID, question, answer]

    sql = 'update Question set ({0},{1},{2}) values({3},"{4}","{5}" where studentID = {6})'.format(
        label[0], label[1],
        label[2], content[0], content[1],
        content[2], content[0])
    print(sql)
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


#  update student data
def updatestudent(studentid, email, password, firstName, lastName):
    cursor, db = connectHWCdb()

    label = ['studentID', 'email', 'password', 'firstName', 'lastName']
    content = [studentid, email, password, firstName, lastName]

    sql = 'update Students set {0} ({1},{2},{3},{4}) values({5},"{6}","{7}","{8}","{9}" where studentID = {10})'.format(
        label[0], label[1],
        label[2], label[3], label[4],
        content[0], content[1],
        content[2], content[3],
        content[4], label[0])
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


#  read data from Question table
def readquestion(quiz_num):
    cursor, db = connectHWCdb()

    sql = 'select {0} from {1} where {2}'.format("question", "Question", "questionID =")
    result = cursor.execute(sql)
    return list(result)


#  read data from Students table
def readstudent():
    cursor, db = connectHWCdb()

    sql = 'select * from {0}'.format("Students")
    result = cursor.execute(sql)
    return list(result)


#  run the main program
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

# request.json.get
# make_response(json_encode(data), http_code,
#       {'Content-Type': 'application/json; charset=utf-8'})

import json

from flask import Flask, render_template, request, jsonify, make_response

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
    try:
        cursor = db.cursor()
        return cursor, db
    except Exception as e:
        return "database not exist"


#  connect to target database
def connectAWdb():
    db = pymssql.connect(host="LocalHost", user="mysql", password='88888888', database="AdventureWorks2019")
    try:
        cursor = db.cursor()
        return cursor, db
    except Exception as e:
        return "database not exist"


#  Page transaction
#  route to port /menu for pulling main menu page to front end
@app.route('/menu')
def menuPage():
    return render_template('menu.html')


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
def quizManagepage():
    return render_template('quizselection.html', data=10001)


#  route to port /quizmanage/manage for pulling quizselection page to front end
@app.route('/quizmanagepage', methods=['GET', 'POST'])
def quizManage():
    qnum = request.args.get("qnum")
    return render_template('quizmanage.html', qnum=qnum, size=readQuizSize(qnum))


@app.route('/seeResult')
def seeResultPage():
    if request.method == 'GET':
        teacher_email = request.args.get('teacher_email')
        teacher_password = request.args.get('teacher_password')

        # testing
        # print(passwordCheck(teacher_email, teacher_password, "Teacher"))
        rList = readStudentResultList(readStudentList())
        if passwordCheck(teacher_email, teacher_password, "Teacher"):
            return render_template('studentResult.html', rList=rList)
        else:
            return render_template('teacherlogin.html', data=10003)


#  route to port /feedback for pulling resultTeacher page to front end
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    sID = request.args.get('studentID')
    qID = request.args.get('quizID')
    name = request.args.get('studentName')
    aList, mList = readStudentAnswernMarkList(sID, qID)
    totalMark = readTotalMark(sID, qID)
    size = readQuizSize(qID)
    feedback = readFeedback(sID, qID)
    qnList = []
    for i in range(readQuizSize(qID)):
        qnList.append(i + 1)
    return render_template('feedback.html', qList=readQuestion(qID), aList=aList, mList=mList, totalMark=totalMark,
                           qnList=qnList, name=name, size=size, feedback=feedback, sID=sID, qID=qID)


#  route to port /practical for pulling correct quiz page to front end
@app.route('/quiz', methods=['GET', 'POST'])
def quizSection():
    if request.method == 'GET':
        quiz_num = int(request.args.get('qnum'))
        email = request.args.get('email')

    if quiz_num == 1:
        question = selectquestion(quiz_num)
        size = readQuizSize(quiz_num)
        question_num = []
        for i in range(size):
            question_num.append(i + 1)

        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(quiz_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, email=email,
                               question=question)


    elif quiz_num == 2:
        question = selectquestion(quiz_num)
        size = readQuizSize(quiz_num)
        question_num = []
        for i in range(size):
            question_num.append(i + 1)

        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(quiz_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, email=email,
                               question=question)


    elif quiz_num == 3:
        question = selectquestion(quiz_num)
        size = readQuizSize(quiz_num)
        question_num = []
        for i in range(size):
            question_num.append(i + 1)

        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(quiz_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, email=email,
                               question=question)


    elif quiz_num == 4:
        question = selectquestion(quiz_num)
        size = readQuizSize(quiz_num)
        question_num = []
        for i in range(size):
            question_num.append(i + 1)

        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(quiz_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, email=email,
                               question=question)


    elif quiz_num == 5:
        question = selectquestion(quiz_num)
        size = readQuizSize(quiz_num)
        question_num = []
        for i in range(size):
            question_num.append(i + 1)

        if (quizFinishcheck(readstudentID(email), quiz_num)):
            return render_template('quizselection.html', message='You have finished this', data=10000, email=email)

        if (quizOpencheck(quiz_num)):
            return render_template('quizselection.html', message='Quiz not yet open', data=10000, email=email)

        return render_template('quiz.html', quiz_num=quiz_num, question_num=question_num, email=email,
                               question=question)

    return render_template('quizselection.html')


#  Function in quiz
#  route to port /checkQuery for displaying query result on quiz page
@app.route('/checkQuery', methods=['GET', 'POST'])
def checkQuery():
    sql = request.args.get('query')

    cursor, db = connectAWdb()
    data = []
    try:
        cursor.execute(sql)
        result = cursor.fetchall()

        for res in result:
            data.append(str(res))
    except Exception as e:

        return make_response((
            json.dumps({"status": 10001, "data": []}),
            200,
            {'Content-Type': 'application/json; charset=utf-8'}
        ))
    return make_response((
        json.dumps({"status": 10000, "data": data}),
        200,
        {'Content-Type': 'application/json; charset=utf-8'}
    ))


#   Function in feedback
#   save the feedback teacher enter for a quiz
@app.route('/saveFeedback', methods=['GET', 'POST'])
def saveFeedback():
    feedback = request.args.get('feedback')
    tMark = request.args.get('totalMark')
    sID = request.args.get('sID')
    qID = request.args.get('qID')
    saveFeedbacknMarktoDb(feedback, tMark, sID, qID)
    rList = readStudentResultList(readStudentList())
    return render_template('studentResult.html', rList=rList)



def saveFeedbacknMarktoDb(feedback, tMark, sID, qID):

    cursor, db = connectHWCdb()
    sql = "update Result set totalmark = {} ,feedback = '{}' where quizID = {} and studentID = {}".format(tMark, checkString(feedback), qID, sID)
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


def readFeedback(studentID, quizID):
    cursor, db = connectHWCdb()

    sql = "select * from Result where studentID = {} and quizID = {}".format(studentID, quizID)

    cursor.execute(sql)
    result = cursor.fetchall()

    return result[0][3]



#   Fuction in quiz management
#   refresh the quiz manage page regarding the size teacher selected
@app.route('/selectQuizSize', methods=['GET', 'POST'])
def selectQuizSize():
    size = request.args.get('selected')
    qnum = request.args.get('qnum')
    size = int(size)

    qList = []

    for i in range(size):
        if i != 0:
            qList.append(i)
            i += 1
    qList.append(i)
    return render_template('quizmanage.html', qnum=qnum, qList=qList, size=size)


#   save the quiz size teacher selected
def updateQuizSize(quizID, quizSize):
    cursor, db = connectHWCdb()

    label = ['quizID', 'quizSize']
    content = [quizID, quizSize]

    sql = 'update Quiz set {0} = {1} where quizID = {2}'.format(
        label[1], content[1], content[0])
    print(sql)
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


#   read the quiz size teacher selected
def readQuizSize(quizID):
    cursor, db = connectHWCdb()

    sql = "select * from {} where quizID='{}'".format("Quiz", quizID)

    cursor.execute(sql)
    result = cursor.fetchall()[0][1]
    return result


#  select the question quiz required
def selectquestion(quizID):
    cursor, db = connectHWCdb()
    sql = "select * from Question where quizID = {}".format(quizID)
    try:
        cursor.execute(sql)
        rList = []
        result = cursor.fetchall()
        for i in range(readQuizSize(quizID)):
            rList.append(str(result[i][1]))
        return rList
    except Exception as e:
        return rList


@app.route('/savequestion', methods=['GET', 'POST'])
def saveQuestion():
    qList = toList(request.args.get('qList'))
    qaList = toList(request.args.get('qaList'))
    size = request.args.get('size')
    quizID = request.args.get('qnum')

    updateQuizSize(quizID, size)

    deleteQuiz(quizID)
    for i in range(int(size)):
        insertQuestion(i + 1, qList[i], qaList[i], quizID)
    return quizManagepage()


#  Login
#  route to port /student for transferring student login data from studentlogin page and do password checking
@app.route('/student', methods=['GET', 'POST'])
def studentLogin():
    if request.method == 'GET':
        student_email = request.args.get('student_email')
        student_password = request.args.get('student_password')

        if passwordCheck(student_email, student_password, "Student"):
            return render_template('quizselection.html', data=10000, email=student_email)
        else:
            return render_template('studentlogin.html', data=10002)


@app.route('/studentSignin')
def studentSignin():
    return render_template('studentSignin.html')

@app.route('/studentSign', methods=['GET', 'POST'])
def studentSign():
    student_name = request.args.get('student_name')
    student_email = request.args.get('student_email')
    student_password = request.args.get('student_password')
    if studenSignedCheck(student_name, student_email):
        return render_template('studentSignin.html', data=10005)
    else:
        insertStudent(getLastStudentID()+1,student_name, student_email, student_password)
        return render_template('studentlogin.html', data=10006, student_name=student_name)


def getLastStudentID():
    cursor, db = connectHWCdb()

    sql = "SELECT TOP 1 * FROM Student ORDER BY studentID desc;"
    cursor.execute(sql)
    result = cursor.fetchall()[0][0]
    return result


def studenSignedCheck(name, email):
    cursor, db = connectHWCdb()

    sql = "select 1 from Student where name ='{}' and email='{}'".format(name, email)
    cursor.execute(sql)
    if cursor.fetchall():
        return True
    else:
        return False


#  route to port /teacher for transferring teacher login data from teacherlogin page and do password checking
@app.route('/teacher', methods=['GET', 'POST'])
def teacherLogin():
    if request.method == 'GET':
        teacher_email = request.args.get('teacher_email')
        teacher_password = request.args.get('teacher_password')

        if passwordCheck(teacher_email, teacher_password, "Teacher"):
            return quizManagepage()
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
        querylist = toList(request.args.get('qaList'))

        question_num = request.args.get('question_num')

        quiz_num = request.args.get('quiz_num')

        student_email = request.args.get('email')

        question_num = len(question_num)

        quiz_num = int(quiz_num)

        totalmark = 0
        deduction = []
        size = []
        questionNumber = 1
        for i in range(readQuizSize(quiz_num)):
            q1rows, q1col = countQueryRnC(selectSampleAnswer(i + 1, quiz_num))
            print(selectSampleAnswer(i + 1, quiz_num))
            print(q1rows, q1col)

            q2rows, q2col = countQueryRnC(querylist[i])
            print(querylist[i])
            print(q2rows, q2col)

            size.append(questionNumber)

            deduction.append(returnCorectState(compareResult(q1rows, q1col, q2rows, q2col)))

            totalmark += compareResult(q1rows, q1col, q2rows, q2col)
            insertAnswer(questionNumber, readstudentID(student_email), querylist[i],
                         compareResult(q1rows, q1col, q2rows, q2col), quiz_num)
            questionNumber += 1

        insertResult(readstudentID(student_email), quiz_num, totalmark, 'no feedback')

        return render_template('result.html', data=totalmark, deduction=deduction, size=size,
                               totalquestions=readQuizSize(quiz_num))


def selectSampleAnswer(qnum, quizID):
    cursor, db = connectHWCdb()
    sql = "select answer from Question where questionID='{}' and quizID='{}'".format(qnum, quizID)
    try:
        cursor.execute(sql)
        result = str(cursor.fetchall()[0])[2:-3]
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
def countQueryRnC(query):
    cursor, db = connectAWdb()
    try:
        cursor.execute(query)
        # if need the first item code: data = cursor.fetchone(), if need all item, code: data = cursor.fetchall()
        data = cursor.fetchall()

        try:
            for col in range(30):
                data[0][col]
        except Exception as e:
            columes = col

        rows = 0
        for queryrows in data:
            rows += 1

        # return data
        return rows, columes
    except Exception as e:
        return 'cannot run', 'cannot run'

    # testing

    # print(query)
    # cursor.execute(query)
    # data = cursor.fetchall()
    # q = 0
    # for queryitem in data:
    #     q += 1
    # return q


# calculate the mark
def compareResult(r1, c1, r2, c2):
    try:
        if r1 == r2 and c1 == c2 and type(r1) == int:
            return 1
        else:
            return 0
    except Exception as e:
        return 0


def returnCorectState(deduction):
    if deduction == 1:
        return 'Correct'
    else:
        return 'Incorrect'


#  read studentID from Students table in database
def readstudentID(email):
    cursor, db = connectHWCdb()

    sql = "select * from {} where email='{}'".format("Student", email)

    cursor.execute(sql)
    result = cursor.fetchall()[0][0]
    return result


def readStudentAnswernMarkList(studentID, quizID):
    cursor, db = connectHWCdb()

    sql = "select * from Answer where studentID = {} and quizID = {}".format(studentID, quizID)

    cursor.execute(sql)
    result = cursor.fetchall()
    aList = []
    mList = []
    for i in result:
        aList.append(i[2])
        mList.append(i[3])
    return aList, mList


#  read data from Students table
def readStudentList():
    cursor, db = connectHWCdb()

    sql = "select * from {}".format("Student")

    cursor.execute(sql)
    result = cursor.fetchall()
    sList = dict()
    for i in result:
        sList[i[0]] = i[1]
    return sList


#  read data from Result table
def readStudentResultList(sList):
    cursor, db = connectHWCdb()

    sql = "select * from {}".format("Result")

    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    mList = []
    for i in result:
        _html = "feedback?studentID="
        mList.append((sList.get(i[0]), i[1], i[2], i[0], _html + str(i[0]) + "&quizID="
                      + str(i[1]) + "&studentName=" + (sList.get(i[0]))))
    print(mList)
    return mList


def readTotalMark(studentID, quizID):
    cursor, db = connectHWCdb()

    sql = "select * from {} where studentID = {} and quizID = {}".format("Result", studentID, quizID)

    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][2]


@app.route('/test', methods=['GET', 'POST'])
def test():
    sID = request.args.get('studentID')
    qID = request.args.get('quizID')
    return render_template('test.html', quizID=qID, studentID=sID)


def quizFinishcheck(id, quiz_num):
    cursor, db = connectHWCdb()

    sql = "select 1 from Result where studentID='{}' and quizID='{}'".format(id, quiz_num)
    cursor.execute(sql)
    if cursor.fetchall():
        return True
    else:
        return False


def quizOpencheck(quizID):
    cursor, db = connectHWCdb()

    sql = "select 1 from Question where quizID='{}'".format(quizID)
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


def toList(strList):
    strList1 = str(strList)
    strList2 = strList1.split("[],")
    strList3 = []
    for strItem in strList2:
        strList3.append(strItem.replace('[]', ''))
    return strList3


#  insert data to Answer table
def insertAnswer(questionID, studentID, answer, mark, quizID):
    cursor, db = connectHWCdb()

    label = ['questionID', 'studentID', 'answer', 'mark', 'quizID']
    content = [questionID, studentID, answer, mark, quizID]

    sql = "insert into Answer ({0},{1},{2},{3},{4}) values({5},{6},'{7}',{8},{9})".format(label[0], label[1],
                                                                                          label[2], label[3], label[4],
                                                                                          content[0],
                                                                                          content[1],
                                                                                          checkString(content[2]),
                                                                                          content[3], content[4])
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


def deleteQuiz(quizID):
    cursor, db = connectHWCdb()

    sql = 'delete from Question where quizID = {}'.format(quizID)
    print(sql)
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


def insertQuestion(questionID, question, answer, quizID):
    cursor, db = connectHWCdb()

    label = ['questionID', 'question', 'answer', 'quizID']
    content = [questionID, question, answer, quizID]

    sql = "insert into Question ({0},{1},{2},{3}) values({4},'{5}','{6}',{7})".format(
        label[0], label[1],
        label[2], label[3], content[0], content[1],
        checkString(content[2]), content[3])
    print(sql)
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


def updateQuestion(questionID, question, answer, quizID):
    cursor, db = connectHWCdb()

    label = ['questionID', 'question', 'answer', 'quizID']
    content = [questionID, question, answer, quizID]

    sql = "update Question set ({0},{1},{2},{3}) values({4},'{5}','{6}',{7} where questionID = {8} and quizID = {9})".format(
        label[0], label[1],
        label[2], label[3], content[0], content[1],
        content[2], content[0], content[4])
    print(sql)
    result = cursor.execute(sql)
    db.commit()
    return True if result else False


#  insert data to Students table
def insertStudent(studentid, name, email, password):
    cursor, db = connectHWCdb()

    label = ['studentID', 'name','email', 'password']
    content = [studentid, name, email, password]

    sql = "insert into {0} ({1},{2},{3},{4}) values({5},'{6}','{7}','{8}')".format("Student", label[0], label[1],
                                                                         label[2], label[3],
                                                                         content[0], content[1],
                                                                         content[2], content[3])
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
def readQuestion(quiz_num):
    cursor, db = connectHWCdb()

    sql = 'select * from {} where quizID = {}'.format("Question", quiz_num)

    cursor.execute(sql)
    result = cursor.fetchall()
    qList = []
    for i in result:
        qList.append(i[1])

    print(qList)
    return qList


#  run the main program
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)


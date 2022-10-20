from django.shortcuts import render
from sqlserverconnect.models import sqlserverconn
import pyodbc

conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )
                        
cursor=conn.cursor()

def loggg(request):
    '''
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )'''
    cursor=conn.cursor()
    
    cursor.execute("select * from Students")
    result=cursor.fetchall()
    return render(request,'student login.html',{'sqlserverconn':result})


def connsql(request):
    '''
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )'''
    cursor=conn.cursor()

    cursor.execute("select * from Students")
    result=cursor.fetchall()

    cursor1=conn.cursor()
    cursor1.execute("select * from Teacher")
    result1=cursor1.fetchall()


    return render(request,'Admindetail.html',{'sqlserverconn':result, 'teacher1':result1})


def question(request):
    '''
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )
    cursor=conn.cursor()'''
    cursor.execute("select * from Question")
    result=cursor.fetchall()
    return render(request,'all question.html',{'question':result})


def submitted(request):
    '''
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )
    cursor=conn.cursor()
    '''
    cursor.execute("select * from Question")
    result=cursor.fetchall()
    return render(request,'FinishPage.html',{'submitted':result})


def menu(request):
    '''
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )
    cursor=conn.cursor()
    '''
    cursor.execute("select * from Question")
    result=cursor.fetchall()
    return render(request,'Menu.html',{'submitted':menu})


def TeacherLogin(request):
    '''
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )
    cursor=conn.cursor()
    '''
    cursor.execute("select * from Question")
    result=cursor.fetchall()
    return render(request,'teacher login.html',{'submitted':TeacherLogin})


def AdminLogin(request):
    '''
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )
    cursor=conn.cursor()
    '''
    cursor.execute("select * from Question")
    result=cursor.fetchall()
    return render(request,'admin login.html',{'submitted':AdminLogin})

'''
def teacher(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )
    cursor=conn.cursor()
    cursor.execute("select * from Teacher")
    result=cursor.fetchall()
    return render(request,'admin login.html',{'submitted':AdminLogin})
    '''


def QuestionAndAnswer(request):
    '''
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )
    cursor=conn.cursor()
    '''
    cursor.execute("select * from Question")
    result=cursor.fetchall()
    return render(request,'QuestionAndAnswer.html',{'QuestionAndAnswer':result})


def QuestionSubmittion(request):
    '''
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-46ON81A;'
                        'Database=HomeworkChecker;'
                        'Trusted_Connection=yes;' )
    cursor=conn.cursor()
    '''
    cursor.execute("select * from Question")
    result=cursor.fetchall()
    return render(request,'QuestionSubmittion.html',{'QuestionSubmittion':result})


def UploadingScreen(request):
    '''
    cursor=conn.cursor()
    '''
    cursor.execute("select * from Question")
    result=cursor.fetchall()
    return render(request,'UploadingScreen.html',{'UploadingScreen':result})
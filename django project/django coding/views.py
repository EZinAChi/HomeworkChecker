from django.shortcuts import render
from StudentDatabase.models import connectDatabaseToDjango
import pyodbc

def connectsql(request):
    conec=pyodbc.connect('Driver={SQL server};'
                        #access sql server
                         'Server=DUNGPHAM-PC; '
                         #access database
                         'Database=user_database;'
                         'Trusted_Connection=yes;')
    
    cursor=conec.cursor()
    cursor.execute("select * from Student_info_DummyDB")
    results =cursor.fetchall()
    return render(request, 'Index.html', {'connectDatabaseToDjango': results})
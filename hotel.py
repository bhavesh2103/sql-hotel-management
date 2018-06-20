import smtplib
import mysql.connector
import random
import os
import datetime
from prettytable import PrettyTable
from prettytable import from_db_cursor
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
conn=mysql.connector.connect(user='root',password='060492',host='localhost')
c=conn.cursor()
def create_table():    
    c.execute('CREATE DATABASE IF NOT EXISTS HOTEL')
    c.execute('USE HOTEL')
    c.execute("CREATE TABLE IF NOT EXISTS HOTEL3(roomno int primary key,name varchar(40),emailid varchar(40),CI DATE,CO DATE,bill int,number int);")
class CheckOutGreaterError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)
def checkin():
    flag=0
    number=0
    room_no=int(input("ENTER A VACANT ROOM NO. :\n"))
    name=input("ENTER NAME OF THE GUEST\n")
    email=input("ENTER EMAIL ID OF THE GUEST\n")
    while(flag!=1):
        try:
            CI=int(input("ENTER CHECKIN DATE\n"))
            CO=int(input("ENTER CHECKOUT DATE\n"))
            if(CO<CI):
                raise CheckOutGreaterError("CHECKOUT DATE IS LESS THAN CHECKIN DATE")
        except CheckOutGreaterError as e:
                    print(e)
                    print("Enter again")
        if(CI<CO):
            flag=1
            
                
    number1=int(input("ENTER NO OF PERSONS"))
    number=int(CO)-int(CI)
    number=int(number)
    bill=number*1000*number1
    c.execute("UPDATE HOTEL3 set name='%s',emailid='%s',CI='%d',CO='%d',bill='%d',number='%d' WHERE roomno='%d'"%(name,email,CI,CO,bill,number1,room_no))
    conn.commit()

def vacantRooms():
    print("ROOMS WHICH ARE VACANT ARE:")
    c.execute("SELECT roomno FROM hotel3 where name='0'")
    i=0
    for row in c.fetchall():
        i=i+1
        print(row[0])
    print("Number Of Rooms Empty is : '%d'"%i)

def addToBill():
    print("Enter Room number to update its bill\n")
    k=int(input())
    bill=int(input("Enter the amount to add \n"))
    c.execute("SELECT bill FROM HOTEL3 WHERE roomno='%d'"%k)
    for row in c.fetchall():
     oldbill=list(row)
     print("THE OLD BILL WAS"% oldbill )
     bill=bill+int(oldbill[0])
     c.execute("UPDATE hotel3 set bill='%d' WHERE roomno='%d'"%((bill),k))
     conn.commit()

def display():
    c.execute('SELECT * FROM HOTEL3')
    mytable=from_db_cursor(c)
    print(mytable)

def displaybill():
    c.execute('SELECT * FROM HOTEL3 ORDER BY bill DESC')
    mytable=from_db_cursor(c)
    print(mytable)

def checkout():
    key=int(input("ENTER ROOMNO OF THE GUEST LEAVING TO DISPLAY his/her BILL\n"))
    c.execute("SELECT bill FROM HOTEL3 WHERE roomno='%d'"% key)
    for row in c.fetchall():
        mylist=list(row)
        print("\nBILL FOR ROOM NUMBER %d is  "%key)
        print (mylist)
        c.execute("UPDATE hotel3 set name='0', emailid='0',CI='000000',CO='000000',bill='0',number=0 WHERE roomno='%d'"%key)
        print("\n")
    conn.commit()
    
def file():
    flag2=0
    while(flag2==0):
        try:
            flag2=0
            c.execute('SELECT * FROM HOTEL3')
            mytable=from_db_cursor(c)
            file=open('HOTELDATABASE.txt','w')
            file.write(tabulate(mytable))
            toaddr=input('ENTER YOUR EMAIL ADDRESS\n')
            fromaddr="2016.dhiren.motwani@ves.ac.in"
            msg=MIMEMultipart()
            msg['From']=fromaddr
            msg['To']=toaddr
            msg['Subject']="HOTEL DATABASE PYTHON PROJECT"
            body="OPEN ATTACHMENT FOR HOTELDATABASE"
            msg.attach(MIMEText(body,'plain'))
            filename="textfile.txt"
            attachment=open('HOTELDATABASE.txt','rb')
            part=MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename=%s"% filename)
            msg.attach(part)
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(fromaddr,"797@dhiren")
            text=msg.as_string()
            server.sendmail(fromaddr,toaddr,text)
            server.quit()
            os.system('C:/Users/dhire/Desktop/HOTELDATABASE.txt')
        except:
            print("\nCONNECT TO INTERNET\n")
            flag2=2
        if(flag2==0):
             print('FILE SUCCUSSEFULLY SAVED AND SENT')

def start():
    create_table()
    ab=int(input('PRESS 1 IF RECORDS ALREADY EXISTS\nPRESS 2 IF RECORDS DOES NOT EXIST\n'))
    try:
        if(ab==2):
            j=int(input("NO OF ROOMS IN THE HOTEL"))
            i=1
            while(i<=j):
              c.execute("INSERT INTO hotel3 VALUES ('%s',0,0,0,0,0,0)"%i)
              i=i+1
              conn.commit()
        print("CHOOSE AN ACTION TO PERFORM: ")
        r=0
        while r<10:
            
            print("Press 1 to Checkin Customers\nPress 2 to Checkout Customers and display their bill\nPress 3 to Add a bill amount to particular room\nPress 4 To display details of all rooms \nPress 5 to display details of all rooms with respect to Bill amount\nPress 6 to check vacant rooms\nPress 7 to store all the details of customers in a file and email the file\nPress 10 to EXIT \n")
            r=int(input())
            if(r==1):
                checkin()
                print('CHECKIN SUCESSFULL')
            elif(r==2):
                checkout()
                print('CHECKOUT SUCESSFULL')
            elif(r==3):
                addToBill()
            elif(r==4):
                display()
            elif(r==5):
                displaybill()
            elif(r==6):
                vacantRooms()
            elif(r==7):
                file()
               
            else:
                r=10
    except:
         print("\nDATABASE ALREADY EXISTS ,RERUN THE PROGRAM\n")
        
start()
c.close()
conn.close()

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
from tkinter import *
from functools import partial
conn=mysql.connector.connect(user='root',password='060492',host='localhost')
c=conn.cursor()
d=0
def create_table():    
    c.execute('CREATE DATABASE IF NOT EXISTS HOTEL')
    c.execute('USE HOTEL')
    c.execute("CREATE TABLE IF NOT EXISTS HOTEL3(roomno int primary key,name varchar(40),emailid varchar(40),CI DATE,CO DATE,bill int,number int);")

def checkin():
    number=0
    frame.pack_forget()
    frame3.pack()
    
def fourth():
    j=int(E1.get())
    i=1
    while(i<=j):
          c.execute("INSERT INTO hotel3 VALUES ('%s',0,0,0,0,0,0)"%i)
          i=i+1
          conn.commit()
    second()
def third():
    A2=Label(f1,text=" ENTER NO OF ROOMS")
    A2.pack()
    E1.pack()
    b11=Button(f1,text="SUBMIT",command=fourth)
    b11.pack()
def ch():
    number=0
    bill=0
    room_no=0
    number1=0
    room_no=int(l11.get())
    name=l22.get()
    email=l33.get()
    CI=int(l44.get())
    CO=int(l55.get())
    number1=int(l66.get())
    number=int(CO)-int(CI)
    number=int(number)
    bill=int(number*1000*number1)
    c.execute("UPDATE HOTEL3 set name='%s',emailid='%s',CI='%d',CO='%d',bill='%d',number='%d' WHERE roomno='%d'"%(name,email,CI,CO,bill,number1,room_no))
    conn.commit()
    second()
def second():
    X1.pack_forget()
    T1.pack_forget()
    O1.pack_forget()
    f1.pack_forget()
    I1.pack_forget()
    frame3.pack_forget()
    K1.pack_forget()
    J1.pack_forget()
    frame.pack()
def checkout():
  frame.pack_forget()
  I1.pack()
def checkingout():
 key=int(I3.get())
 c.execute("SELECT bill FROM HOTEL3 WHERE roomno='%d'"% key)
 p=0
 for row in c.fetchall():
   p=row[0]
 d=p
 I6.config(text=d)
 c.execute("UPDATE hotel3 set name='0', emailid='0',CI='000000',CO='000000',bill='0',number=0 WHERE roomno='%d'"%key)
 conn.commit()
def addbill():
  frame.pack_forget()
  K1.pack()
def addbill2():
  key=int(K3.get())
  bill=int(K6.get())
  oldbill=0
  c.execute("SELECT bill FROM HOTEL3 WHERE roomno='%d'"%key)
  for row in c.fetchall():
     oldbill=list(row)
     bill=bill+int(oldbill[0])
     c.execute("UPDATE hotel3 set bill='%d' WHERE roomno='%d'"%((bill),key))
     conn.commit()
def email():
  frame.pack_forget()
  J1.pack()
def file():
  
    c.execute('SELECT * FROM HOTEL3')
    mytable=from_db_cursor(c)
    file=open('HOTELDATABASE.txt','w')
    file.write(tabulate(mytable))
    toaddr=J3.get()
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

def display():
  frame.pack_forget()
  O1.pack()
  c.execute('SELECT * FROM HOTEL3')
  mytable=from_db_cursor(c)
  O2.config(text=mytable)
  
def displaybill():
  frame.pack_forget()
  T1.pack()
  c.execute('SELECT * FROM HOTEL3 ORDER BY bill DESC')
  mytable=from_db_cursor(c)
  T2.config(text=mytable)
def vacant():
  frame.pack_forget()
  X1.pack()
  c.execute("SELECT roomno FROM hotel3 where name='0'")
  mytable=from_db_cursor(c)
  X3.config(text=mytable)
  i=0
  c.execute("SELECT roomno FROM hotel3 where name='0'")
  for row in list(c.fetchall()):
        i=i+1
  X5.config(text=i)
  
tk=Tk()
X1=Frame(tk)
O1=Frame(tk)
T1=Frame(tk)
J1=Frame(tk)
K1=Frame(tk)
I1=Frame(tk)
f1=Frame(tk)
E1=Entry(f1)
frame=Frame(tk)
frame.config()
X1.config()
O1.config()
T1.config()
J1.config()
K1.config()
f1.config()
E1.config()
I1.config()
frame3=Frame(tk)
l11=Entry(frame3)
l22=Entry(frame3)
l33=Entry(frame3)
l44=Entry(frame3)
l55=Entry(frame3)
l66=Entry(frame3)
X2=Label(X1,text="ROOMS WHICH ARE VACANT ARE")
X2.pack()
X3=Label(X1)
X3.pack()
X4=Label(X1,text="NO OF VACANT ROOMS ARE")
X4.pack()
X5=Label(X1)
X5.pack()
X6=Button(X1,text="OKAY",command=second)
X6.pack()
O2=Label(O1)
O2.pack()
O3=Button(O1,text="OKAY",command=second)
O3.pack()
T2=Label(T1)
T2.pack()
T3=Button(T1,text="OKAY",command=second)
T3.pack()

J2=Label(J1,text="ENTER YOUR EMAIL ADDRESS")
J2.pack()
J3=Entry(J1)
J3.pack()
J4=Button(J1,text="SUBMIT",command=file)
J4.pack()
J7=Button(J1,text="OKAY",command=second)
J7.pack()
K2=Label(K1,text="ADD ROOM NO TO UPDATE ITS BILL")
K2.pack()
K3=Entry(K1)
K3.pack()
K5=Label(K1,text="ENTER BILL AMOUNT")
K5.pack()
K6=Entry(K1)
K6.pack()
K4=Button(K1,text="SUBMIT",command=addbill2)
K4.pack()
K7=Button(K1,text="OKAY",command=second)
K7.pack()
I2=Label(I1,text="ENTER THE ROOMNO OF THE GUEST CHECKING OUT")
I2.pack()
I3=Entry(I1)
I3.pack()
I4=Button(I1,text="SUBMIT",command=checkingout)
I4.pack()
I5=Label(I1,text="BILL OF THE CUSTOMER CHECKING OUT IS")
I5.pack()
I6=Label(I1)
I6.pack()
I7=Button(I1,text="OKAY",command=second)
I7.pack()
l1=Label(frame3,text="ENTER A VACANT ROOM NO. :\n")
l1.pack()
l11.pack()
l2=Label(frame3,text="ENTER NAME OF THE GUEST :\n")
l2.pack()
l22.pack()
l3=Label(frame3,text="ENTER EMAILID OF THE GUEST :\n")
l3.pack()
l33.pack()
l4=Label(frame3,text="ENTER CHECKIN DATE :\n")
l4.pack()
l44.pack()
l5=Label(frame3,text="ENTER CHECKOUT DATE :\n")
l5.pack()
l55.pack()
l6=Label(frame3,text="ENTER NO OF PERSONS :\n")
l6.pack()
l66.pack()
l7=Button(frame3,text="SUBMIT",command=ch)
l7.pack()
create_table()

f1.pack()
#h2=PhotoImage(file="h1.png")
#V1=Label(frame,image=h2)
#V1.pack()
#A1=Label(f1,image=h2)
#A1.pack()
b1=Button(f1,text="DATABASE ALREADY EXISTS",command=second)
b1.pack()
b2=Button(f1,text="TO CREATE DATABASE",command=third)
b2.pack()
b1=Button(frame,text="CHECKIN",command=checkin)
b1.pack()
b2=Button(frame,text="CHECKOUT",command=checkout)
b2.pack()
b3=Button(frame,text="ADD A BILL AMOUNT TO PARTICULAR ROOM",command=addbill)
b3.pack()
b4=Button(frame,text="DISPLAY DETAILS OF ALL ROOMS",command=display)
b4.pack()
b5=Button(frame,text="DISPLAY DETAILS ACCORDING TO BILL AMOUNT",command=displaybill)
b5.pack()
b6=Button(frame,text="TO DISPLAY ALL VACANT ROOMS",command=vacant)
b6.pack()
b7=Button(frame,text="TO STORE DETAILS IN A FILE AND EMAIL IT",command=email)
b7.pack()
b8=Button(frame,text="EXIT",command=tk.destroy)
b8.pack()
        

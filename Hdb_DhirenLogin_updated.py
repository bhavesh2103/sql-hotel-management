import mysql.connector
import random
import os
import datetime

conn=mysql.connector.connect(user='root',password='060492',host='localhost')
c=conn.cursor()

def create_table():
    
    c.execute('CREATE DATABASE IF NOT EXISTS HOTEL')
    c.execute('USE HOTEL')
    c.execute("CREATE TABLE IF NOT EXISTS HOTEL3(roomno int primary key,name varchar(40),emailid varchar(40),CI DATE,CO DATE,bill int,number int);")
def data_entry():
    room_no=1
    name="python"
    email="abc@gmail.com"
    CI=20
    CO=21
    bill=0
    number=int(random.randrange(1,10))
    c.execute("INSERT INTO HOTEL3(roomno,name,emailid,CI,CO,bill,number) VALUES (%s,%s,%s,%s,%s,%s,%s)",(room_no,name,email,CI,CO,bill,number))
    conn.commit()
    

def display():
    c.execute('SELECT * FROM HOTEL3')
    for row in c.fetchall():
        mylist=list(row)
        print(mylist)


def checkin():
    os.system('cls')
    number=0
    room_no=int(input("ENTER A VALID ROOM NO. (FROM 1 TO 50) :\n"))
    name=input("ENTER NAME OF THE GUEST\n")
    email=input("ENTER EMAIL ID OF THE GUEST\n")
    CI=int(input("ENTER CHECKIN DATE\n"))
    CO=int(input("ENTER CHECKOUT DATE\n"))

    number=int(CO)-int(CI)
    number=int(number)
    bill=number*3000
    c.execute("UPDATE HOTEL3 set name='%s',emailid='%s',CI='%d',CO='%d',bill='%d',number='%d' WHERE roomno='%d'"%(name,email,CI,CI,bill,number,room_no))
    conn.commit()
def checkout():
    os.system('cls')
    key=int(input("ENTER ROOMNO OF THE GUEST LEAVING TO DISPLAY his/her BILL\n"))
    c.execute("SELECT bill FROM HOTEL3 WHERE roomno='%d'"% key)
    for row in c.fetchall():
        mylist=list(row)
        print("\nBILL FOR ROOM NUMBER %d is  "%key)
        print (mylist)
        c.execute("UPDATE hotel3 set name='0', emailid='0',CI='0',CO='0',bill='0',number=0 WHERE roomno='%d'"%key)
        print("\n")
    display()
def start():
    create_table()
    ab=int(input('PRESS 1 IF TABLE ALREADY EXISTS\nPRESS 2 IF TABLE DOESNOT EXIST\n'))
    if(ab==2):
        i=1
        while(i<50):
          c.execute("INSERT INTO hotel3 VALUES ('%s',0,0,0,0,0,0)"%i)
          i=i+1
          conn.commit()
######    for i in range(10):
######        data_entry()
    print("roomno\tname\temailid\tCI\tCO\tbill\tnumber")
    display()
    print("CHOOSE AN ACTION TO PERFORM: ")
    r=0
    while r<10:
        
        print("Press 1 to Checkin Customers\nPress 2 to Checkout Customers and display their bill\nPress 3 to Add a bill amount to particular room\nPress 4 to display details of all rooms with respect to roomno\nPress 5 to display details of all rooms with respect to Bill amount\nPress 6 to check vacant rooms\nPress 7 to view all Staff details\nPress 8 to store all the details of customers in a file\nPress 9 to display \n")
        r=int(input())
        if(r==1):
            checkin()
            print('CHECKIN SUCESSFULL')
        elif(r==2):
            checkout()
            print('CHECKOUT SUCESSFULL')
        elif(r==3):
            r=3
        elif(r==4):
            r=3
        elif(r==5):
            r=3
        elif(r==6):
            r=3
        elif(r==7):
            r=3
        elif(r==8):
            r=3
        elif(r==9):
            display()
        else:
            r=10
            
    
        

start()
c.close()
conn.close()

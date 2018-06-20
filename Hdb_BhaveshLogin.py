import mysql.connector
import random
import os
import datetime
from prettytable import PrettyTable
from prettytable import from_db_cursor
conn=mysql.connector.connect(user='root',password='060492',host='localhost')
c=conn.cursor()

def create_table():    
    c.execute('CREATE DATABASE IF NOT EXISTS HOTEL')
    c.execute('USE HOTEL')
    c.execute("CREATE TABLE IF NOT EXISTS HOTEL3(roomno int primary key,name varchar(40),emailid varchar(40),CI DATE,CO DATE,bill int,number int);")
    
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

def addToBill():
    print("Enter Room number to update its bill\n")
    k=int(input())
    bill=int(input("Enter the amount to add \n"))
    c.execute("SELECT bill FROM HOTEL3 WHERE roomno='%d'"%k)
    c.execute("UPDATE hotel3 set bill='%d' WHERE roomno='%d'"%((bill),k))
    conn.commit()

def display():
    c.execute('SELECT * FROM HOTEL3')
    mytable=from_db_cursor(c)
    print(mytable)

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
    conn.commit()
    display()
def start():
    create_table()
    ab=int(input('PRESS 1 IF RECORDS ALREADY EXISTS\nPRESS 2 IF RECORDS DO NOT EXIST\n'))
    if(ab==2):
        
        i=1
        while(i<=50):
          c.execute("INSERT INTO hotel3 VALUES ('%s',0,0,0,0,0,0)"%i)
          i=i+1
          conn.commit()
    else:
        display()
        


    print("CHOOSE AN ACTION TO PERFORM: ")
    r=0
    while r<10:
        
        print("Press 1 to Checkin Customers\nPress 2 to Checkout Customers and display their bill\nPress 3 to Add a bill amount to particular room\nPress 4 To display details of all rooms \nPress 5 to display details of all rooms with respect to Bill amount\nPress 6 to check vacant rooms\nPress 7 to view all Staff details\nPress 8 to store all the details of customers in a file\nPress 10 to EXIT \n")
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
            r=3
        elif(r==6):
            r=3
        elif(r==7):
            r=3
        elif(r==8):
            r=3

        else:
            r=10
            
    
        

start()
c.close()
conn.close()

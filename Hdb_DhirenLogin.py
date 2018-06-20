import mysql.connector
import random
#import date

conn=mysql.connector.connect(user='root',password='',host='localhost')
c=conn.cursor()

def create_table():
    
    c.execute('CREATE DATABASE IF NOT EXISTS HOTEL')
    c.execute('USE HOTEL')
    c.execute("CREATE TABLE IF NOT EXISTS HOTEL3(roomno int,name varchar(40),emailid varchar(40),CI int,CO int,bill int,number int);")


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
        print(row)


def checkin():
    room_no=int(input("ENTER ROOM NO:\n"))
    name=input("ENTER NAME OF THE GUEST\n")
    email=input("ENTER EMAIL ID OF THE GUEST\n")
    CI=input("ENTER CHECKIN DATE\n")
    CO=input("ENTER CHECKOUT DATE\n")
    number=CO-CI
    bill=number*3000
    c.execute("INSERT INTO HOTEL3(roomno,name,emailid,CI,CO,bill,number) VALUES (%s,%s,%s,%s,%s,%s,%s)",(room_no,name,email,CI,CO,bill,number))
    conn.commit()
def checkout():
    key=input("ENTER NAME OF THE GUEST LEAVING TO DISPLAY his/her BILL")
    c.execute("SELECT * FROM HOTEL3 WHERE name=%s",(key))
    x=c.fetchall()
    print(x)
        
def start():
    create_table()
##    for i in range(10):
##        data_entry()
    display()
    print("roomno\tname\temailid\tCI\tCO\tbill\tnumber")
    print("CHOOSE AN ACTION TO PERFORM: ")
    r=0
    while r<9:
        print("Press 1 to Checkin Customers\nPress 2 to Checkout Customers and display their bill\nPress 3 to Add a bill amount to particular room\nPress 4 to display details of all rooms with respect to roomno\nPress 5 to display details of all rooms with respect to Bill amount\nPress 6 to check vacant rooms\nPress 7 to view all Staff details\nPress 8 to store all the details of customers in a file\nPress 9 to exit\n")
        r=int(input())
        if(r==1):
            checkin()
        elif(r==2):
            checkout()
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
        else:
            r=9
    
        

start()
c.close()
conn.close()

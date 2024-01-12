from colorama import Fore
import psycopg2
from prettytable import PrettyTable
from datetime import datetime

cmd=['view -a','view','add','del','update','exit']    # Commands for CRUD

hostname='localhost'
database='Project'
username='postgres'
pwd='python'
port_no=5432
cur,conn=None,None

try:
    conn=psycopg2.connect( host=hostname, dbname=database, user=username, password=pwd, port=port_no)   #create connection object
    conn.autocommit = True       #will make changes in DB if commit otherwise script does not execute
    cur= conn.cursor()    #creates cursor object for CRUD operation

    script='''CREATE TABLE if not exists Phone_Book(    
        ContactId     BIGINT PRIMARY KEY,
        FirstName     varchar(40) NOT NULL,
        LastName      varchar(40) Not NULL,
        Email         varchar(50) NOT NULL,
        PhoneNumber   BIGINT ) '''    #Script

    registeredUser='''CREATE TABLE if not exists RegisteredUser(
            Mobile_No        BIGINT PRIMARY KEY,
            Firstname        varchar(80) NOT NULL,
            Lastname         varchar(80) NOT NULL  ) '''
    
    cur.execute(script)          #will execute script
    cur.execute(registeredUser)         

except Exception as E:
    print(E)    


def inTableFormat(t):
    colName=['ContactId','FirstName','LastName','Email','PhoneNumber']
    table=PrettyTable(colName)             # list of collumn name
    for x in t:
        table.add_row([x[0],x[1],x[2],x[3],x[4]])
    
    print(Fore.CYAN,table)
    print(Fore.WHITE)
    

def insertUser(firstName,lastName,mobNo):       # To insert data of registered user in table
    try:
        insert_script='INSERT INTO RegisteredUser(Mobile_No,Firstname,Lastname) VALUES (%s,%s,%s)'
        insert_values=(mobNo,firstName,lastName)
        cur.execute(insert_script,insert_values)
    except Exception as E:
        print(E)
    else:
        return 1
        

def choice():               # Just for taking user choice
    print(Fore.MAGENTA+"1.Registration")
    print("2.Login( If u are already registered )")
    res=int(input(Fore.WHITE+"Enter UR Choice:"))
    return res


def LoginUser(firstname,lastname):      # To check user exist or not
    script='''SELECT * FROM RegisteredUser'''
    cur.execute(script)
    try:        # if error occur in fetching data from table means table is empty 
        for x in cur.fetchall():        #will fetch all records from table
            if x[1]==firstname and x[2]==lastname:
                return 1
    except:
        return 0


def Registration():             # To register User
    print("\nWelcome To Registration :")
    firstName=input("Enter FirstName:")
    lastName=input("Enter LastName:")
    mobNo=int(input("Enter Mobile Number:"))
    if insertUser(firstName,lastName,mobNo):
        print(Fore.GREEN+'[{} Are Successfully Registered]'.format(firstName))
        Fore.WHITE


def login():                   # To Login User
    print("\n\tLogin Page:")
    firstname=input("Enter Ur First Name:")
    lastname=input("Enter Ur Last Name:")
    l=LoginUser(firstname,lastname)
    if l==1:
        print(Fore.GREEN+"[User {} Logged In]".format(firstname)+Fore.WHITE)
        print(datetime.now())
        print('---------------------------------------')
        return 1
    else:
        print("Sorry!! User Does Not Exist")


def template():             # Display Commands
    print("What Do You Want To Do?")
    print("[view -a]        To view All Saved Contacts")
    print("[view]           To view a Specific Contact")
    print("[add]            To add a New Contact")
    print("[del]            To delete a Contact")
    print("[update]         To update an Existing Contact")
    print("[exit]           To Exit the Program")
   

def view_Allcontacts():     # To view all contacts
    script='SELECT * from Phone_Book'
    cur.execute(script)
    try:
        contacts=cur.fetchall()
        if len(contacts)==0:
            print("Contact List Is Empty !!!")
        else:
            inTableFormat(contacts)

    except Exception as E:
        print(E)


def viewContact(ftname,ltname):     # To view single Contact
    script='''SELECT * from Phone_Book'''
    cur.execute(script)
    reg=0           # To check user exist or not
    try:
        contact=cur.fetchall()
        if len(contact)==0:
            print("Contact List Is Empty !!!")
        elif len(contact)>0:
            for x in contact:
                if x[1]==ftname and x[2]==ltname:
                    reg=1
                    inTableFormat([x])
            else:
                if reg==0:
                    print(Fore.RED+"Contact {} Doesn't Exist".format(ftname)+Fore.WHITE)
    except Exception as E:  
        print(E)


def addContact(id,fname,lname,email,no):
    try:
        insert_script='INSERT INTO Phone_Book (ContactId,FirstName,LastName,Email,PhoneNumber) VALUES (%s,%s,%s,%s,%s)'
        insert_values=(id,fname,lname,email,no)
        cur.execute(insert_script,insert_values)
    except Exception as E:
        print(E)
    else:
        print(Fore.GREEN+"[User {} Added Successfully]".format(fname)+Fore.WHITE)


def delete_Record():
    cid=int(input("Enter Contact Id:"))
    fname=input("Enter First Name:")
    lname=input("Enter Last Name:")
    email=input("Enter Email:")
    mobNo=int(input("Enter Mobile Number:"))
    try:
        delete_script='DELETE FROM Phone_Book Where ContactId=%s'
        delete_record=(cid,)
        cur.execute(delete_script,delete_record)
    except:
        print("Contact Doesn't Exist")
    else:
        print(Fore.GREEN+"Contact {} Deleted Successfully !!!".format(fname)+Fore.WHITE)


def updateContact(email,no,fname):
    try:
        update_script="UPDATE Phone_Book SET PhoneNumber=%s where Email=%s"
        update_record=(no,email)
        cur.execute(update_script,update_record)
    except:
        print("Contact Doesn't Exist !!!")
    else:
        print(Fore.GREEN+"The Contact {} Successfully Updated !!!".format(fname)+Fore.WHITE)


def main():
    print("Welcome To Digital Phone Book")
    res=choice()
    if res==1:
      Registration()
    else:
      login_id=login()
      if login_id==1: 
          template()
          while True:
                res=input("\nEnter Command:").lower()
                if res==cmd[0]:
                    view_Allcontacts()
                elif res==cmd[1]:
                    firstname=input("Enter FirstName :")
                    lastname=input("Enter LastName :")
                    viewContact(firstname,lastname)
                elif res==cmd[2]:
                    cid=int(input("Enter Contact Id:"))
                    firstname=input("Enter FirstName :")
                    lastname=input("Enter LastName :")
                    email=input("Enter Email:")
                    mobNo=input("Enter Mobile Number:")
                    addContact(cid,firstname,lastname,email,mobNo)
                elif res==cmd[3]:
                    delete_Record()
                elif res==cmd[4]:
                    print("Enter User Data to Change Phone Number:")
                    fname=input("Enter First Name:")
                    email=input("Enter Email Id:")
                    newNo=int(input("Enter Mobile Number To change:"))
                    updateContact(email,newNo,fname)
                elif res==cmd[5]:
                    print("")
                    quit()   
                else:
                    print("You Entered Wrong Command! Please Try Again")  
                if len(input("\nPress Enter To Continue"))!=0:
                    break


main()

cur.close()             # To close the cursor Object
conn.close()            # To close the connection Object

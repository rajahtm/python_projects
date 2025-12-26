
import mysql.connector
def connectdb():
    
        mydb = mysql.connector.connect(
            host="localhost",
            user ="root",
            password ="Raja@1096",
            database ="SBIBANKDATABASE"
        )
        return mydb

dbconnected = connectdb()
mycursor = dbconnected.cursor(buffered=True)

     
     
def signup():
    name = input("enter your name :").strip().lower()
    password = input("enter your password :").strip().lower()
    userole =input("enter  role her customer / admin :").strip().lower()
    dbconnected = connectdb()
    mycursor = dbconnected.cursor(buffered=True)
    mycursor.execute("insert into users(username,password,userrole)values(%s,%s,%s)", (name,password,userole))
    dbconnected.commit()
    mycursor.execute("select userid from users where username = %s",(name,))
    userid_tuple = mycursor.fetchone()
    accounttype = input("enter your account type savings / current :").strip().lower()
    mycursor.execute("insert into accounts(userid,accounttype,accountbalance)values(%s,%s,%s)",(userid_tuple[0],accounttype,5000,)) 
    dbconnected.commit()
    print("signup successful")
def login():
     name = input("enter your name:").strip().lower()
     password = input("enter your password:").strip().lower()
     role = input("enter your role customer / admin :").strip().lower()
     mycursor.execute("select*from users where username = %s",(name,))
     name = mycursor.fetchone()
     username,password,userrole,userid=name
     if userrole =="customer":
          print("-------customer login successful---------")
          print("1. view account balance")
          print("2. deposit amount")
          print("3. withdraw amount")
          print("4. raise a request")
          choic = input("enter here one option :")
          if choic =="1":
               balance_check(userid)
          if choic =="2":
               deposit(userid)
          if choic == "3":
               withdraw(userid)
          if choic =="4":
               print("1. cheque book request") 
               print("2. atm card request")
               print("3. loan request")
            #    print("4. complaint registration")
               request_choice = input("enter your request option :")
          if request_choice =="1":
                request= "chequebook"
                checkbook_request(userid,request)
          if request_choice == "3":
               request = "loan"
               loan_request(userid,request)
          if request_choice =="2":
               request = "atmcard"
               atm_request(userid,request)
    

     if userrole == "admin":
          print("--------admin login successful---------")
          print(" 1.delate user ")
          print("2. view account user details")
          admin_choice = input("enter your choice :")
          if admin_choice =="1":
               delate_user()
          if admin_choice =="2":
               view_user_details()
def withdraw(userid):
     amount = int(input("enter amount to withdraw :"))
     mycursor.execute("select *from accounts where userid = %s",(userid,))
     account = mycursor.fetchone()
     accountid,userid,accounttype,accountbalance = account
     if amount > accountbalance:
          print(f"insufficient balance your available balance is : {accountbalance}")
     else:
          new_balance = accountbalance - amount
          mycursor.execute("update accounts set accountbalance = %s where userid = %s",(new_balance,userid))
          dbconnected.commit()
          print("withdraw successful. your avilable balance is :", new_balance)
def deposit(userid):

    
    amount = int(input("enter amount to deposit:"))
    if amount<=100:
          print("amount should be greater than 100")
    else:
        mycursor.execute("select *from accounts where userid = %s",(userid,))
        account = mycursor.fetchone()
        accountid,userid,accounttype,accountbalance = account
        new_balance = accountbalance + amount
        print("deposit successful. your available balance is :", new_balance)
        dbconnected.commit()
def balance_check(userid):
     mycursor.execute("select *from accounts where userid = %s",(userid,))
     account = mycursor.fetchone()
     accountid,userid,accounttype,accountbalance = account
     print("your available balance is :",accountbalance)
     dbconnected.commit()
def checkbook_request(userid,request):
    #  mycursor.execute("insert into requests(userid,requesttype)values(%s,%s)",(userid,request))
     print("cheque book request successful")  

     dbconnected.commit() 
def loan_request(userid,request):
     loan_amount = int(input("enter loan amount :"))
     mycursor.execute("insert into requests(userid,requesttype,request_balance)values(%s,%s,%s)",(userid,request,loan_amount))
     dbconnected.commit()
     print("loan request successful")
def atm_request(userid,request):
     
    #  mycursor.execute("insert into requests(userid,requesttype)values(%s,%s)",(userid,request))
    
     print("atm card request successful")
     dbconnected.commit()


def view_user_details():
     mycursor.execute("select users.userid,users.username,accounts.accounttype,accounts.accountbalance ,requests.requesttype from users left join accounts using(userid) left join requests using(userid)")
     users_details = mycursor.fetchall()
     id = int(input("enter user id to view details :"))
     for user in users_details:
          if user[0] == id:
               print(user)
def delate_user():
     id = int(input("enter user id  to  delate :"))
     mycursor.execute("delete from requests where userid = %s",(id,))
     mycursor.execute("delete from accounts where userid = %s",(id,))
     mycursor.execute("delete from users where userid = %s",(id,))
     dbconnected.commit()
     print("user delated successfully")





print("----SBI bank project---- ")
print(" 1. signup")
print(" 2. login")
print(" 3. exit")
choice = input("enter your choice :") 
if choice =="1":
    signup()
if choice =="2":
     login()

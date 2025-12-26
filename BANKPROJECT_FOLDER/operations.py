from main import connnectdb
def adddata(name, age, address):
     dbconnected=connnectdb()
     mycursor = dbconnected.cursor()
     mycursor.execute("INSERT INTO students(studentNames,studentAge,studentAdress)values(%s,%s,%s)",(name,age,address))
     dbconnected.commit()
     dbconnected.close()
     print("data added successfully")
def delate_data(age):
     dbconnected=connnectdb()
     mycursor = dbconnected.cursor()
     mycursor.execute("DELETE FROM STUDENTS WHERE studentAge = %s",(age,))
     dbconnected.commit()
     dbconnected.close()
     print("data delated scuccessfully")
def viewdata(table):
     dbconnected=connnectdb()
     mycursor = dbconnected.cursor()
     mycursor.execute(f"SELECT * FROM {table}")
     table_data=mycursor.fetchall()
     print(table_data)


    
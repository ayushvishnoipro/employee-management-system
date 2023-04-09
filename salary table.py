import mysql.connector as a
con=a.connect(host="localhost",
              user="root",
              passwd="xifr1234",
              database="employee")
sql="""create table salary
(ecode varchar(10),
name varchar(30),
year varchar(20),
month varchar(15),workingD integer,finalPay integer)"""
c=con.cursor()
c.execute(sql)

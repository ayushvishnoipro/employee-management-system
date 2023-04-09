import mysql.connector as a
con=a.connect(host="localhost",
              user="root",
              passwd="xifr1234",
              database="employee")
sql="""create table office
(ecode varchar(10),
name varchar(30),
post varchar(20),
joining varchar(10),
BasicPay integer)"""
c=con.cursor()
c.execute(sql)

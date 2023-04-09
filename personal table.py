import mysql.connector as a
con=a.connect(host="localhost",
              user="root",
              passwd="xifr1234",
              database="employee")
sql="""create table personal
(name varchar(10),
city varchar(30),
birthdate varchar(20),
phone varchar(15))"""
c=con.cursor()
c.execute(sql)


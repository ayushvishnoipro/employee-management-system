import mysql.connector as a
con=a.connect(host="localhost",
              user="root",
              passwd="xifr1234",
              database="employee")

def npersonal():
    n=input("enter employee name:")
    c=input("enter emloyee city name:")
    d=input("enter employee D.O.B.:")
    p=input("enter employee phone:")
    data=(n,c,d,p)
    sql='insert into personal values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data entered sucessfully")
    main()

def personal():
    sql="select * from personal"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()

def noffice():
    ec=input("enter employee code:")
    n=input("enter employee name:")
    ps=input("enter emloyee post:")
    j=input("enter employee's joinning date:")
    bp=int(input("enter assigned salary:"))
    data=(ec,n,ps,j,bp)
    sql='insert into office values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data entered sucessfully")
    main()


def office():
    sql="select * from office"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()
    
def nsalary():
    ec=input("enter employee code:")
    v=(ec,)
    sql="select BasicPay from office where Ecode=%s"
    c=con.cursor()
    c.execute(sql,v)
    bs=c.fetchone()
    n=input("enter employee name:")
    y=input("enter year for salary:")
    m=input("enter month for salary:")
    wd=int(input("enter working days in given month:"))
    td=int(input("enter total days in given month:"))
    fp=bs[0]/td*wd
    data=(ec,n,y,m,wd,fp)
    sql='insert into salary values(%s,%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data entered sucessfully")
    main()


def salary():
    sql="select * from salary"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()

def main():
    print("""
1.add new employee personal details
2.display employees personal details
3.add new emploee office details
4.display employees office details
5.enter salary details of employee
6.display  salary details of employee""")
    choice=input("enter task no:")
    while True:
        if(choice=='1'):
            npersonal()
        elif(choice=='2'):
            personal()
        elif(choice=='3'):
            noffice()
        elif(choice=='4'):
            office()
        elif(choice=='5'):
            nsalary()
        elif(choice=='6'):
            salary()
        else:
            print("wrong choice...........")
main()
            
              
        
            








    
    









    

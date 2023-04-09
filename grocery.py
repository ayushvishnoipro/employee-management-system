import mysql.connector
print("""
_________________________________
welcome to grocery management system
____________________________________
""")
mydb=mysql.connector.connect(host="127.0.0.1", user='root', password='xifr1234')
if mydb.is_connected():
    print("connected")
mycursor=mydb.cursor()
mycursor.execute('use store_vdo')
mycursor.execute('create table login(username varchar(25),password varchar(25))')
mycursor.execute("create table purchase(odate date not null, name varchar(25) not null,pcode int not null,amount int not null)")
mycursor.execute("create table stock(pcode int not null, pname varchar(25) not null, quantity int not null,price int not null)")
mydb.commit()
z=0 
mycursor.execute("select*from login")
for i in mycursor:
    z+=1
if(z==0):
    mycursor.execute("insert into login values('username','ng')")
    mydb.commit()
while True:
    print("""
1.ADMIN
2.CUSTOMER
3.EXIT
""")
    ch=input("enter yuor choice")
    if(ch==1):
     passs=input("enter password:")
     mycursor.execute("select* from login")
     for i in mycursor:
         username,password=i
         if(passs==password):
             print("welcome")
             loop2='y'
             while(loop2=='y' or loop2=='Y'):
                  print("""    1.add new item
2.updating price
3.deleting item
4.display all items
5.to change the password
6.log out
""")
             ch=int(input("enter your choice"))
             if(ch==1):
                  loop='y'
                  while(loop=='y'or loop=='Y'):
                       pcode=int(input("Enter product code: "))
                       pname=input("Enter product name: ")
                       quantity=int(input("Enter product quantity: "))
                       price=int(input("Enter product price: "))
                       mycursor.execute("insert into stock values('"+str(pcode)+"','"+pname+"','"+str(quantity)+"','"+str(price)+"'")
                       mydb.commit()
                       print("record successfully inserted")
                       loop=input("do you want to enter more items(y/n):")

                  loop2=input("do you want to continue adding editting more stock(y/n)")
                  
             elif(ch==2):
                 loop2='y'
                 while(loop2=='y' or loop2=='Y'):
                     pcode=int(input("enter product code"))
                     new_price=int(input("enter new price"))
                     mycursor.execute("update stock set price='"+newprice+"' where pcode='"+str(pcode)+"'")
                     mydb.commit()
                     loop=input("do you want to change the price of any other item(y/n):")
                 loop2=input("do you want to continue editting stock(y/n):")
                    
             elif(ch==3):
                loop='y'
                while(loop2=='y' or loop2=='Y'):
                    pcode=int(input("enter product code:"))
                    mycursor.execute("delete from stock where pcode='"+str(pcode)+"'")
                    mydb.comit()
                    loop=input("do you want to delete any data(y/n):")
                loop2=input("do you want to continue editting stock(y/n):")
                
             elif(ch==4):
                 mycursor.execute("select*from stock")
                 print("pcode||pname||quantity||price")
                 for i in mycursor:
                     t_code,t_name,t_quan,t_price=i
                     print(f"{t_code}||{t_name}||{t_quan}||{t_price}")

             elif(ch==5):
                old_passs=input("enter old password:")
                mycursor.execute("select*from login")
                for i in mycursor:
                    username,password=i
                if(old_passs==password):
                    new_passs=input("enter new password:")
                    mycursor.execute("update login set password='"+new_passs+"'")
                    mydb.commit()
            
             elif(ch==6):
                 break
         else:
                 print("wrong password")
   
                   


                
    elif(ch==2):
        print("""1.item bucket
2.payment
3.view available items
4.go back
""")
        ch2=int(input("enter your choice:"))
        if(ch2==1):
            name=input("enter your name")
            pcode=int(input("enter product code"))
            quantity=int(input("Enter product quantity: "))
            mycursor.execute("select * from stock where pcode='"+str(pcode)+"'")
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
            amount=t_price*quantity
            net_quan=t_quan-quantity
            mycursor.execute("update stock set quantity='"+str(net_quan)+"'where pcode='"+pcode+"'")
            mycursor.execute("insert intopurchase values(now(),'"+name+"','"+str(pcode)+"')")
            mydb.commit()
        
        elif(ch==2):
            print(f"amountto be paid{amount}")
        elif(ch2==3):
            print("CODE||NAME||PRICE")
            mycursor.execute("select * from stock")
            for i in mycursor:
                 t_code,t_name,t_quan,t_price=i
                 print(f"{t_code}||{t_name}||{t_price}")

        elif(ch2==4):
            break
    elif(ch==3):
        break








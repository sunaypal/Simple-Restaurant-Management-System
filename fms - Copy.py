from tkinter import *
import random
import time
import datetime

def choose():
    print('''ENTER WHAT YOU WANT TO EAT(e.g. 2)
1.INDIAN
2.CHINESE
3.SNACKS
4.ICE CREAM
5.DRINKS
6.DESSERTS
7.CLOSE''')
    a=int(input(""))
    global s
    s=0
    global p
    global q
    global r
    
#MENU

    if a==1:
        print('''                    MENU
Item#                                          Price#
1.Roti                                         4(per piece)
2.Paratha                                      6(per piece)
3.Puri                                         10(4 pieces)
4.Aloo dum                                     40
5.Paneer tikka                                 10(per piece)
6.Chana                                        40
7.Chilli Paneer                                50
8.Fried rice                                   40
9.Chilli chicken                               50
10.Chicken(normal)                             45
11.Rumali roti                                 5(per piece)
12.Chicken kabab                               30
13.Fish finger                                 15
14.Fish curry                                  45
15.Biriyani                                    70
16.Mutton Biriyani                             80
17.Mutton(normal)                              60
18.Chicken Roll                                30
19.Egg Roll                                    25
20.Egg Chicken Roll                            35''')
        a1,b1=1,4
        a2,b2=2,6
        a3,b3=3,10 
        a4,b4=4,40   
        a5,b5=5,10
        a6,b6=6,40 
        a7,b7=7,50
        a8,b8=8,40
        a9,b9=9,50
        a10,b10=10,45
        a11,b11=11,5
        a12,b12=12,30
        a13,b13=13,15
        a14,b14=14,45
        a15,b15=15,70
        a16,b16=16,80
        a17,b17=17,60
        a18,b18=18,30
        a19,b19=19,25
        a20,b20=20,35
        c1="Roti"
        c2="Paratha"
        c3="Puri"
        c4="Aloo Dum"
        c5="Paneer Tikka"
        c6="Chana"
        c7="Chilli Paneer"
        c8="Fried Rice"
        c9="Chilli Chicken"
        c10="Chicken(normal)"
        c11="Rumali Roti"
        c12="Chicken kabab"
        c13="Fish finger"
        c14="Fish Curry"
        c15="Biriyani"
        c16="Mutton Biriyani"
        c17="Mutton (Normal)"
        c18="Chicken Roll"
        c19="Egg Roll"
        c20="Egg Chicken Roll"
        b=int(input("select the dish of your choice->"))
        c=int(input("enter number of dishes->"))
        if a1==b:
            s+=(c*b1)
            p.append(c1)
            q+=str(c)
        elif a2==b:
            s+=c*b2
            p.append(c2)
            q+=str(c)
        elif a3==b:
            s+=c*b3
            p.append(c3)
            q+=str(c) 
        elif a4==b:
            s+=c*b4
            p.append(c4)
            q+=str(c)  
        elif a5==b:
            s+=c*b5
            p.append(c5)
            q+=str(c) 
        elif a6==b:
            s+=c*b6
            p.append(c6)
            q+=str(c) 
        elif a7==b:
            s+=c*b7
            p.append(c7)
            q+=str(c) 
        elif a8==b:
            s+=c*b8
            p.append(c8)
            q+=str(c)
        elif a9==b:
            s+=c*b9
            p.append(c9)
            q+=str(c) 
        elif a10==b:
            s+=c*b10
            p.append(c10)
            q+=str(c)
        elif a11==b:
            s+=c*b11
            p.append(c11)
            q+=str(c)
        elif a12==b:
            s+=c*b12
            p.append(c12)
            q+=str(c)
        elif a13==b:
            s+=c*b13
            p.append(c13)
            q+=str(c)
        elif a14==b:
            s+=c*b14
            p.append(c14)
            q+=str(c) 
        elif a15==b:
            s+=c*b15
            p.append(c15)
            q+=str(c) 
        elif a16==b:
            s+=c*b16
            p.append(c16)
            q+=str(c) 
        elif a17==b:
            s+=c*b17
            p.append(c17)
            q+=str(c) 
        elif a18==b:
            s+=c*b18
            p.append(c18)
            q+=str(c) 
        elif a19==b:
            s+=c*b19
            p.append(c19)
            q+=str(c)  
        elif a20==b:
            s+=c*b20
            p.append(c20)
            q+=str(c) 
        else:
            print("choose the correct number->")
        print("total amount->",s)
    elif a==2:
        print('''                    MENU
Item#                                        Price#
1.Veg Chowmin                                70
2.Chicken Chowmin                            80 
3.Egg Chowmin                                75 
4.Veg Momo                                   45
5.Chicken Momo                               50
6.Manchurian                                 60 ''')
        a1,b1=1,70
        a2,b2=2,80
        a3,b3=3,75 
        a4,b4=4,45   
        a5,b5=5,50
        a6,b6=6,60  
        c1="Veg Chowmin"
        c2="Chicken Chowmin"
        c3="Egg Chowmin"
        c4="Veg Momo"
        c5="Chicken Momo"
        c6="Manchurian"
        b=int(input("select the dish of your choice->"))
        c=int(input("enter number of dishes->"))
        if a1==b:
            s+=(c*b1)
            p.append(c1)
            q+=str(c)
        elif a2==b:
            s+=c*b2
            p.append(c2)
            q+=str(c)
        elif a3==b:
            s+=c*b3
            p.append(c3)
            q+=str(c) 
        elif a4==b:
            s+=c*b4
            p.append(c4)
            q+=str(c)  
        elif a5==b:
            s+=c*b5
            p.append(c5)
            q+=str(c) 
        elif a6==b:
            s+=c*b6
            p.append(c6)
            q+=str(c) 
        else:
            print("choose the correct number")
        print("total amount->",s)
    elif a==3:
        print('''                    MENU
Item#                                       Price#
1.Lays                                      10
2.Good Day                                  10
3.Bourbon                                   25
4.Cream Cracker Biscuit                     10
5.Kurkure                                   10
6.Popcorn                                   15
7.Cotton Candy                              15
8.Dairy Milk                                50 
9.Bournville                                60
10.Kitkat                                   50
11.Haldiram Groundnuts                      45
12.Chocolate Cake                           30''')
        a1,b1=1,10
        a2,b2=2,10
        a3,b3=3,25 
        a4,b4=4,10  
        a5,b5=5,10
        a6,b6=6,15 
        a7,b7=7,15
        a8,b8=8,50
        a9,b9=9,60
        a10,b10=10,50
        a11,b11=11,45
        a12,b12=12,30
        c1="Lays"
        c2="Good Day"
        c3="Bourbon"
        c4="Cream Cracker Biscuit"
        c5="Kurkure"
        c6="Popcorn"
        c7="Cotton Candy"
        c8="Dairy Milk"
        c9="Bournville"
        c10="Kit Kat"
        c11="Haldiram Groundnuts"
        c12="Chocolate Cake"
        b=int(input("select your choice->"))
        c=int(input("how many?"))
        if a1==b:
            s+=(c*b1)
            p.append(c1)
            q+=str(c)
        elif a2==b:
            s+=c*b2
            p.append(c2)
            q+=str(c)
        elif a3==b:
            s+=c*b3
            p.append(c3)
            q+=str(c) 
        elif a4==b:
            s+=c*b4
            p.append(c4)
            q+=str(c)  
        elif a5==b:
            s+=c*b5
            p.append(c5)
            q+=str(c) 
        elif a6==b:
            s+=c*b6
            p.append(c6)
            q+=str(c) 
        elif a7==b:
            s+=c*b7
            p.append(c7)
            q+=str(c) 
        elif a8==b:
            s+=c*b8
            p.append(c8)
            q+=str(c)
        elif a9==b:
            s+=c*b9
            p.append(c9)
            q+=str(c) 
        elif a10==b:
            s+=c*b10
            p.append(c10)
            q+=str(c)
        elif a11==b:
            s+=c*b11
            p.append(c11)
            q+=str(c)
        elif a12==b:
            s+=c*b12
            p.append(c12)
            q+=str(c)
        else:
            print("choose the correct number")
        print("total amount->",s)
    elif a==4:
        print('''                    MENU
Item#                                         Price#
1.Choco Bar                                   10
2.Cornetto                                    30
3.Vanilla(cup)                                15
4.Chocolate(cup)                              15
5.Butter scotch(cup)                          15
6.Mango Flavour                               10
7.Orange Flavour                              10
8.Kulfi                                       10''')
        a1,b1=1,10
        a2,b2=2,30
        a3,b3=3,15 
        a4,b4=4,15  
        a5,b5=5,15
        a6,b6=6,10 
        a7,b7=7,10
        a8,b8=8,10
        c1="Choco Bar"
        c2="Cornetto  "
        c3="Vanilla(cup) "
        c4="Chocolate(cup)"
        c5="Butter Scotch(cup)"
        c6="Mango Flavour"
        c7="Orange Flavour"
        c8="Kulfi"
        b=int(input("select your choice->"))
        c=int(input(" how many?"))
        if a1==b:
            s+=(c*b1)
            p.append(c1)
            q+=str(c)
        elif a2==b:
            s+=c*b2
            p.append(c2)
            q+=str(c)
        elif a3==b:
            s+=c*b3
            p.append(c3)
            q+=str(c) 
        elif a4==b:
            s+=c*b4
            p.append(c4)
            q+=str(c)  
        elif a5==b:
            s+=c*b5
            p.append(c5)
            q+=str(c) 
        elif a6==b:
            s+=c*b6
            p.append(c6)
            q+=str(c) 
        elif a7==b:
            s+=c*b7
            p.append(c7)
            q+=str(c) 
        elif a8==b:
            s+=c*b8
            p.append(c8)
            q+=str(c)
        else:
            print("choose the correct number")
        print("total amount->" ,s)
    elif a==5:
        print('''                    MENU
Item#                                         Price#  
1.Mineral Water(500ml)                        20 
2.Thumps up(500ml)                            35  
3.Coca-Cola(500ml)                            40
4.Pepsi(500ml)                                40
5.Limca(500ml)                                40
6.Sprite(500ml)                               45
7.Mountain Dew(500ml)                         45
8.Maaza(500ml)                                45
9.Tea                                         5
10.Green Tea                                  6
11.Black Tea                                  5
12.Lemon Tea                                  5
13.Coffee                                     10
14.Black Coffee                               10
15.Cold Coffee                                10
16.Lemon Squash                               10
17.Lassi                                      10
18.Fruit Juice                                15''')
        a1,b1=1,20
        a2,b2=2,35
        a3,b3=3,40 
        a4,b4=4,40  
        a5,b5=5,40
        a6,b6=6,45 
        a7,b7=7,45
        a8,b8=8,45
        a9,b9=9,5
        a10,b10=10,6
        a11,b11=11,5
        a12,b12=12,5
        a13,b13=13,10
        a14,b14=14,10
        a15,b15=15,10
        a16,b16=16,10
        a17,b17=17,10
        a18,b18=18,15
        c1="Mineral Water "
        c2="Thumps Up"
        c3="Coca-Cola"
        c4="Pepsi"
        c5="Limca"
        c6="Sprite"
        c7="Mountain Dew"
        c8="Maaza"
        c9="Tea"
        c10="Green Tea"
        c11="Black Tea"
        c12="Lemon Tea"
        c13="Coffee"
        c14="Black Coffe"
        c15="Cold Coffee"
        c16="Lemon Squash"
        c17="Lassi"
        c18="Fruit Juice"
        b=int(input("select your choice->"))
        c=int(input("how many?"))
        if a1==b:
            s+=(c*b1)
            p.append(c1)
            q+=str(c)
        elif a2==b:
            s+=c*b2
            p.append(c2)
            q+=str(c)
        elif a3==b:
            s+=c*b3
            p.append(c3)
            q+=str(c) 
        elif a4==b:
            s+=c*b4
            p.append(c4)
            q+=str(c)  
        elif a5==b:
            s+=c*b5
            p.append(c5)
            q+=str(c) 
        elif a6==b:
            s+=c*b6
            p.append(c6)
            q+=str(c) 
        elif a7==b:
            s+=c*b7
            p.append(c7)
            q+=str(c) 
        elif a8==b:
            s+=c*b8
            p.append(c8)
            q+=str(c)
        elif a9==b:
            s+=c*b9
            p.append(c9)
            q+=str(c) 
        elif a10==b:
            s+=c*b10
            p.append(c10)
            q+=str(c)
        elif a11==b:
            s+=c*b11
            p.append(c11)
            q+=str(c)
        elif a12==b:
            s+=c*b12
            p.append(c12)
            q+=str(c)
        elif a13==b:
            s+=c*b13
            p.append(c13)
            q+=str(c)
        elif a14==b:
            s+=c*b14
            p.append(c14)
            q+=str(c) 
        elif a15==b:
            s+=c*b15
            p.append(c15)
            q+=str(c) 
        elif a16==b:
            s+=c*b16
            p.append(c16)
            q+=str(c) 
        elif a17==b:
            s+=c*b17
            p.append(c17)
            q+=str(c) 
        elif a18==b:
            s+=c*b18
            p.append(c18)
            q+=str(c) 
        else:
           print("choose the correct number")
        print("total amount->" ,s)
    elif a==6:
        print('''                    MENU
Item#                                         Price(per pc)#
1.Gulab Jamun                                 5 
2.Kaju Barfi                                  5
3.Rasgulla                                    5
4.Rasmalai                                    10
5.Cham Cham                                   5
6.Laddu                                       10 
7.Sandesh                                     5
8.Sonpapdi                                    6
''')
        a1,b1=1,5
        a2,b2=2,5
        a3,b3=3,5 
        a4,b4=4,10  
        a5,b5=5,5
        a6,b6=6,10 
        a7,b7=7,5
        a8,b8=8,6
        c1="Gulag Jamun"
        c2="Kaju Barji"
        c3="Rasgulla"
        c4="Rasmalai"
        c5="Cham Cham"
        c6="Laddu"
        c7="Sandesh"
        c8="Sonpapdi"
        b=int(input("select the sweet of your choice->"))
        c=int(input("enter number of sweets->"))
        if a1==b:
            s+=(c*b1)
            p.append(c1)
            q+=str(c)
        elif a2==b:
            s+=c*b2
            p.append(c2)
            q+=str(c)
        elif a3==b:
            s+=c*b3
            p.append(c3)
            q+=str(c) 
        elif a4==b:
            s+=c*b4
            p.append(c4)
            q+=str(c)  
        elif a5==b:
            s+=c*b5
            p.append(c5)
            q+=str(c) 
        elif a6==b:
            s+=c*b6
            p.append(c6)
            q+=str(c)
        elif a7==b:
            s+=c*b7
            p.append(c7)
            q+=str(c) 
        elif a8==b:
            s+=c*b8
            p.append(c8)
            q+=str(c)    
        else:
            print("choose the correct number")
        print("total amount->" ,s)
    elif a==7:
         print('''


        THANK YOU
              VISIT AGAIN''')
    else:
        print("INVALID NUMBER")

#--------------------------------------------------------------------------------
def choice():
    print('''
1.Continue
2.Finished''')
    g=int(input("Enter your choice->"))
    if g==1:
        choose()
        global f
        f+=s
        choice()
    elif g==2:
        print("""
grand total->""",f)
        print("""
select the mode of payment->
1.Cash
2.Credit/Debit card
3.paytm/paypal/googlepay(5% discount on grand total)""")
        m=int(input())
        global w
        if m==3:
            w=f-(0.05*f)
        elif m==1 or m==2:
            w=f
        else:
            print("other modes are not available")
        print("""
net amount payable->""",w)
    else:
        print("choose correct option" )
        choice()
def Receipt():
    roor = Tk()
    roor.geometry("600x700+0+0")

    f1 = Frame(roor, width = 1600, height = 700, bd = 12, relief = "raise")
    f1.pack()
    lblReceipt = Label(f1, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
    lblReceipt.grid(row=0, column=0, sticky=W)
    txtReceipt = Text(f1, width=64, height=35, bg="white", bd=8, font=('arial', 11, 'bold'))
    txtReceipt.grid(row=1, column=0)
    txtReceipt.delete("1.0", END)
    o=random.randint(1000,9999)
    txtReceipt.insert(END, 'BILL NUMBER-->' + str(o)+"\n")
    localtime=time.asctime(time.localtime(time.time()))
    txtReceipt.insert(END, 'DATE-->'+str(localtime)+"\n\n")                 
    txtReceipt.insert(END, 'CUSTOMER NAME-->'+str(cn)+"\n\n")
    txtReceipt.insert(END, 'Items\t\t\t\t' + "No. of Items \n\n")
    
    for i in range(0,len(p)):
        txtReceipt.insert(END, p[i]+'\t\t\t\t' +q[i]+ "\n\n")
    txtReceipt.insert(END,"Total Cost-->\t\t\t\t"+str(f)+"\n\n")   
    txtReceipt.insert(END,"Amount Payable-->\t\t\t\t"+str(w)+"\n\n")
    roor.mainloop()

def database():
    import mysql.connector as wi
    global cn
    mydb=wi.connect(host='localhost',user='root',passwd='1234')
    y=mydb.cursor()
    cn=input('enter your name')
    x=wi.connect(host='localhost',user='root',passwd='1234',database='baban')
    a=x.cursor()
    x.commit()
##------------------------------MAIN-----------------------------------------------

localtime=time.asctime(time.localtime(time.time()))
print(localtime)

##------------------------------body-----------------------------------------------
cn=''
database()
p=[]
q=[]

print("""
                              FOOD MANAGEMENT SYSTEM """)
print("                             WELCOME TO PAL'S KITCHEN ")
f=0
choose()
f+=s
choice()
v=input("Want receipt?(y/n)")
if v=="y":
    Receipt()
elif v!="n":
    print("choose correct option")

print('''


        THANK YOU
              VISIT AGAIN''')

import mysql.connector as wi
j=localtime
mydb=wi.connect(host='localhost',user='root',passwd='1234')
kl=mydb.cursor()
kl.execute('use baban')
rt=wi.connect(host='localhost',user='root',passwd='1234',database='baban')
a=rt.cursor()   
a.execute("insert into Reg(customer_name,date_of_visit) values('{}','{}')".format(cn,j))
rt.commit()
   


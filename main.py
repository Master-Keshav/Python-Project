# Main
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="system",database="mydatabase")
mycursor = mydb.cursor()
import tkinter
from tkinter import *
import tkinter as tk
myw=tk.Tk()
myw.geometry('1525x1000')
myw.title("Project HMS")
myw.state('zoomed')
from PIL import ImageTk, Image

# ----------------------  Database Part --------------------------------------------

import datetime as dt
import copy
import mysql.connector 
from mysql.connector import Error
def camp_info(cursor):
    ls = []
    cursor.execute('select event_name from all_events')
    for i in cursor:
        ls.append(i[0])

    return ls
def event_timings(cursor):
    ls = []
    cursor.execute('select event_stime,event_etime from all_events')
    for i in cursor:
        ll=[]
        ll.append(i[0])
        ll.append(i[1])
        ls.append(ll)
    return ls
def event_place(cursor):
    ls = []
    cursor.execute('select event_place from all_events')
    for i in cursor:
        ls.append(i[0])

    return ls
def event_date(cursor):
    ls = []
    cursor.execute('select event_date from all_events')
    for i in cursor:
        ls.append(i[0])

    return ls
def convert_deltatime(delta):
    s = int(delta.total_seconds())
    hh = s//3600
    s%=3600
    mm = s//60
    s%=60
    ss = s
  
    d_time = dt.time(hh,mm,ss)
    d_s = d_time.strftime('%I:%M %p')
    return d_s
def give_info(cursor):
    en = camp_info(cursor)
    et = event_timings(cursor)
    ep = event_place(cursor)
    ed = event_date(cursor)
    index = -1
    dd = dt.date.today()
    print(dd)
    for i in range(len(ed)):
        if dd == ed[i]:
            #print(ed[i])
            index=i
            break

    if index!=-1:
        print(en[index],et[index],ep[index],ed[index])
        stime = convert_deltatime(et[index][0])
        etime = convert_deltatime(et[index][1])
        print(stime,etime)
        date_format = ed[index].strftime('%B %d, %Y')
        print(date_format)
        index=-1
        inf = f"Free {en[index]} Check Up Camp is being organised on {date_format} from {stime} to {etime} at {ep[index]} ."
        return inf
  
    return ""
def all_events(cursor):
    en = camp_info(cursor)
    et = event_timings(cursor)
    ep = event_place(cursor)
    ed = event_date(cursor)

    n = len(en)
    lis = []
    cur_date = dt.date.today()
    for i in range(n):
        print(ed[i],ed[i] > cur_date)
        if ed[i] >= cur_date:
            stime = convert_deltatime(et[i][0])
            etime = convert_deltatime(et[i][1])
        
            date_format = ed[i].strftime('%B %d, %Y')
            ss = f"Free {en[i]} Check Up Camp is being organised on {date_format} from {stime} to {etime} at {ep[i]} ."
            lis.append(ss)

        
    return lis
def check_info(cursor):
    inf = give_info(cursor)
    global infs
    if inf == "":
        p=dt.date.today()
        infs="No Camps Available Today! Check For Furthur Available Camps"
    else:
        infs=inf

import getpass

conn = mysql.connector.connect(user='root',password='system',host='localhost',database='mydatabase')
cursor = conn.cursor()
infs=''
check_info(cursor)


# --------------------   Background Image Part -----------------------
myimage=Image.open("Hospital.png")
myimage=myimage.resize((1525,800))
img=ImageTk.PhotoImage(myimage)
label=tk.Label(myw,image=img)
label.pack()

# Functional Part   

lb1=Label(myw,text="Hospital Management System",bg='gold')
lb1.place(x=50,y=40)
lb1.config(font=('Helvatical bold',80))

def Apt():
    newWindow = Toplevel(myw)
    newWindow.title("Appointment")
    # Booking Appointments
    newWindow.configure(bg='gold')
    newWindow.geometry('1525x1000')
    newWindow.state('zoomed')

    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="system",database="mydatabase")
    mycursor = mydb.cursor()
    # mycursor.execute("Create Database mydatabase")
    # mycursor.execute("Drop Table IF exists appointment")
    # mycursor.execute("Create table appointment(id int Auto_Increment Primary Key,fname VARCHAR(50),lname VARCHAR(50),phone int,age int, gender varchar(20),doctor varchar(50))")

    a=""
    b=""
    c=""
    d=""
    e=""
    f=""

    lb1=Label(newWindow,text="Appointment Window",bg='red')
    lb1.place(x=350,y=20)
    lb1.config(font=('Helvatical bold',60))

    lb2 = Label(newWindow,text="First Name",bg='light green')
    lb2.place(x=60,y=200)
    lb2.config(font=('Helvatical bold',25))
    e2=Entry(newWindow,bg='light blue')
    e2.place(x=400,y=200)
    e2.config(font=('Helvatical bold',25))

    lb6 = Label(newWindow,text="Last Name",bg='light green')
    lb6.place(x=850,y=200)
    lb6.config(font=('Helvatical bold',25))
    e6=Entry(newWindow,bg='light blue')
    e6.place(x=1050,y=200)
    e6.config(font=('Helvatical bold',25))

    lb3 = Label(newWindow,text="Phone Number",bg='light green')
    lb3.place(x=60,y=300)
    lb3.config(font=('Helvatical bold',25))
    e3=Entry(newWindow,bg='light blue')
    e3.place(x=400,y=300)
    e3.config(font=('Helvatical bold',25))

    lb4 = Label(newWindow,text="Age",bg='light green')
    lb4.place(x=850,y=300)
    lb4.config(font=('Helvatical bold',25))
    e4=Entry(newWindow,bg='light blue')
    e4.place(x=1050,y=300)
    e4.config(font=('Helvatical bold',25))

    myvar1=IntVar()
    myvar2=IntVar()
    myvar3=IntVar()
    myvar4=IntVar()
    myvar5=IntVar()
    myvar6=IntVar()
    lb5 = Label(newWindow,text="Select Gender",bg='light green')
    lb5.place(x=60,y=400)
    lb5.config(font=('Helvatical bold',25))
    rb1=Radiobutton(newWindow,text="Male",variable=myvar1,value=0,width=15,anchor='w',bg='blue')
    rb1.place(x=400,y=400)
    rb1.config(font=('Helvatical bold',25))
    rb2=Radiobutton(newWindow,text="Female",variable=myvar1,value=1,width=15,anchor='w',bg='pink')
    rb2.place(x=750,y=400)
    rb2.config(font=('Helvatical bold',25))
    rb3=Radiobutton(newWindow,text="Transgender",variable=myvar1,value=2,width=15,anchor='w',bg='orange')
    rb3.place(x=1100,y=400)
    rb3.config(font=('Helvatical bold',25))


    f1 = Frame(newWindow)
    f1.place(x=400,y=500)
    lb5 = Label(newWindow,text="Select Doctor",bg='light green')
    lb5.place(x=60,y=500)
    lb5.config(font=('Helvatical bold',25))
    cb1=Checkbutton(f1,text="Cardiologist",variable=myvar2,onvalue=100,offvalue=0,width=15,anchor='w',bg='grey')
    cb1.grid(row=1)
    cb1.config(font=('Helvatical bold',25))
    cb2=Checkbutton(f1,text="Audiologist",variable=myvar3,onvalue=30,offvalue=0,width=15,anchor='w',bg='grey')
    cb2.grid(row=2)
    cb2.config(font=('Helvatical bold',25))
    cb3=Checkbutton(f1,text="Dentist",variable=myvar4,onvalue=50,offvalue=0,width=15,anchor='w',bg='grey')
    cb3.grid(row=3)
    cb3.config(font=('Helvatical bold',25))
    cb4=Checkbutton(f1,text="Gynaecologist",variable=myvar5,onvalue=60,offvalue=0,width=15,anchor='w',bg='grey')
    cb4.grid(row=4)
    cb4.config(font=('Helvatical bold',25))
    cb5=Checkbutton(f1,text="Paediatrician",variable=myvar6,onvalue=20,offvalue=0,width=15,anchor='w',bg='grey')
    cb5.grid(row=5)
    cb5.config(font=('Helvatical bold',25))

    def enter(t):
         query="INSERT into appointment(fname,lname,phone,age,gender,doctor) values(%s,%s,%s,%s,%s,%s)"
         val=(t[0],t[1],t[2],t[3],t[4],t[5])
         mycursor.execute(query,val)
         mycursor.execute("SELECT * FROM appointment")
         myresult=mycursor.fetchall()
         for x in myresult:
            print(x)
         mydb.commit()
    def submit():
        a=e2.get()
        b=e6.get()
        c=str(e3.get())
        d=str(e4.get())
        if myvar1.get()==0:
            e="Male"
        if myvar1.get()==1:
            e="Female"
        if myvar1.get()==2:
            e="Transgender"
        if myvar2.get()!=0:
            f="Cardiologist"
        if myvar3.get()!=0:
            f="Audiologist"
        if myvar4.get()!=0:
            f="Dentist"
        if myvar5.get()!=0:
            f="Gynaecologist"
        if myvar6.get()!=0:
            f="Paediatrician"
        val=(a,b,c,d,e,f)
        enter(val)
        lb7 = Label(newWindow,text=val,bg='light green')
        lb7.place(x=900,y=700)
        lb7.config(font=('Helvatical bold',30))

    btn1 = Button(newWindow,text ="Submit Details",command = submit,bg='red')
    btn1.config(font=('Helvatical bold',25))
    btn1.place(x=1000,y=600)


    btn2 = Button(newWindow, text="Go To Home Page", command=newWindow.destroy,bg='teal')
    btn2.config(font=('Helvatical bold',25))
    btn2.place(x=60,y=600)
    mainloop()

btn1 = Button(myw,text ="Book An Appointment Now",command = Apt,bg='red')
btn1.config(font=('Helvatical bold',30))
btn1.place(x=60,y=250)

count = 0
def beds():
        newWindow = Toplevel(myw)
        newWindow.title("Appointment")
        newWindow.configure(bg='gold')
        newWindow.geometry('600x400')

        lb1=Label(newWindow,text="Beds Available : -----------------------",bg='light green')
        lb1.place(x=60,y=230)
        lb1.config(font=('Helvatical bold',20))

        lb2=Label(newWindow,text="Total 4 Wards: A B C D",bg='light blue')
        lb2.place(x=60,y=20)
        lb2.config(font=('Helvatical bold',20))
        lb3=Label(newWindow,text="In 1 Ward - 25 Beds Available",bg='light blue')
        lb3.place(x=60,y=90)
        lb3.config(font=('Helvatical bold',20))

        def beds():
            global count
            count = count + 1
            if count>100 :
                lb1.config(text="Beds Not Avialable!, Sorry For The Inconvenience!")
            if 0<count<=25:
                lb1.config(text="Beds Available:- Ward:A, BED:"+str(count))
            if 25<count<=50:
                lb1.config(text="Beds Available:- Ward:B, BED:"+str(count-25))
            if 50<count<=75:
                lb1.config(text="Beds Available:- Ward:C, BED:"+str(count-50))
            if 75<count<=100:
                lb1.config(text="Beds Available:- Ward:D, BED:"+str(count-75))

        btn1 = Button(newWindow,text ="Check Beds Available",command = beds,bg='red')
        btn1.config(font=('Helvatical bold',20))
        btn1.place(x=60,y=160)

        lb4=Label(newWindow,text="* Note Them For Furthur Details",bg='cyan')
        lb4.place(x=400,y=180)
        lb4.config(font=('Helvatical bold',10))

        btn2 = Button(newWindow, text="Go To Home Page", command=newWindow.destroy,bg='teal')
        btn2.config(font=('Helvatical bold',20))
        btn2.place(x=60,y=300)

        mainloop()

btn2 = Button(myw,text ="Beds Available",command = beds,bg='light blue')
btn2.config(font=('Helvatical bold',30))
btn2.place(x=1100,y=250)

def med():
    import tkinter.font as tkFont
    mw = Tk()
    font_ = tkFont.Font(family='PT Mono',size=20,weight='bold')
    mw.geometry('700x280')
    mw.configure(bg='#191970')

    fr2 = Frame(mw)
    fr2.grid(row=1,column=1)
    listbox = Listbox(fr2, width=60, height=16, selectmode=MULTIPLE,bg="light green")
    listbox.insert(1, "Azithromycin")
    listbox.insert(2, "Chloroquine Phosphate")
    listbox.insert(3, "Malorone")
    listbox.insert(4, "Vibramycin")
    listbox.insert(5, "Acetaminophen")
    listbox.insert(6, "Ibuprofen")
    listbox.insert(7, "Paracetamol")
    listbox.insert(8, "Chlorothiazide")
    listbox.insert(9, "Chlorthalidone")
    listbox.insert(10, "Amlodipine")
    listbox.insert(11, "Benazepril")
    listbox.insert(12, "Acebutolol")
    listbox.insert(13, "Amiloride")
    listbox.insert(14, "Rifaximin")
    listbox.insert(15, "Rifamycin")
    listbox.insert(16, "Ciprofloxacin")
    lb1 = Label(fr2,height=5,width=50,bg='#cc86ff')
    lb1.grid(row=0,column=2)
    def get_items():

        lis = []
        for i in listbox.curselection():
            lis.append(listbox.get(i))
        tp=0
        listbox.selection_clear(0,int(listbox.size()-1))
        lis_stock_out=[]
        for i in lis:
            query = f"select price,quantity,name from medicines where name='{i}'"
            cursor.execute(query)
            for j in cursor:
                val = j[0]
                tp+=val
                qval = j[1]
                if qval < 100:
                    lis_stock_out.append(j[2])
                else:
                    tp+=val
                    qval-=5
                    query_2 = f"update medicines set quantity = {qval} where name = '{j[2]}'"
                    cursor.execute(query_2)  
            conn.commit()     
        rs = u"\u20B9"
        if len(lis_stock_out)==0:

            lb1.config(text=f"You need to pay {rs}{tp:.2f} only.")
        else:
            ss = 'These Medicines are out of Stock.'
            yy=""
            for i in range(len(lis_stock_out)):
                if i==len(lis_stock_out)-1:
                    yy+=lis_stock_out[i]
                else:
                    yy+=lis_stock_out[i]
                    yy+=","
            print(ss+'---'+yy+'.  Contact dealer to order more...')
            fs = f" You need to pay {rs}{tp:.2f} only for rest of the medicines."
            lb1.config(text=fs)

    btn = Button(fr2, text='Buy', command=get_items,bg='orange')
    btn.grid(row=1,column=0)
    listbox.grid(row=0,column=0)
    btn7 = Button(mw,text="Back", command=mw.destroy,bg='red')
    btn7.config(font=('Helvatical bold',30))
    btn7.place(x=450,y=200)
    mainloop()

btn3 = Button(myw,text ="Buy Medicines",command = med,bg='light green')
btn3.config(font=('Helvatical bold',30))
btn3.place(x=60,y=400)

def doctor():
        newWindow=Toplevel(myw)
        newWindow.configure(bg='gold')
        newWindow.geometry('1525x1000')
        newWindow.title("Doctor's Data")
        newWindow.state('zoomed')

        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="system",database="mydatabase")
        mycursor = mydb.cursor()

        a=""

        lb1=Label(newWindow,text="Doctor Details",bg='red')
        lb1.place(x=450,y=20)
        lb1.config(font=('Helvatical bold',60))

        var=IntVar()

        lb6 = Label(newWindow,text="Select Speciality :-",bg='light green')
        lb6.place(x=50,y=225)
        lb6.config(font=('Helvatical bold',30))
        rb1=Radiobutton(newWindow,text="Cardiologist",variable=var,value=1,width=20,anchor='w',bg='teal')
        rb1.place(x=400,y=200)
        rb1.config(font=('Helvatical bold',18))
        rb2=Radiobutton(newWindow,text="Audiologist",variable=var,value=2,width=20,anchor='w',bg='violet')
        rb2.place(x=800,y=200)
        rb2.config(font=('Helvatical bold',18))
        rb3=Radiobutton(newWindow,text="Dentist",variable=var,value=3,width=20,anchor='w',bg='cyan')
        rb3.place(x=1200,y=200)
        rb3.config(font=('Helvatical bold',18))
        rb4=Radiobutton(newWindow,text="Gynaecologist",variable=var,value=4,width=20,anchor='w',bg='purple')
        rb4.place(x=600,y=275)
        rb4.config(font=('Helvatical bold',18))
        rb5=Radiobutton(newWindow,text="Paediatrician",variable=var,value=5,width=20,anchor='w',bg='purple')
        rb5.place(x=1000,y=275)
        rb5.config(font=('Helvatical bold',18))

        def show():
            if var.get()==1:
                mycursor.execute("select * from doc where speciality = 'Cardiologist'")
            if var.get()==2:
                mycursor.execute("select * from doc where speciality = 'Audiologist'")
            if var.get()==3:
                mycursor.execute("select * from doc where speciality = 'Dentist'")
            if var.get()==4:
                mycursor.execute("select * from doc where speciality = 'Gynaecologist'")
            if var.get()==5:
                mycursor.execute("select * from doc where speciality = 'Paediatrician'")
            myresult=mycursor.fetchall()
            a=0
            for x in myresult:
                print(x)
                lb2 = Label(newWindow,text=x,bg='pink')
                lb2.place(x=100,y=400+a)
                lb2.config(font=('Helvatical bold',30))
                a+=70
        btn2 = Button(newWindow,text ="Show Details",command = show,bg='red')
        btn2.config(font=('Helvatical bold',25))
        btn2.place(x=450,y=650)

        btn1 = Button(newWindow,text ="Go Back",command = newWindow.destroy,bg='red')
        btn1.config(font=('Helvatical bold',25))
        btn1.place(x=700,y=650)

        mainloop()
       
btn4 = Button(myw,text ="Search Doctor",command = doctor,bg='magenta')
btn4.config(font=('Helvatical bold',30))
btn4.place(x=60,y=550)

def pat():
        newWindow=Toplevel(myw)
        newWindow.configure(bg='gold')
        # Patients Data
        newWindow.geometry('1525x1000')
        newWindow.title('Patients Data')
        newWindow.state('zoomed')

        import mysql.connector
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="system",database="mydatabase")
        mycursor = mydb.cursor()
        # mycursor.execute("Create Database mydatabase")
        # sql = "Drop Table IF exists patient"
        # mycursor.execute(sql)
        # mycursor.execute("Create table patient(fname VARCHAR(50),lname VARCHAR(50),phone int,age int, gender varchar(20),ward varchar(50),room varchar(50))")


        a=""
        b=""
        c=""
        d=""
        e=""
        f=""

        lb1=Label(newWindow,text="Patients Booking Detail",bg='red')
        lb1.place(x=350,y=20)
        lb1.config(font=('Helvatical bold',60))

        lb2 = Label(newWindow,text="First Name",bg='light green')
        lb2.place(x=60,y=200)
        lb2.config(font=('Helvatical bold',25))
        e2=Entry(newWindow,bg='light blue')
        e2.place(x=400,y=200)
        e2.config(font=('Helvatical bold',25))

        lb6 = Label(newWindow,text="Last Name",bg='light green')
        lb6.place(x=850,y=200)
        lb6.config(font=('Helvatical bold',25))
        e6=Entry(newWindow,bg='light blue')
        e6.place(x=1050,y=200)
        e6.config(font=('Helvatical bold',25))

        lb3 = Label(newWindow,text="Phone Number",bg='light green')
        lb3.place(x=60,y=300)
        lb3.config(font=('Helvatical bold',25))
        e3=Entry(newWindow,bg='light blue')
        e3.place(x=400,y=300)
        e3.config(font=('Helvatical bold',25))

        lb4 = Label(newWindow,text="Age",bg='light green')
        lb4.place(x=850,y=300)
        lb4.config(font=('Helvatical bold',25))
        e4=Entry(newWindow,bg='light blue')
        e4.place(x=1050,y=300)
        e4.config(font=('Helvatical bold',25))

        myvar1=IntVar()
        myvar2=IntVar()
        lb5 = Label(newWindow,text="Select Gender",bg='light green')
        lb5.place(x=60,y=400)
        lb5.config(font=('Helvatical bold',25))
        rb1=Radiobutton(newWindow,text="Male",variable=myvar1,value=0,width=15,anchor='w',bg='blue')
        rb1.place(x=400,y=400)
        rb1.config(font=('Helvatical bold',25))
        rb2=Radiobutton(newWindow,text="Female",variable=myvar1,value=1,width=15,anchor='w',bg='pink')
        rb2.place(x=750,y=400)
        rb2.config(font=('Helvatical bold',25))
        rb3=Radiobutton(newWindow,text="Transgender",variable=myvar1,value=2,width=15,anchor='w',bg='orange')
        rb3.place(x=1100,y=400)
        rb3.config(font=('Helvatical bold',25))


        lb6 = Label(newWindow,text="Select Ward",bg='light green')
        lb6.place(x=60,y=500)
        lb6.config(font=('Helvatical bold',25))
        rb4=Radiobutton(newWindow,text="Ward A",variable=myvar2,value=0,width=10,anchor='w',bg='teal')
        rb4.place(x=400,y=500)
        rb4.config(font=('Helvatical bold',25))
        rb5=Radiobutton(newWindow,text="Ward B",variable=myvar2,value=1,width=10,anchor='w',bg='violet')
        rb5.place(x=650,y=500)
        rb5.config(font=('Helvatical bold',25))
        rb6=Radiobutton(newWindow,text="Ward C",variable=myvar2,value=2,width=10,anchor='w',bg='cyan')
        rb6.place(x=900,y=500)
        rb6.config(font=('Helvatical bold',25))
        rb7=Radiobutton(newWindow,text="Ward D",variable=myvar2,value=3,width=10,anchor='w',bg='purple')
        rb7.place(x=1150,y=500)
        rb7.config(font=('Helvatical bold',25))

        lb8 = Label(newWindow,text="Enter Room Number Alloted",bg='light green')
        lb8.place(x=60,y=600)
        lb8.config(font=('Helvatical bold',25))
        e8=Entry(newWindow,bg='light blue')
        e8.place(x=550,y=600)
        e8.config(font=('Helvatical bold',25))

        def enter(a):
             query="INSERT INTO patient(fname,lname,phone,age,gender,ward,room) VALUES(%s,%s,%s,%s,%s,%s,%s)"
             val=(a[0],a[1],a[2],a[3],a[4],a[5],a[6])
             mycursor.execute(query)
             mycursor.execute("SELECT * FROM appointment")
             myresult=mycursor.fetchall()
             for x in myresult:
                print(x)
             mydb.commit()

        def submit():
            a=e2.get()
            b=e6.get()
            c=str(e3.get())
            d=str(e4.get())
            if myvar1.get()==0:
                e="Male"
            if myvar1.get()==1:
                e="Female"
            if myvar1.get()==2:
                e="Transgender"
            if myvar2.get()==0:
                f="A"
            if myvar2.get()==1:
                f="B"
            if myvar2.get()==2:
                f="C"
            if myvar2.get()==3:
                f="D"
            g=str(e8.get())
            val=(a,b,c,d,e,f,g)
            # print(val)
            query="INSERT INTO patient(fname,lname,phone,age,gender,ward,room) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,val)
            mycursor.execute("SELECT * FROM appointment")
            myresult=mycursor.fetchall()
            for x in myresult:
               print(x)
            lb7 = Label(newWindow,text="Details are : Name = "+a+" "+b+", Number = "+" "+c+", Age = "+d+", Gender = "+e+", Ward = "+f+", Room = "+g,bg='light green')
            lb7.place(x=550,y=700)
            lb7.config(font=('Helvatical bold',15))

        btn1 = Button(newWindow,text ="Submit Details",command = submit,bg='red')
        btn1.config(font=('Helvatical bold',25))
        btn1.place(x=1000,y=600)

        btn2 = Button(newWindow, text="Go To Home Page", command=newWindow.destroy,bg='teal')
        btn2.config(font=('Helvatical bold',25))
        btn2.place(x=60,y=700)

        mainloop()
        
btn5 = Button(myw,text ="Admit New Patients",command = pat,bg='cyan')
btn5.config(font=('Helvatical bold',30))
btn5.place(x=1100,y=400)

def eve():
    win= Tk()
    win.title("Events")
    win.geometry('1100x140')
    win.configure(bg='#136f72')
    info_s = all_events(cursor)
    st = ''
    for i in info_s:
        st+=i
        st+='\n'
    lb1 = Label(win,text=st,bg='light green')
    lb1.configure(font=('Helvatical bold',15))
    print(st)
    lb1.grid(row=2,column=2)
    mainloop()

lb6 = Label(myw,text = infs,width=60,height=2,bg='#a70d2a')
lb6.config(font=('Helvatical bold',20))
lb6.place(x=60,y=700)

btn6 = Button(myw,text ="Click For More Info",command =eve,bg='teal')
btn6.config(font=('Helvatical bold',30))
btn6.place(x=1100,y=700)

def dele():
    # Delete Records
    newWindow=Toplevel(myw)
    newWindow.configure(bg='gold')
    newWindow.state('zoomed')
    from tkinter import messagebox as msg
    newWindow.title("Delete Patient")
    newWindow.configure(bg='gold')
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="system",database="mydatabase")
    mycursor = mydb.cursor()
    # mycursor.execute("Create Database mydatabase")
    # mycursor.execute("Drop Table IF exists appointment")
    # mycursor.execute("Create table appointment(id int Auto_Increment Primary Key,fname VARCHAR(50),lname VARCHAR(50),phone int,age int, gender varchar(20),doctor varchar(50))")
    a=""
    b=""
    lb1=Label(newWindow,text="Delete Patient Details",bg='red')
    lb1.place(x=350,y=20)
    lb1.config(font=('Helvatical bold',60))
    
    lb6 = Label(newWindow,text="Enter Patients Phone No.",bg='light green')
    lb6.place(x=60,y=200)
    lb6.config(font=('Helvatical bold',25))
    e6=Entry(newWindow,bg='light blue')
    e6.place(x=500,y=200)
    e6.config(font=('Helvatical bold',25))

    # def enter(t):
    #      query="INSERT into appointment(fname,lname,phone,age,gender,doctor) values(%s,%s,%s,%s,%s,%s)"
    #      val=(t[0],t[1],t[2],t[3],t[4],t[5])
    #      mycursor.execute(query,val)
    #      mycursor.execute("SELECT * FROM appointment")
    #      myresult=mycursor.fetchall()
    #      for x in myresult:
    #         print(x)
    #      mydb.commit()
    def delete():
        mycursor.execute("select * from patient")
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)

        a = e6.get()
        mycursor.execute("SELECT * FROM patient where phone="+str(a))
        mydelete = mycursor.fetchall()
        mycursor.execute("DELETE FROM patient WHERE phone=" + str(a) )
        msg.showerror("Deleted ","Patients Details With Phone Number = "+str(a))
        mycursor.execute("SELECT * FROM patient")
        myresult=mycursor.fetchall()
        for x in myresult:
            print(x)
        mydb.commit()
        lb7 = Label(newWindow,text=mydelete,bg='light green')
        lb7.place(x=60,y=500)
        lb7.config(font=('Helvatical bold',30))
    btn1 = Button(newWindow,text ="Delete Patient Details",command = delete,bg='red')
    btn1.config(font=('Helvatical bold',25))
    btn1.place(x=1000,y=200)
    btn2 = Button(newWindow, text="Go To Home Page", command=newWindow.destroy,bg='teal')
    btn2.config(font=('Helvatical bold',25))
    btn2.place(x=1000,y=600)
    mainloop()



btn7 = Button(myw, text="Delete Patient Record", command=dele,bg='orange')
btn7.config(font=('Helvatical bold',30))
btn7.place(x=1100,y=550)

# ----------------------Menu Buttons----------------------

mymenu=Menu(myw)
myw.config(menu=mymenu) # we are telling myw that mymenu is the menu please accept it
filemenu=Menu(mymenu)

def new():
    newWindow = Toplevel(myw)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    newWindow.state('zoomed')
    Label(newWindow,text ="This is a new dummy window").pack()

mymenu.add_cascade(label='Menu',menu=filemenu)
filemenu.add_command(label="New Tab",command=new)
filemenu.add_command(label="Appointment",command=Apt)
filemenu.add_command(label="Medicines",command=med)
filemenu.add_command(label="Admit",command=pat)
filemenu.add_separator()
filemenu.add_command(label="Save")
filemenu.add_command(label="SaveAs")
filemenu.add_command(label="Exit",command=myw.destroy)
editmenu=Menu(mymenu)
mymenu.add_cascade(label='Your Account',menu=editmenu)
editmenu.add_command(label="Login")
editmenu.add_command(label="Forgot Password")
editmenu.add_command(label="On Leave")
mainloop()
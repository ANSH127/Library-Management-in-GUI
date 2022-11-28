from tkinter import *
from PIL import Image,ImageTk
import random
lst1=[]
lst2=[]
id1=[]
d1=[]
d3=[]
x5=[]
q1=[]
q2=[]
q3=[]
t=0
t2=''
r=0



def Return():
    global purentry,root8
    
    if t==1:
        root8=Tk() 
        root8.geometry('600x400')
        root8.config(bg='cyan')
        Label(root8,text='RETURN',font='papyrue 20 bold',bg='black',fg='white',padx=25).place(x=190,y=50)
        Label(root8,text='Purchaser Name',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=190,y=180)
        purentry=Entry(root8,font=20)
        purentry.place(x=165,y=210)
        b_1=Button(root8,fg='white',text='Submit',bd=2,pady=5,padx=20,bg='black',font='comicsansms 7 bold',command=return1)
        b_1.place(x=163,y=270)
        b_2=Button(root8,fg='white',text='Quit',bd=2,pady=5,padx=20,bg='black',font='comicsansms 7 bold',command=quit)
        b_2.place(x=290,y=270)
        root8.mainloop()

def return1():
    global t,t2,x5,r
    x=purentry.get()
    if x==t2:
        if x in q1:
            po=q1.index(x)  
            Label(root8,text='Return Sucessful',font='papyrue 12 bold',bg='orchid1',fg='white',padx=25).place(x=190,y=300)
        
            for i in range(0,len(x5)):
                z=d1.index(x5[i])
                d1.pop(z)
            q1.pop(po)
            q2.pop(po)
            q3.pop(po)
            id1.pop(po)
            lst2.pop(po)
            t=0
            t2=''
            x5=[]
            r=0
            
            print(d1,q1,q2,q3,id1)
    
















def showbill():
    global t,r
    root7=Tk()
    root7.geometry('550x800')
    
    for i in range(0,len(x5)):
            r+=int(x5[i][4][0])
    print(r)
    
    
    Label(root7,text='-------------------------------',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=20)
    Label(root7,text='LIBRARY',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=190,y=50)
    Label(root7,text='---------------------------',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=90)
    Label(root7,text='BILL',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=130)
    Label(root7,text='-----------------------------',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=180)    
    Label(root7,text=('Name-',q1[p]),font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=220)
    Label(root7,text=('Adress',q2[p]),font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=260)
    Label(root7,text=('Phone no',q3[p]),font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=300)
    Label(root7,text='Type-Books',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=340)
    Label(root7,text='--------------------------------',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=380)
    Label(root7,text=('Total Amount',r,'$'),font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=420)
    Label(root7,text='-------------------------------',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=460)
    Label(root7,text='Thank You',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=500)
    Label(root7,text='Stay Home Stay Safe',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=540)
    Label(root7,text='--------------------------------',font='papyrue 12 bold',bg='black',fg='white',padx=25).place(x=170,y=590)
    
    t+=1
   # q1.pop(p)
    #q2.pop(p)
    #q3.pop(p)
   # id1.pop(p)
    
   # for i in range(0,len(x5)):
    #        z=d1.index(x5[i])
     #       d1.pop(z)
   # print(d1)
    
    root7.mainloop()
















def pay():
    global id_entry
    root5=Tk()
    root5.geometry('550x350')
    root5.config(bg='gold')
    Label(root5,text='Enter The Id',font='papyrue 18 bold',bg='black',fg='white',padx=25).place(x=170,y=70)
    id_entry=Entry(root5,font=20)
    id_entry.place(x=150,y=150)
    b_1=Button(root5,fg='white',text='Submit',bd=2,pady=5,padx=20,bg='black',font='comicsansms 7 bold',command=pay1)
    b_1.place(x=170,y=200)
    b_2=Button(root5,fg='white',text='Quit',bd=2,pady=5,padx=20,bg='black',font='comicsansms 7 bold',command=quit)
    b_2.place(x=290,y=200)
    
    root5.mainloop()
    



def pay1():
    global p,x5,t2
    #print(adentry.get())
    v1=id_entry.get()
    if int(v1) in id1:
        root6=Tk()
        root6.geometry('550x350')
        root6.config(bg='gold')
        p=id1.index(int(v1))
        print(p)
        Label(root6,text=('Name-',q1[p]),font='papyrue 10 bold',bg='black',fg='white').place(x=50,y=50)
        Label(root6,text=('Adress-',q2[p]),font='papyrue 10 bold',bg='black',fg='white').place(x=300,y=50)
        #Label(root6,text=('Phone no.',q3),font='papyrue 215 bold',bg='black').pack()
        Label(root6,text=('1 -Credit/Debit Card'),font='papyrue 10 bold',bg='black',fg='white').place(x=150,y=100)
        Label(root6,text=('2-Using Upi'),font='papyrue 10 bold',bg='black',fg='white').place(x=150,y=130)
        Label(root6,text=('3-Using Cash'),font='papyrue 10 bold',bg='black',fg='white').place(x=150,y=160)

        Label(root6,text=('MODE OF PAYMENT'),font='papyrue 15 bold',bg='black',fg='white').place(x=150,y=10)
       
        choientry=Entry(root6,font=20)
        choientry.place(x=120,y=210)
        b_1=Button(root6,fg='white',text='Submit',bd=2,pady=5,padx=20,bg='black',font='comicsansms 7 bold',command=showbill)
        b_1.place(x=153,y=250)
        b_2=Button(root6,fg='white',text='Quit',bd=2,pady=5,padx=20,bg='black',font='comicsansms 7 bold',command=quit)
        b_2.place(x=280,y=250)
        
        for i in range(0,len(d1)):
            for j in range(0,len(lst2[p])):
                if int(lst2[p][j])==int(d1[i][0]):
                    #print(d1[i])
                    x5+=[d1[i]]
        t2=q1[p]
       # Label(root6,text=('Name-',q1),font='papyrue 20 bold',bg='black').pack()
        #Label(root6,text=('Name-',q1),font='papyrue 20 bold',bg='black').pack()
        
        root6.mainloop()












def booked():
    global lst1,lst2,id1,d1
    x=Label(root3,text='Booked Sucessfully',bg='misty rose',font='papyrue 12 bold')
    x.place(x=280,y=470)
    y=choentry.get()
    lst1=y.split()
    lst2+=lst1,
    print(lst1)
    print(lst2)
    lst=[
         ['S.NO','Subject','Nameofthebook','Publisher','Price'],
         ['1','English','Flamingo','NCERT','2$'],
         ['2', 'English' ,'Vistas','NCERT','1$'],
         ['3 ','Maths' ,'Text book' ,'NCERT','3$'],
         ['4' ,'IP ' ,'withPython','NCERT','2$'],
         ['5 ',  'Physics' , 'Text ','NCERT','1$'],
         ['6  ','Chemistry',' Text','NCERT','4$'],
         ['7','Biology'  ,'	Text '	,'NCERT','2$'],
         ['8','Chemistry','	Lab Manual ','R.K. Publishers','1$'],
         ['9','Biology'  ,' Lab Manual','Evergreen Publications','3$'],
         ['10' ,'Physics'  ,'	Lab Manual ','Arihant Publications','2$'],
         ['11', 'Maths','Exemplar ','Activities in Mathematics'',2$'],
         ['12', 'P.Edu','Text Book' , 'S P Books','1$'],
         ['13', 'P.Edu' ,'Practical File' ,'S P Books','1$']]
    for i in lst1:
        x3=int(i)
        d1+=[lst[x3],]
    print(d1)
    
    r=random.randint(1000,10000)
    id1+=r,
    print(id1)
    x1=Label(root3,text=('Your Purchase Id is',r),bg='misty rose',font='papyrue 12 bold')
    x1.place(x=280,y=500)
    



def showdata():
    global q1,q2,q3
    q1+=nameentry.get(),
    q2+=adentry.get(),
    q3+=phentry.get(),
    global root3,choentry
    root3=Tk()
    root3.geometry('800x600')
    x=Label(root3,text='''
S.NO	Subject	   	Nameofthebook		Publisher                     Price
1	    English		Flamingo		     NCERT                         2$
2	   English    	Vistas			     NCER                          1$
3   	Maths 		Text book 		     NCERT                         3$
4  	     IP  		withPython	 	     NCERT                         2$
5      Physics  	Text 			     NCERT                         1$
6  	  Chemistry	    Text			     NCERT                         4$
7	  Biology   	Text 			     NCERT                         2$
8	  Chemistry 	Lab Manual 		    R.K. Publishers                1$
9	  Biology     	Lab Manual		   Evergreen Publications          3$
10 	  Physics   	Lab Manual 		   Arihant Publications            2$
11	   Maths	        Exemplar 		Activities in Mathematics      2$
12	   P.Edu 		    Text Book 	 	S P Books                      1$
13	   P.Edu 		Practical File 		S P Books                      1''',font='papyrue 10 bold')
    x.pack()
    
    y=Label(root3,text='Enter the choice no.',fg='white',bg='black',font='papyrue 15 bold',relief='sunken',bd=8,padx=9)
    y.place(x=250,y=300)
    choentry=Entry(root3,font=20)
    choentry.place(x=250,y=350)
    b_1=Button(root3,fg='white',text='Submit',bd=2,pady=5,padx=20,bg='black',font='comicsansms 7 bold',command=booked)
    b_1.place(x=250,y=420)
    b_2=Button(root3,fg='white',text='Quit',bd=2,pady=5,padx=20,bg='black',font='comicsansms 7 bold',command=quit)
    b_2.place(x=410,y=420)
    


def submit():
    global d3
    
    v=identry.get()
    if int(v) in id1:
        root4=Tk()
        root4.geometry('550x350')
        
        ind=id1.index(int(v))
        print(ind)
        d3=[]
        for i in range(0,len(d1)):
            for j in range(0,len(lst2[ind])):
                if int(lst2[ind][j])==int(d1[i][0]):
                    #print(d1[i])
                    d3+=[d1[i]]
        z2=Label(root4,text='The Records Are',font='papyrue 15 bold')
        z2.pack()
        z3=Label(root4,text='S.No Subject Nameofthebook	Publisher Price',font='papyrue 10 bold')
        z3.place(x=100,y=80)
        b=0
        for i in range(len(d3)):
            Label(root4,text=d3[i],bg='white',font='papyrue 13 bold',padx=20).place(x=100,y=100+b)
            b+=50
        
        
        root4.mainloop()
        
        
        
        
    
def quit():
    quit()

def display():
    global identry
    root1=Tk()
    
    root1.geometry('600x400')
    root1.config(bg='gold')
    x=Label(root1,text='Display Books',fg='white',bg='black',font='papyrue 15 bold',relief='sunken',bd=10,padx=40)
    x.place(x=240,y=50)
    y=Label(root1,text="Purchase Id:",fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=3)
    y.place(x=100,y=180)
    #idvalue=StringVar()
    identry=Entry(root1,font=20)
    identry.place(x=240,y=178)
    
    b_1=Button(root1,fg='black',text='Submit',bd=2,pady=5,padx=20,bg='white',font='comicsansms 7 bold',command=submit)
    b_1.place(x=200,y=250)
    b_2=Button(root1,fg='black',text='Quit',bd=2,pady=5,padx=20,bg='white',font='comicsansms 7 bold',command=quit)
    b_2.place(x=390,y=250)
    root1.mainloop()


def borrow():
    global nameentry,adentry,phentry
    root2=Tk()
    
    root2.geometry('600x400')
    root2.config(bg='gold')
    x=Label(root2,text='Borrow',fg='white',bg='black',font='papyrue 15 bold',relief='sunken',bd=10,padx=40)
    x.place(x=240,y=50)
    y=Label(root2,text="Name",fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=3,padx=10)
    y.place(x=100,y=180)
    z=Label(root2,text="Adress",fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=3,padx=10)
    z.place(x=100,y=215)
    z1=Label(root2,text="Phone no.",fg='white',bg='black',font='papyrue 10 bold',relief='sunken',bd=3,padx=5)
    z1.place(x=100,y=255)
    nameentry=Entry(root2,font=20)
    nameentry.place(x=200,y=178)
    adentry=Entry(root2,font=20)
    adentry.place(x=200,y=210)
    phentry=Entry(root2,font=20)
    phentry.place(x=200,y=250)
    b_1=Button(root2,fg='black',text='Submit',bd=2,pady=5,padx=20,bg='white',font='comicsansms 7 bold',command=showdata)
    b_1.place(x=150,y=320)
    b_2=Button(root2,fg='black',text='Quit',bd=2,pady=5,padx=20,bg='white',font='comicsansms 7 bold',command=quit)
    b_2.place(x=345,y=320)
    
    
    
    
    root2.mainloop()
    
idvalue=''
root=Tk()
root.title('ANSH GUI')
root.geometry('1800x1200')
x=Image.open(r"C:\Users\ansha\Downloads\Library-management-system-synopsis-e1569435337531.jpg")
y=ImageTk.PhotoImage(x)
label=Label(image=y)
label.pack()
f=Frame(root,width=100,height=150)
Label(f,text='Welcome To library',font='lucida 33 bold',fg='black',bg='cornsilk2',padx=400).pack()
Label(f,text='Made By Ansh',font='lucida 13',bg='coral',padx=550).pack()
f.place(x=30,y=30)


b1=Button(root,fg='violetred1',text='Display',bd=10,padx=50,bg='black',font='comicsansms 15 bold',command=display)
b1.place(x=570,y=260)
b2=Button(root,fg='violetred1',text='Borrow',bd=10,padx=50,bg='black',font='comicsansms 15 bold',command=borrow)
b2.place(x=570,y=325)
b3=Button(root,fg='violetred1',text='Return',bd=10,padx=50,bg='black',font='comicsansms 15 bold',command=Return)
b3.place(x=570,y=385)
b4=Button(root,fg='violetred1',text='Payment',bd=10,padx=40,bg='black',font='comicsansms 15 bold',command=pay)
b4.place(x=570,y=450)

root.mainloop()
from tkinter import*
from tkinter import messagebox as tmsg
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from PIL import Image,ImageTk
import mysql.connector

class login:
    def __init__(self) -> None:
        self.root=Tk()
        self. Name=StringVar()
        self.pas=StringVar()  
    
    def newsu(self):
        self.root.destroy()
        newsupli().main()
    
    def loginfo1(self):
        self.select=self.r1.get()
        self.nam=self.Name.get()
        self.passs=self.pas.get()
        self.select1=self.r2.get()

        if self.select=='Admin':
             conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
             cur=conn.cursor()
             cur.execute("select*from admin")
             res=cur.fetchall()
             for x in res:
                 if x[0]==self.nam and x[1]==self.passs:
                     tmsg.showinfo("success","Login Successfull")
                
                     conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
                     cur=conn.cursor()
                     cur.execute("insert into loginpage values('{}','{}')".format(self.nam,self.passs))
                     conn.commit()

                     self.root.destroy()
                     newsupli().main()
                     break
                         
             else:
                 tmsg.showerror("error","Admin not found or incorrect password")
        
        elif  self.select1=='Emp':
            
              con=mysql.connector.connect(host='localhost',user='root',password='',database='created')
              cur=con.cursor()
              cur.execute("select*from createdinfo")
              re=cur.fetchall()
              for t in re:
                  if t[0]==self.nam and t[2]==self.passs:
                     tmsg.showinfo("success","Login successfull")
                     conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
                     cur=conn.cursor()
                     cur.execute("insert into loginpage values('%s','%s')"%(self.nam,self.passs))
                     conn.commit()
                     self.root.destroy()
                     logo().main()
                     break
              else:
                  tmsg.showerror("error","Invalid username or password")
        else:
            tmsg.showinfo("select","Select admin or emp")

    def main(self):
        root=self.root
        root.geometry("600x500")
        root.maxsize(600,500)
        root.minsize(600,500)
        self.r1=StringVar()
        self.r1.set('Suppliers')
        self.r2=StringVar()
        self.r2.set('Suppliers')
       
        Label(root,text="Employee Login",font=("arial 29"),pady=50).pack()
        f=Frame(root,width=400,height=300,relief=SUNKEN,border=15,bg='orange').place(x=100,y=100)
        h=Radiobutton(f,text="Admin",font=("arial 15"),bg="orange",variable=self.r1,value='Admin')
        h.place(x=190,y=150)
        h=Radiobutton(f,text="Employee",font=("arial 15"),bg="orange",variable=self.r2,value="Emp")
        h.place(x=290,y=150)
        Label(root,text="Name",font=("arial 20"),bg='orange').place(x=150,y=190)
       
        Label(root,text="Password",font=("arial 20"),bg='orange').place(x=150,y=240)
        Button(root,text="Login",font=("arial 15"),width=10,command=self.loginfo1,bg='black',fg='white').place(x=180,y=300)
        Button(root,text="Create",width=10,font=("arial 15"),command=self.nextpage,bg='black',fg='white').place(x=320,y=300)
        Entry(root,textvariable=self.Name,width=30,relief=SUNKEN,border=5).place(x=280,y=195)
        
        Entry(root,textvariable=self.pas,width=30,relief=SUNKEN,border=5,show='*').place(x=280,y=245)
        root.mainloop() 

    def nextpage(self):
        self.root.destroy()
        create().main()

class logo:
    def __init__(self) -> None:
        self.root=Tk()
        self.refno=StringVar()
        self.comname=StringVar()
        self.type=StringVar()
        self.medname=StringVar()
        self.lotno=''
        self.issuedate=StringVar()
        self.expda=StringVar()
        self.uses=StringVar()
        self.sideffec=StringVar()
        self.prewar=StringVar()
        self.dosage=StringVar()
        self.tabletpric=StringVar()
        self.quant=StringVar()
        self.patient=StringVar()
        self.phoneno=StringVar()

    def stkk(self):
        self.root.destroy()
        fq().main()

    def rollbck(self):
        self.root.destroy()
        login().main()

    def savefile(self):
        self.j=self.h
        print(self.j)
      
        self.file=filedialog.asksaveasfilename(filetypes=[('text file','*.txt')],defaultextension='.txt')
        fobj=open(self.file,'w')            
        fobj.write(self.j)                 
        
    
    def billing(self):
        t1=Text(self.root,width=55,height=27,relief=RIDGE,border=6)
        t1.place(x=950,y=120)
        self.d=int(self.quant.get())
        self.d1=int(self.tabletpric.get())
        self.h=self.d*self.d1
        t1.insert(END,"\n"+"...................Billing Details....................")
        t1.insert(END,"\n")
        t1.insert(END,"\n"+"Name: "+self.patient.get())
        t1.insert(END,"\n")
        t1.insert(END,'\n'+"Medicine Name:"+self.medname.get())
        t1.insert(END,"\n")
        t1.insert(END,"\n"+"Quantity: "+self.quant.get())
        t1.insert(END,"\n")
        t1.insert(END,"\n"+"Dose: "+self.dosage.get())
        t1.insert(END,"\n")
        t1.insert(END,"\n"+"Price: "+self.tabletpric.get())
        t1.insert(END,"\n")
        t1.insert(END,"\n"+"Phone Number: "+self.phoneno.get())
        t1.insert(END,"\n")
        t1.insert(END,"\n"+"Reference Number: "+self.refno.get())
        t1.insert(END,"\n")
        t1.insert(END,"\n"+"Total amount:"+str(self.h))


        self.h=t1.get('1.0',END)

        Button(self.root,text="Save",command=self.savefile).place(x=1150,y=500)
    


        
       
    
    def main(self):
        root=self.root
        root.geometry("1500x600")
       
        root.title("Pharmacy Management System")
        ibtitle=Label(root,text="Pharmacy Management System",bd=15,bg='white',fg='darkgreen',font=("arial 30")).pack(side=TOP,fill=X)
        f1=Frame(root,width=1400,height=500,bd=15,relief=RIDGE).pack(padx=20,pady=10)
        f2=LabelFrame(f1,bd=15,text="Medicine form",width=890,height=450,padx=10,pady=30,fg='red').place(x=50,y=120)
        # t1=Text(f2,width=55,height=27,relief=RIDGE,border=6)
        # t1.place(x=950,y=120)
        self.ref=Label(f2,text="Reference_no").place(x=70,y=150)
        refff=Entry(f2,textvariable=self.refno,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=150)
        f3=Label(f2,text="Company Name",pady=10).place(x=70,y=170)
        self.comname=Entry(f2,textvariable=self.comname,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=180)

        f4=Label(f2,text="Medicine Name",pady=10).place(x=70,y=200)
        self.mednam=Entry(f2,textvariable=self.medname,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=210)

        f5=Label(f2,text="Lot_no",pady=10).place(x=70,y=230)
        self.lott=Entry(f2,textvariable=self.lotno,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=240)

        f6=Label(f2,text="Issue date",pady=10).place(x=70,y=260)
        self.issdat=Entry(f2,textvariable=self.issuedate,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=270)


        f7=Label(f2,text="Exp date",pady=10).place(x=70,y=290)
        self.exdat=Entry(f2,textvariable=self.expda,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=300)

        f8=Label(f2,text="Uses",pady=10).place(x=70,y=320)
        self.use=Entry(f2,textvariable=self.uses,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=330)

        f9=Label(f2,text="Side effect",pady=10).place(x=70,y=350)
        self.sidd=Entry(f2,textvariable=self.sideffec,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=360)

        f10=Label(f2,text="Prec&warning",pady=10).place(x=70,y=380)
        self.precc=Entry(f2,textvariable=self.prewar,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=390)

        f11=Label(f2,text="Dosage",pady=10).place(x=70,y=410)
        self.dosss=Entry(f2,textvariable=self.dosage,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=420)

        f12=Label(f2,text="Patient Name",pady=10).place(x=70,y=440)
        self.pat=Entry(f2,textvariable=self.patient,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=450)

        f13=Label(f2,text="Phone no",pady=10).place(x=70,y=470)
        self.ephonn=Entry(f2,textvariable=self.phoneno,font=("arial",9,"bold"),width=32,relief=SUNKEN,bd=1).place(x=180,y=480)

        f14=Label(f2,text="Tablet price",pady=10).place(x=500,y=135)
        self.tabpri=Entry(f2,textvariable=self.tabletpric,width=42,relief=SUNKEN).place(x=600,y=145)

        f15=Label(f2,text="Quantity",pady=10).place(x=500,y=165)
        self.qua=Entry(f2,textvariable=self.quant,width=42,relief=SUNKEN).place(x=600,y=175)

        self.b3=Button(f2,text="Submit",bg="red",fg='white',width=20,command=self.valll).place(x=70,y=520)
        self.yy=Button(f2,text="Stock",bg="red",fg='white',width=20,command=self.stkk).place(x=250,y=520)
        self.yyy=Button(f2,text="Back",bg="red",fg='white',width=20,command=self.rollbck).place(x=430,y=520)
        self.yyyy=Button(f2,text="Generate bill",bg="red",fg='white',width=20,command=self.billing).place(x=610,y=520)
        self.img=Image.open(r"C:\Users\user\Downloads\flask\phr.jpg")
        self.img=self.img.resize((420,280),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(self.img)
        self.b1=Button(root,image=self.photoimg,borderwidth=0,relief=RIDGE,border=5)
        self.b1.place(x=480,y=220)
       
        root.mainloop() 

    def valll(self):
            self.patientt=self.patient.get()
            self.medn=self.medname.get()
            self.pri=self.tabletpric.get()
            self.quantity=self.quant.get()
            self.dd=self.dosage.get()
            
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
            cur=conn.cursor()
            cur.execute("insert into pharmacy values('{}','{}','{}','{}','{}')".format(self.patientt,self.medn,self.pri,self.quantity,self.dd))
            cur.execute("select*from medicine")
            d=cur.fetchall()
            conn.commit()
            for g in d:
                 if g[0]==self.medn:
                     conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
                     cur=conn.cursor()
                     cur.execute("update medicine set Qty={}-{} where Brand_Name='{}'".format(g[4],self.quantity,self.medn))
                     conn.commit()
                    #  self.root.destroy()
                    #  logo().main()

                    
  
class create:
    def __init__(self) -> None:
        self.root=Tk()
        self.nam=StringVar()
        self.emai=StringVar()
        self.Pas=StringVar()
        self.phon=StringVar()
        self.gend=StringVar()
        self.Addr=StringVar()
        self.dob=StringVar()

    def checkk(self):
        self.namm=self.nam.get()
        self.email=self.emai.get()
        self.passs=self.Pas.get()
        self.phh=self.phon.get()
        self.gen=self.gend.get()
        self.add=self.Addr.get()
        self.dateof=self.dob.get()
        self.genddd=self.gen.lower()
        if self.namm.strip()=='' or self.email.strip()=='' or self.passs.strip()=='' or self.phh.strip()=='' or self.gen.strip()=='' :
           tmsg.showerror("error","cannot leave empty")
        elif "@" not in self.email:
            tmsg.showerror("error", "Invalid Email")

        elif len(self.passs) < 6:
            tmsg.showerror("error", "Password must be greater than 6")
        
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
            cur=conn.cursor()
            cur.execute("select*from createdinfo")
            res=cur.fetchall()
            for x in res:
                if x[0]==self.namm:
                     tmsg.showerror("error","Username already exist")
                     break
            else:
                conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
                cur=conn.cursor()
                cur.execute("insert into createdinfo values('%s','%s','%s','%s','%s','%s','%s')"%(self.namm,self.email,self.passs,self.phh,self.add,self.dateof,self.gen))
                conn.commit()
                tmsg.showinfo("success","Created  successfully")
                                            
    def relog(self):
        self.root.destroy()
        login().main()

    def main(self):
        root=self.root
        root.geometry("800x900")
        Label(root,text="Employee Registration form",font=("arial 29"),pady=30).pack()
        f=Frame(root,width=600,height=600,relief=SUNKEN,border=15,padx=50,bg='lightblue').pack()
        Label(root,text="Name",font=("arial 20"),bg='lightblue').place(x=150,y=150)
        Label(root,text="Email",font=("arial 20"),bg='lightblue').place(x=150,y=200)
        Label(root,text="Password",font=("arial 20"),bg='lightblue').place(x=150,y=250)
        Label(root,text="Phone_no",font=("arial 20"),bg='lightblue').place(x=150,y=300)
        Label(root,text="Gender",font=("arial 20"),bg='lightblue').place(x=150,y=350)
        Label(root,text="Birth Date",font=("arial 20"),bg='lightblue').place(x=150,y=400)
        Label(root,text="Address",font=("arial 20"),bg='lightblue').place(x=150,y=450)
        
        Entry(root,textvariable=self.nam,width=35,relief=SUNKEN,border=5).place(x=340,y=155)
        Entry(root,textvariable=self.emai,width=35,relief=SUNKEN,border=5).place(x=340,y=205)
        Entry(root,textvariable=self.Pas,width=35,relief=SUNKEN,border=5,show='*').place(x=340,y=255)
        Entry(root,textvariable=self.phon,width=35,relief=SUNKEN,border=5).place(x=340,y=305)
        Entry(root,textvariable=self.gend,width=35,relief=SUNKEN,border=5).place(x=340,y=355)
        Entry(root,textvariable=self.dob,width=35,relief=SUNKEN,border=5).place(x=340,y=405)
        Entry(root,textvariable=self.Addr,width=35,relief=SUNKEN,border=5).place(x=340,y=455)

        Button(root,text="Create",font=("arial 15"),relief=RIDGE,command=self.checkk,border=5,width=25,bg='black',fg='white').place(x=240,y=550)
        Button(root,text="Already have account",width=25,font=("arial 15"),relief=RIDGE,border=5,command=self.relog,bg='black',fg='white').place(x=240,y=600)
    
class fq:
    def __init__(self) -> None:
        self.root=Tk()

    def retu(self):
        self.root.destroy()
        logo().main()

    def main(self):
        root=self.root
        root.geometry("900x460")
        root.title("Stocks available")
        tree=ttk.Treeview(root)
        self.s=ttk.Style(root)
        self.s.theme_use("clam")
        self.s.configure(".",font=("Helvetica",11))
        self.s.configure("Treeview.Heading",foreground='red')
        tree['columns']=('Brand Name','Generic Name','Your price','Savings','Quantity','Dose')
        tree.column("Brand Name",width=150,anchor='center')
        tree.column("Generic Name",width=150,anchor='center')
        tree.column("Your price",width=150,anchor='center')
        tree.column("Savings",width=150,anchor="center")
        tree.column("Quantity",width=150,anchor="center")
        tree.column("Dose",width=150,anchor="center")
        tree['show']='headings'

        tree.heading("Brand Name",text="Brand_Name",anchor='center')
        tree.heading("Generic Name",text="Generic_Name",anchor='center')
        tree.heading("Your price",text="Price",anchor="center")
        tree.heading("Savings",text="Saving",anchor="center")
        tree.heading("Quantity",text="Quantity",anchor="center")
        tree.heading("Dose",text="Dose",anchor="center")
        tree.pack()
        Button(root,text="Back",font=("arial 10"),command=self.retu).pack()

        conn=mysql.connector.connect(host='localhost',database='created',password='',user='root')
        cur=conn.cursor()
        cur.execute("select*from medicine")
        u=cur.fetchall()
        i=0
        for x in u:
            tree.insert('',i,text="",values=(x[0],x[1],x[2],x[3],x[4],x[5]))

        root.mainloop()

class newsupli:
    def __init__(self) -> None:
        self.root=Tk()
        self.brand=StringVar()
        self.generic=StringVar()
        self.pric=StringVar()
        self.saving=StringVar()
        self.qty=StringVar()
        self.dose=StringVar()
        self.admin=StringVar()
        self.supp=StringVar()

    def sup(self):
        self.brandnam=self.brand.get()
        self.gename=self.generic.get()
        self.price=self.pric.get()
        self.sav=self.saving.get()
        self.quantity=self.qty.get()
        self.dos=self.dose.get()
        self.adm=self.admin.get()

        conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
        cur=conn.cursor()
        cur.execute("select*from medicine")
        f=cur.fetchall()
        for g in f:
            if g[0]==self.brandnam:
                conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
                cur=conn.cursor()
                cur.execute("update medicine set Qty={}+{} where Brand_Name='{}'".format(g[4],self.quantity,self.brandnam))
                conn.commit()
                self.root.destroy()
                newsupli().main()
                break
            
        else:
                conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
                cur=conn.cursor()
            
                cur.execute("insert into medicine values('%s','%s','%s','%s','%s','%s')"%(self.brandnam,self.gename,self.price,self.sav,self.quantity,self.dos))
                conn.commit()
                self.root.destroy()
                newsupli().main()
                 
    def showstk(self):
        self.root.destroy()
        stocking().main()
 
    def chang(self):
        self.root.destroy()
        chg().main()   
    
    def emplo(self):
        self.root.destroy()
        empp().main()

    def em(self):
        self.root.destroy()
        login().main()

    def hist(self):
        self.root.destroy()
        history().main()
        
    def main(self):
        root=self.root
        root.geometry("600x600")
        # conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
        # cur=conn.cursor()
        # cur.execute("select*from medicine")
        # g=cur.fetchall()
        # for t in g:
        #      if t[4]<=6:
        #          tmsg.showerror("check","Stocks is low please check")
        #          break
        Label(root,text="Admin",font=("arial 15")).pack()
        f=Frame(root,width=480,height=500,border=5,relief=SUNKEN,pady=30,bg='lightgreen')
        f.place(x=60,y=50)
        Label(root,text="Brand Name",font=("arial 15"),bg='lightgreen').place(x=100,y=100) 
        Label(root,text="Generic Name",font=("arial 15"),bg='lightgreen').place(x=100,y=150) 
        Label(root,text="Price",font=("arial 15"),bg='lightgreen').place(x=100,y=200) 
        Label(root,text="Savings",font=("arial 15"),bg='lightgreen').place(x=100,y=250) 
        Label(root,text="Quantity",font=("arial 15"),bg='lightgreen').place(x=100,y=300) 
        Label(root,text="Dose",font=("arial 15"),bg='lightgreen').place(x=100,y=350) 
   
        Button(root,text="Supply",font=("arial 10"),command=self.sup,bg='black',fg='white').place(x=340,y=430)
        Button(root,text="Show stock",font=("arial 10"),command=self.showstk,bg='black',fg='white').place(x=250,y=430)
        Button(root,text="Change password",font=("arial 10"),command=self.chang,bg='black',fg='white').place(x=400,y=430)
        Button(root,text="Show employee",font=("arial 10"),command=self.emplo,bg='black',fg='white').place(x=140,y=430)
        Button(root,text="Log out",font=("arial 15"),command=self.em,bg='red').place(x=290,y=470)

        Button(root,text="Sales History",font=("arial 10"),command=self.hist,bg='black',fg='white').place(x=140,y=460)

        Entry(root,textvariable=self.brand,width=30).place(x=300,y=105)
        Entry(root,textvariable=self.generic,width=30).place(x=300,y=155)
        Entry(root,textvariable=self.pric,width=30).place(x=300,y=205)
        Entry(root,textvariable=self.saving,width=30).place(x=300,y=255)
        Entry(root,textvariable=self.qty,width=30).place(x=300,y=305)
        Entry(root,textvariable=self.dose,width=30).place(x=300,y=355)

        # conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
        # cur=conn.cursor()
        # cur.execute("select*from medicine")
        # g=cur.fetchall()
        # for t in g:
        #     if t[4]<=6:
        #         tmsg.showerror("check","Stocks is low please check")
        #         break

        root.mainloop()

class stocking:
    def __init__(self) -> None:
        self.root=Tk()

    def ret(self):
        self.root.destroy()
        newsupli().main()    
      
    def main(self):
        root=self.root
        root.geometry("900x600")
        root.title("Stocks available")
        tree=ttk.Treeview(root)
        self.s=ttk.Style(root)
        self.s.theme_use("clam")
        self.s.configure(".",font=("Helvetica",11))
        self.s.configure("Treeview.Heading",foreground='red')
        tree['columns']=('Brand Name','Generic Name','Your price','Savings','Quantity','Dose')
        tree.column("Brand Name",width=150,anchor='center')
        tree.column("Generic Name",width=150,anchor='center')
        tree.column("Your price",width=150,anchor='center')
        tree.column("Savings",width=150,anchor="center")
        tree.column("Quantity",width=150,anchor="center")
        tree.column("Dose",width=150,anchor="center")
        tree['show']='headings'

        tree.heading("Brand Name",text="Brand_Name",anchor='center')
        tree.heading("Generic Name",text="Generic_Name",anchor='center')
        tree.heading("Your price",text="Price",anchor="center")
        tree.heading("Savings",text="Saving",anchor="center")
        tree.heading("Quantity",text="Quantity",anchor="center")
        tree.heading("Dose",text="Dose",anchor="center")
        tree.pack()
        
        Button(root,text="Back",font=("arial 10"),command=self.ret).pack()
       
        conn=mysql.connector.connect(host='localhost',database='created',password='',user='root')
        cur=conn.cursor()
        cur.execute("select*from medicine")
        u=cur.fetchall()
        i=0
        for x in u:
            tree.insert('',i,text="",values=(x[0],x[1],x[2],x[3],x[4],x[5]))
            
       
        root.mainloop()

class chg:
    def __init__(self) -> None:
        self.root=Tk()
        self.username=StringVar()
        self.p=StringVar()
        self.cp=StringVar()

    def adpas(self):
        self.use=self.username.get()
        self.pa=self.p.get()
        self.cpp=self.cp.get()
        
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
        cur=conn.cursor()
        cur.execute("select*from admin")
        resu=cur.fetchall()
        for c in resu:
            if self.use==c[0] and self.pa==self.cpp :
                conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
                cur=conn.cursor()
                cur.execute("update admin set Password='{}' where Name='{}'".format(self.pa,self.use))
                conn.commit()
                tmsg.showinfo("success","Password has been changed successfully")
                self.root.destroy()
                chg().main()

    def returnn(self):
        self.root.destroy()
        newsupli().main()
            
    def main(self):
        root=self.root
        root.geometry("600x400")
        root.title("Changing password")
        Label(root,text='Admin',font=("arial 15")).pack()
        f=Frame(root,width=400,height=300,relief=SUNKEN,border=15).pack()
        Label(f,text="Username",font=("arial 15")).place(x=130,y=70)
        Label(f,text="Password",font=("arial 15")).place(x=130,y=110)
        Label(f,text="Confirm password",font=("arial 15")).place(x=130,y=150)
        Button(f,text="Submit",font=("arial 15"),command=self.adpas).place(x=260,y=230)
        Button(f,text="Back",font=("arial 15"),command=self.returnn).place(x=350,y=230)
        Entry(f,textvariable=self.username,width=28).place(x=305,y=75)
        Entry(f,textvariable=self.p,width=28,show='*').place(x=305,y=115)
        Entry(f,textvariable=self.cp,width=28,show='*').place(x=305,y=155)

        root.mainloop()

class empp:
    def __init__(self) -> None:
        self.root=Tk()
        self.use=StringVar()
        self.tr=ttk.Treeview(self.root)
    
    def delet(self):
        self.h=self.use.get()
        print(self.h)
        
        if self.h=='':
            tmsg.showwarning("error","fill the employee name")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
            cur=conn.cursor()
            cur.execute("delete from createdinfo where Name='{}'".format(self.h))
            tmsg.showinfo("success","Employee has been deleted successfully")
            conn.commit()

    def bb(self):
        self.root.destroy()
        newsupli().main()
    
    def main(self):
        root=self.root
        root.geometry("2000x600")
        Entry(root,textvariable=self.use,width=30).place(x=630,y=250)
        self.s=ttk.Style(root)
        self.s.theme_use('clam')
        self.s.configure(".",font=("Helvetica",11))
        self.s.configure("Treeview.Heading",foreground='red')
        Button(root,text="back",width=10,command=self.bb).place(x=150,y=250)

        tree=self.tr
        tree["columns"]=('Name','Email','Password','Phone_no','Address','Birth_date','Gender')
        tree.column("Name",width=200,anchor='center')
        tree.column("Email",width=200,anchor='center')
        tree.column("Password",width=200,anchor='center')
        tree.column("Phone_no",width=200,anchor="center")
        tree.column("Address",width=200,anchor="center")
        tree.column("Birth_date",width=200,anchor="center")
        tree.column("Gender",width=200,anchor="center")
        tree['show']='headings'

        tree.heading("Name",text="Name",anchor='center')
        tree.heading("Email",text="Email",anchor='center')
        tree.heading("Password",text="Password",anchor="center")
        tree.heading("Phone_no",text="Phone_no",anchor="center")
        tree.heading("Address",text="Address",anchor="center")
        tree.heading("Birth_date",text="Birth_date",anchor="center")
        tree.heading("Gender",text="Gender",anchor="center")    
        tree.pack()
        Button(root,text="delete",command=self.delet).place(x=698,y=270)

        conn=mysql.connector.connect(host='localhost',database='created',password='',user='root')
        cur=conn.cursor()
        cur.execute("select*from createdinfo")
        u=cur.fetchall()
        i=0
        for x in u:
            tree.insert('',i,text="",values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
            
        root.mainloop()

class history:
    def __init__(self) -> None:
        self.root=Tk()
        self.tr=ttk.Treeview(self.root)
    
    def gb(self):
        self.root.destroy()
        newsupli().main()

    def main(self):
        root=self.root
        root.geometry("1000x400")
        tree=ttk.Treeview(root)
        tree["columns"]=('Patient','medicine','price','quantity','dose')
        tree['show']='headings'
        s=ttk.Style(root)
        s.theme_use('clam')
        s.configure('.',font=("arial 10"))
        s.configure('Treeview.Heading',foreground='red')
        tree.column('Patient',width=150)
        tree.column('medicine',width=150)
        tree.column('price',width=150)
        tree.column('quantity',width=150)
        tree.column('dose',width=150)

        tree.heading('Patient',text='Patient_Name',anchor='center')
        tree.heading('medicine',text='Medicine_Name',anchor='center')
        tree.heading('price',text='Price',anchor='center')
        tree.heading('quantity',text='Qty',anchor='center')
        tree.heading('dose',text='Dose',anchor='center')
        tree.pack()
        Button(root,text='back',command=self.gb).place(x=240,y=240)
        conn=mysql.connector.connect(host='localhost',user='root',password='',database='created')
        cur=conn.cursor()
        cur.execute("select*from pharmacy")
        res=cur.fetchall()
        i=0
        for c in res:
            tree.insert('',i,text='',values=(c[0],c[1],c[2],c[3],c[4]))
        
        root.mainloop()

log=login()
log.main()
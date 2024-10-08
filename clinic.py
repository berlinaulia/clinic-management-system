from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from turtle import bgcolor
from PIL import Image
from PIL import ImageTk
from tkcalendar import *
import sqlite3
import time
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import date

db=sqlite3.connect('admin.db')
dbpatient=sqlite3.connect('PatientInformation.db')

root = Tk()
root.title("Clinic Management System")
root.iconbitmap('filename.ico')
root.geometry("1290x800+0+0")
root.resizable(0,0)

class main:
    def __init__(self):
        self.x = 1290  # Start position for the text

    def login(self):
        self.var1 = self.e1.get()
        self.var2 = self.e2.get()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM UserLogin WHERE UserID='" + self.var1 + "' and Password='" + self.var2 + "'")
        db.commit()
        self.ab = cursor.fetchone()

        if self.ab is not None:
            self.under_fm = Frame(root, height=500, width=1290, bg='#fff')
            self.under_fm.place(x=0, y=0)
            
            self.fm2 = Frame(root, bg='#56799B', height=120, width=1290)
            self.fm2.place(x=0, y=0)

            self.lbb = Label(self.fm2, bg='#56799B')
            self.lbb.place(x=15, y=5)
            self.ig = PhotoImage(file=r'icon\clinic.png')
            self.lbb.config(image=self.ig)
            
            self.lb3 = Label(self.fm2, text='PATIENT INFORMATION HOME PAGE', fg='White', bg='#56799B', font=('times new roman', 35, 'bold'))
            self.lb3.place(x=self.x, y=26)  # Initial position for the text

            self.name = Label(root, text="Name : ", bg='#56799B', fg="#fff", font=('Calibri', 12, 'bold'))
            self.name.place(x=5, y=83)
            self.name1 = Label(root, text=self.ab[0], fg='#fff', bg='#56799B', font=('Calibri', 12, 'bold'))
            self.name1.place(x=60, y=83)
            
            self.animate_text()  # Start the animation after login success
            self.cur()
        else:
            messagebox.showerror('Clinic System', 'Your ID or Password is invalid!')

    def animate_text(self):
        # Update position
        self.x -= 5  # Move left by 5 pixels
        if self.x < -self.lb3.winfo_reqwidth():  # If text goes out of view
            self.x = 1290  # Reset position

        # Update text position
        self.lb3.place(x=self.x, y=26)
        
        # Schedule next update
        root.after(25, self.animate_text)  # Repeat every 50ms
            
    def cur(self):
        self.fm3=Frame(root,bg='#F0FFFF',width=1290,height=550)
        self.fm3.place(x=0,y=115)

        self.fm4=Frame(root,bg='#fff',width=1290,height=70)
        self.fm4.place(x=0,y=660)
       
        def clock():
            h = str(time.strftime("%H"))
            m = str(time.strftime("%M"))
            s = str(time.strftime("%S"))
            
            if int(h) >=12 and int(m) >=0:
                self.lb7_hr.config(text="PM")
                
            self.lb1_hr.config(text=h)
            self.lb3_hr.config(text=m)
            self.lb5_hr.config(text=s)
    
            self.lb1_hr.after(200, clock)
        
        self.lb1_hr = Label(self.fm3, text='12', font=('times new roman', 20, 'bold'), bg='#98AFC7', fg='white')
        self.lb1_hr.place(x=30, y=450, width=60, height=70)

        self.lb3_hr = Label(self.fm3, text='05', font=('times new roman', 20, 'bold'), bg='#98AFC7', fg='white')
        self.lb3_hr.place(x=100, y=450, width=60, height=70)
        
        self.lb5_hr = Label(self.fm3, text='37', font=('times new roman', 20, 'bold'), bg='#98AFC7', fg='white')
        self.lb5_hr.place(x=170, y=450, width=60, height=70)
        
        self.lb7_hr = Label(self.fm3, text='AM', font=('times new roman', 17, 'bold'), bg='#98AFC7', fg='white')
        self.lb7_hr.place(x=240, y=450, width=60, height=70)
        
        clock()
        self.canvas8 = Canvas(self.fm3, bg='black', width=498, height=398)
        self.canvas8.place(x=30, y=37)

        self.photo9=PhotoImage(file=r'icon\afterlogin.png')
        self.canvas8.create_image(0,0,image=self.photo9,anchor=NW) 

        self.today=date.today()
        self.dat=Label(self.fm4,text='Date : ',bg='#fff',fg='black',font=('Calibri',12,'bold'))
        self.dat.place(x=3,y=3)
        self.dat2 = Label(self.fm4, text=self.today, bg='#fff', fg='black', font=('Calibri', 12, 'bold'))
        self.dat2.place(x=50, y=3)
        
        self.label00=Label(self.fm4,text=' Developed By - ciwi-ciwi',bg='#fff',fg='black',font=('Candara',12,'bold'))
        self.label00.place(x=1080,y=3)
        
        self.bt1=Button(self.fm3,text='  Insert Patient',fg='#fff',bg='#98AFC7',font=('Candara',15,'bold'),width=280,height=187,bd=7,relief='flat',command=self.insert,cursor='hand2',activebackground='black',activeforeground='#581845')
        self.bt1.place(x=600,y=40)
        self.log1 = PhotoImage(file=r'icon\insert.png')
        self.bt1.config(image=self.log1, compound=LEFT)
        self.small_log1 = self.log1.subsample(1,1)
        self.bt1.config(image=self.small_log1)
        
        
        self.bt2 = Button(self.fm3, text='  Update Patient', fg='#fff', bg='#98AFC7', font=('Candara', 15, 'bold'),width=280,height=187, bd=7,relief='flat',command=self.update,cursor='hand2',activebackground='black',activeforeground='#581845')
        self.bt2.place(x=935, y=40)
        self.log2 = PhotoImage(file=r'icon\update.png')
        self.bt2.config(image=self.log2, compound=LEFT)
        self.small_log2 = self.log2.subsample(1, 1)
        self.bt2.config(image=self.small_log2)
            
                 
        self.bt3 = Button(self.fm3, text='  Delete Patient', fg='#fff', bg='#98AFC7', font=('Candara', 15, 'bold'),width=280,height=187,bd=7,relief='flat',cursor='hand2',command=self.delete,activebackground='black',activeforeground='#581845')
        self.bt3.place(x=600, y=283)
        self.log3 = PhotoImage(file=r'icon\delete.png')
        self.bt3.config(image=self.log3, compound=LEFT)
        self.small_log3 = self.log3.subsample(1, 1)
        self.bt3.config(image=self.small_log3)

                 
        self.bt4 = Button(self.fm3, text=' Display', fg='#fff', bg='#98AFC7', font=('Candara', 15, 'bold'),width=280,height=187,bd=7,relief='flat',cursor='hand2',command=self.show_display,activebackground='black',activeforeground='#581845')
        self.bt4.place(x=935, y=283)
        self.log4 = PhotoImage(file=r'icon\display.png')
        self.bt4.config(image=self.log4, compound=LEFT)
        self.small_log4 = self.log4.subsample(1, 1)
        self.bt4.config(image=self.small_log4)
 
    
        self.bt5 = Button(self.fm3, text='  Log Out', fg='#fff', bg='#98AFC7', font=('Candara', 15, 'bold'),width=189,height=50, bd=7, relief='flat',cursor='hand2',command=self.code,activebackground='black',activeforeground='#581845')
        self.bt5.place(x=323, y=450)
        self.log5 = PhotoImage(file=r'icon\logout.png')
        self.bt5.config(image=self.log5, compound=LEFT)
        self.small_log5 = self.log5.subsample(1, 1)
        self.bt5.config(image=self.small_log5)

            
    def insert(self):
        class temp(main):
            def insertpatient(self):

                self.fm = Frame(root, bg='#F0FFFF', width=1290, height=650)
                self.fm.place(x=0, y=115)
                
                self.fm1 = Frame(self.fm, bg='#F0FFFF', width=1290, height=650, bd=5, relief='flat')
                self.fm1.place(x=0, y=15)
                
                self.backbt = Button(self.fm, width=60, bg='#F0FFFF', bd=0, relief='flat', command=self.cur, activeforeground='black', activebackground='#F0FFFF')
                self.backbt.place(x=2, y=15)
                self.log = PhotoImage(file=r'icon\back.png')
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

                labels = [
                    "ID", "First Name", "Last Name", "Date of Birth", "Month of Birth",
                    "Year of Birth", "Gender", "Address", "Contact Number", "Email Address",
                    "Blood Type", "History of Patient", "Name of Doctor"
                ]

                positions = [
                    (600, 15), (600, 55), (600, 95), (600, 135), (600, 175),
                    (600, 215), (600, 255), (600, 295), (600, 335), (600, 375),
                    (600, 415), (600, 455), (600, 495)
                ]

                for label, pos in zip(labels, positions):
                    lb = Label(self.fm1, text=label, fg='black', bg='#98AFC7', font=('times new roman', 11, 'bold'), width=20)
                    lb.place(x=pos[0], y=pos[1])

                self.ee1 = Entry(self.fm1, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                self.ee1.place(x=850, y=15)
                self.ee2 = Entry(self.fm1, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                self.ee2.place(x=850, y=55)
                self.ee3 = Entry(self.fm1, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                self.ee3.place(x=850, y=95)

                # Dropdown for Date of Birth (Day)
                self.dob_day_cb = ttk.Combobox(self.fm1, width=33, font=('Calibri', 11, 'bold'))
                self.dob_day_cb['values'] = [str(i) for i in range(1, 32)]
                self.dob_day_cb.place(x=850, y=135)

                # Dropdown for Month of Birth
                self.mob_cb = ttk.Combobox(self.fm1, width=33, font=('Calibri', 11, 'bold'))
                self.mob_cb['values'] = [
                    "Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
                ]
                self.mob_cb.place(x=850, y=175)

                # Dropdown for Year of Birth
                self.yob_cb = ttk.Combobox(self.fm1, width=33, font=('Calibri', 11, 'bold'))
                self.yob_cb['values'] = [str(i) for i in range(1900, 2025)]
                self.yob_cb.place(x=850, y=215)

                # Dropdown for Gender
                self.gnr_cb = ttk.Combobox(self.fm1, width=33, font=('Calibri', 11, 'bold'))
                self.gnr_cb['values'] = ["Male", "Female"]
                self.gnr_cb.place(x=850, y=255)

                self.ee8 = Entry(self.fm1, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                self.ee8.place(x=850, y=295)
                self.ee9 = Entry(self.fm1, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                self.ee9.place(x=850, y=335)
                self.ee10 = Entry(self.fm1, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                self.ee10.place(x=850, y=375)
                self.ee11 = Entry(self.fm1, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                self.ee11.place(x=850, y=415)
                self.ee12 = Entry(self.fm1, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                self.ee12.place(x=850, y=455)
                self.ee13 = Entry(self.fm1, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                self.ee13.place(x=850, y=495)

                self.canvas9 = Canvas(self.fm1, bg='black', width=290, height=290)
                self.canvas9.place(x=200, y=15)

                self.photo10 = PhotoImage(file=r'icon\logoinsert.png')
                self.canvas9.create_image(0, 0, image=self.photo10, anchor=NW)

                self.bt = Button(self.fm1, text='INSERT', width=28, height=2, fg='white', bg='#98AFC7', font=('Canara', 12, 'bold'), bd=3, relief='flat', command=self.submit1, activebackground='black', activeforeground='#ff6690')
                self.bt.place(x=200, y=350)
                self.bt2 = Button(self.fm1, text='RESET', width=28, height=2, fg='white', bg='#98AFC7', font=('Canara', 12, 'bold'), bd=3, relief='flat', command=self.reset, activebackground='black', activeforeground='#ff6690')
                self.bt2.place(x=200, y=430)

            def submit1(self):
                try:
                    self.id = self.ee1.get()
                    self.fn = self.ee2.get()
                    self.ln = self.ee3.get()
                    self.dob = self.dob_day_cb.get()
                    self.mob = self.mob_cb.get()
                    self.yob = self.yob_cb.get()
                    self.gnr = self.gnr_cb.get()
                    self.adr = self.ee8.get()
                    self.cn = self.ee9.get()
                    self.ea = self.ee10.get()
                    self.bld = self.ee11.get()
                    self.his = self.ee12.get()
                    self.dr = self.ee13.get()

                    if all([self.id, self.fn, self.ln, self.dob, self.mob, self.yob, self.gnr, self.adr, self.cn, self.ea, self.bld, self.his, self.dr]):
                        cursor = dbpatient.cursor()
                        cursor.execute(
                            "INSERT INTO Patients(ID,'First Name','Last Name','Date of Birth','Month of Birth','Year of Birth','Gender','Address','Contact Number','Email Address','Blood Type','History of Patient','Name of Doctor') values(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (self.id, self.fn, self.ln, self.dob, self.mob, self.yob, self.gnr, self.adr, self.cn, self.ea, self.bld, self.his, self.dr)
                        )
                        dbpatient.commit()
                        messagebox.showinfo("Success", "The patient information is successfully added")
                        self.clear()
                    else:
                        messagebox.showerror("Error", "Enter Valid Details")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")

            def reset(self):
                for widget in self.fm1.winfo_children():
                    if isinstance(widget, Entry):
                        widget.delete(0, END)
                    elif isinstance(widget, ttk.Combobox):
                        widget.set('')

            def clear(self):
                self.ee1.delete(0, END)
                self.ee2.delete(0, END)
                self.ee3.delete(0, END)
                self.dob_day_cb.set('')
                self.mob_cb.set('')
                self.yob_cb.set('')
                self.gnr_cb.set('')
                self.ee8.delete(0, END)
                self.ee9.delete(0, END)
                self.ee10.delete(0, END)
                self.ee11.delete(0, END)
                self.ee12.delete(0, END)
                self.ee13.delete(0, END)

        obj = temp()
        obj.insertpatient()

    
        
    def update(self):
        class test(main):
            max=0
            n = 1
            def updatepatient(self):
                self.f = Frame(root, bg='#F0FFFF', width=1290, height=650)
                self.f.place(x=0, y=115)
                
                self.fmi=Canvas(self.f,bg='#F0FFFF',width=1290,height=650,bd=0,relief='flat')
                self.fmi.place(x=0,y=0)
                
                self.fc=Frame(self.fmi,bg='#F0FFFF',width=1290,height=650,bd=4,relief='flat')
                self.fc.place(x=70,y=20)
                
                self.ffbll=Frame(self.fc,bg='#98AFC7', bd=2,relief='flat', width=460,height=50)
                self.ffbll.place(x=5,y=0)
                
                self.lc=Label(self.ffbll,text='UPDATE PATIENT  INFORMATION', bg='#98AFC7',fg='black',font=('Arial',14,'bold'))
                self.lc.place(x=70,y=10) 
                
                self.lb = Label(self.fc, text='ID', bg='#F0FFFF', width=15, fg='black', font=('times new roman', 11, 'bold'))
                self.lb.place(x=65, y=100)
                self.em2 = Entry(self.fc, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                self.em2.place(x=175, y=98)
                self.bt = Button(self.fc, text='SEARCH', width=15, bg='#98AFC7', height=1, fg='white', font=('Canara', 12, 'bold'),bd=5,relief='flat',command=self.check, activeforeground='#00203f',activebackground='#adefd1')
                self.bt.place(x=170,y=150)
                
                self.backbt = Button(self.fmi,width=60, bg='#F0FFFF',activebackground='#F0FFFF',bd=0, relief='flat',command=self.issueback)
                self.backbt.place(x=5, y=15)
                self.log = PhotoImage(file=r'icon\back.png')
                self.backbt.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbt.config(image=self.small_log)

            def check(self):
                self.b = self.em2.get()
                cursor = dbpatient.cursor()
                cursor.execute("SELECT * FROM Patients WHERE ID=?", (self.b,))
                dbpatient.commit()
                self.var = cursor.fetchone()
                
                if self.var is not None:
                    self.fmii = Canvas(self.f, bg='#F0FFFF', width=450, height=260, bd=0, relief='flat')
                    self.fmii.place(x=70, y=240)
                    
                    labels_texts = [
                        ('First Name', self.var[1]), ('Last Name', self.var[2]), ('Date of Birth', self.var[3]),
                        ('Month of Birth', self.var[4]), ('Year of Birth', self.var[5]), ('Gender', self.var[6]),
                        ('Address', self.var[7]), ('Contact Number', self.var[8]), ('Email Address', self.var[9]),
                        ('Blood Type', self.var[10]), ('History of Patient', self.var[11]), ('Name of Doctor', self.var[12])
                    ]
                    
                    y_position = 5
                    for label_text, value in labels_texts:
                        label = Label(self.fmii, text=label_text, fg='black', bg='#F0FFFF', font=('Calibri', 12, 'bold'))
                        label.place(x=5, y=y_position)
                        label_value = Label(self.fmii, text=': ' + str(value), fg='black', bg='#F0FFFF', font=('Calibri', 12, 'bold'))
                        label_value.place(x=150, y=y_position)
                        y_position += 20

                    # Fields labels and entry fields for update
                    fields_texts = [
                        'First Name', 'Last Name', 'Date of Birth', 'Month of Birth', 'Year of Birth', 'Gender',
                        'Address', 'Contact Number', 'Email Address', 'Blood Type', 'History of Patient', 'Name of Doctor'
                    ]
                    
                    self.entries = []
                    y_position = 15
                    for i, field_text in enumerate(fields_texts):
                        label = Label(self.f, text=field_text, fg='black', bg='#98AFC7', font=('times new roman', 11, 'bold'), width=20)
                        label.place(x=600, y=y_position)
                        if field_text in ['Date of Birth', 'Month of Birth', 'Year of Birth', 'Gender']:
                            if field_text == 'Date of Birth':
                                entry = ttk.Combobox(self.f, width=33, font=('Calibri', 11, 'bold'))
                                entry['values'] = [str(i) for i in range(1, 32)]
                            elif field_text == 'Month of Birth':
                                entry = ttk.Combobox(self.f, width=33, font=('Calibri', 11, 'bold'))
                                entry['values'] = [
                                    "Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                                    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
                                ]
                            elif field_text == 'Year of Birth':
                                entry = ttk.Combobox(self.f, width=33, font=('Calibri', 11, 'bold'))
                                entry['values'] = [str(i) for i in range(1900, 2025)]
                            elif field_text == 'Gender':
                                entry = ttk.Combobox(self.f, width=33, font=('Calibri', 11, 'bold'))
                                entry['values'] = ["Male", "Female"]
                        else:
                            entry = Entry(self.f, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                        
                        entry.place(x=850, y=y_position)
                        entry.insert(0, self.var[i + 1])
                        self.entries.append(entry)
                        y_position += 40
                    
                    self.update = Button(self.f, text='UPDATE', width=20, height=1, fg='white', bg='#98AFC7', font=('Canara', 14, 'bold'), bd=3, relief='flat', command=self.update_patient_info, activebackground='black', activeforeground='#ff6690')
                    self.update.place(x=750, y=500)
            
                else:
                    messagebox.showerror('Invalid Entry', "This Patient ID doesn't exist!")
                    self.em2.delete(0, END)


            def update_patient_info(self):
                updated_values = [entry.get() for entry in self.entries]

                cursor = dbpatient.cursor()
                try:
                    # Print updated values for debugging
                    print("Updated values:", updated_values)

                    # Create the SQL query
                    sql_query = """
                        UPDATE Patients SET 
                            `First Name`=?, `Last Name`=?, `Date of Birth`=?, `Month of Birth`=?, `Year of Birth`=?, `Gender`=?, 
                            `Address`=?, `Contact Number`=?, `Email Address`=?, `Blood Type`=?, `History of Patient`=?, `Name of Doctor`=?
                        WHERE ID=?
                    """

                    # Print the SQL query for debugging
                    print("SQL query:", sql_query)
                    print("Parameters:", updated_values + [self.b])

                    # Execute the SQL query
                    cursor.execute(sql_query, updated_values + [self.b])
                    dbpatient.commit()

                    messagebox.showinfo("Success", "Patient information updated successfully!")
                except Exception as e:
                    messagebox.showerror("Error", "Enter Valid Details: " + str(e))
                    print("Error details:", str(e)) 

            def issueback(self):
                try:
                    self.boot.destroy()
                    self.cur()
                except Exception as e:
                    self.cur()

        obissue=test()
        obissue.updatepatient()
    

    def delete(self):
        class dele(main):
            max = 0
            n = 1

            def deletepatient(self):
                self.ff = Frame(root, bg='#F0FFFF', width=1290, height=650)
                self.ff.place(x=0, y=115)

                self.f1 = Frame(self.ff, bg='#F0FFFF', width=1290, height=650, bd=5, relief='flat')
                self.f1.place(x=0, y=15)

                self.fc1 = Frame(self.f1, bg='#F0FFFF', width=1290, height=650, bd=4, relief='flat')
                self.fc1.place(x=70, y=20)

                self.ffbl2 = Frame(self.fc1, bg='#98AFC7', bd=2, relief='flat', width=460, height=50)
                self.ffbl2.place(x=5, y=0)

                self.lc1 = Label(self.ffbl2, text='DELETE PATIENT INFORMATION', bg='#98AFC7', fg='black', font=('Arial', 14, 'bold'))
                self.lc1.place(x=70, y=10)

                self.lb2 = Label(self.fc1, text='ID', bg='#F0FFFF', width=15, fg='black', font=('times new roman', 11, 'bold'))
                self.lb2.place(x=65, y=100)
                self.em3 = Entry(self.fc1, width=30, bd=5, relief='ridge', font=('Arial', 8, 'bold'))
                self.em3.place(x=175, y=98)
                self.bt = Button(self.fc1, text='SEARCH', width=15, bg='#98AFC7', height=1, fg='white', font=('Canara', 12, 'bold'), bd=5, relief='flat', command=self.check, activeforeground='#00203f', activebackground='#adefd1')
                self.bt.place(x=170, y=150)

                self.backbtn = Button(self.f1, width=60, bg='#F0FFFF', activebackground='#F0FFFF', bd=0, relief='flat', command=self.issueback)
                self.backbtn.place(x=5, y=15)
                self.log = PhotoImage(file=r'icon\back.png')
                self.backbtn.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbtn.config(image=self.small_log)

            def check(self):
                self.b = self.em3.get()
                cursor = dbpatient.cursor()
                cursor.execute("SELECT * FROM Patients WHERE ID=?", (self.b,))
                dbpatient.commit()
                self.var = cursor.fetchone()

                if self.var is not None:
                    self.fmii = Canvas(self.ff, bg='#F0FFFF', width=450, height=260, bd=0, relief='flat')
                    self.fmii.place(x=70, y=240)

                    labels_texts = [
                        ('First Name', self.var[1]), ('Last Name', self.var[2]), ('Date of Birth', self.var[3]),
                        ('Month of Birth', self.var[4]), ('Year of Birth', self.var[5]), ('Gender', self.var[6]),
                        ('Address', self.var[7]), ('Contact Number', self.var[8]), ('Email Address', self.var[9]),
                        ('Blood Type', self.var[10]), ('History of Patient', self.var[11]), ('Name of Doctor', self.var[12])
                    ]

                    y_position = 5
                    for label_text, value in labels_texts:
                        label = Label(self.fmii, text=label_text, fg='black', bg='#F0FFFF', font=('Calibri', 12, 'bold'))
                        label.place(x=5, y=y_position)
                        label_value = Label(self.fmii, text=': ' + str(value), fg='black', bg='#F0FFFF', font=('Calibri', 12, 'bold'))
                        label_value.place(x=150, y=y_position)
                        y_position += 20

                    # Fields labels and entry fields for deletion
                    fields_texts = [
                        'First Name', 'Last Name', 'Date of Birth', 'Month of Birth', 'Year of Birth', 'Gender',
                        'Address', 'Contact Number', 'Email Address', 'Blood Type', 'History of Patient', 'Name of Doctor'
                    ]
                    
                    self.entries = []
                    y_position = 15
                    for i, field_text in enumerate(fields_texts):
                        label = Label(self.ff, text=field_text, fg='black', bg='#98AFC7', font=('times new roman', 11, 'bold'), width=20)
                        label.place(x=600, y=y_position)
                        if field_text in ['Date of Birth', 'Month of Birth', 'Year of Birth', 'Gender']:
                            if field_text == 'Date of Birth':
                                entry = ttk.Combobox(self.ff, width=33, font=('Calibri', 11, 'bold'))
                                entry['values'] = [str(i) for i in range(1, 32)]
                            elif field_text == 'Month of Birth':
                                entry = ttk.Combobox(self.ff, width=33, font=('Calibri', 11, 'bold'))
                                entry['values'] = [
                                    "Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                                    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
                                ]
                            elif field_text == 'Year of Birth':
                                entry = ttk.Combobox(self.ff, width=33, font=('Calibri', 11, 'bold'))
                                entry['values'] = [str(i) for i in range(1900, 2025)]
                            elif field_text == 'Gender':
                                entry = ttk.Combobox(self.ff, width=33, font=('Calibri', 11, 'bold'))
                                entry['values'] = ["Male", "Female"]
                        else:
                            entry = Entry(self.ff, width=35, bd=4, relief='groove', font=('Calibri', 11, 'bold'))
                        
                        entry.place(x=850, y=y_position)
                        entry.insert(0, self.var[i + 1])
                        self.entries.append(entry)
                        y_position += 40

                    self.delete = Button(self.ff, text='DELETE', width=20, height=1, fg='white', bg='#98AFC7', font=('Canara', 14, 'bold'), bd=3, relief='flat', command=self.deldata, activebackground='black', activeforeground='#ff6690')
                    self.delete.place(x=750, y=500)

                else:
                    messagebox.showerror('Invalid Entry', "This Patient ID doesn't exist!")
                    self.em3.delete(0, END)

            def deldata(self):
                cursor = dbpatient.cursor()
                try:
                    cursor.execute("DELETE FROM Patients WHERE ID=?", (self.b,))
                    dbpatient.commit()
                    self.em3.delete(0, END)
                    self.fmii.destroy()
                    messagebox.showinfo("Success", "Patient information deleted successfully!")
                except Exception as e:
                    messagebox.showerror("Error", "Error deleting patient information: " + str(e))

            def issueback(self):
                try:
                    self.ff.destroy()
                    self.cur()
                except Exception as e:
                    self.cur()

        obissue = dele()
        obissue.deletepatient()

    
    def show_display(self):
        class Display(main):
            def __init__(self):
                self.display_data()

            def display_data(self):
                self.ff = Frame(root, bg='#F0FFFF', width=1290, height=650)
                self.ff.place(x=0, y=115)

                self.f1 = Frame(self.ff, bg='#F0FFFF', width=1290, height=650, bd=5, relief='flat')
                self.f1.place(x=0, y=0)

                self.table_frame = Frame(self.f1, bg='#F0FFFF', bd=4, relief='flat')
                self.table_frame.place(x=10, y=25, width=1270, height=500)

                # Menambahkan Scrollbars
                self.tree_scroll_y = Scrollbar(self.table_frame, orient='vertical')
                self.tree_scroll_y.pack(side=RIGHT, fill=Y)
                
                self.tree_scroll_x = Scrollbar(self.table_frame, orient='horizontal')
                self.tree_scroll_x.pack(side=BOTTOM, fill=X)

                self.tree = ttk.Treeview(self.table_frame, columns=(
                    "ID", "First Name", "Last Name", "Date of Birth", "Month of Birth", "Year of Birth", "Gender", 
                    "Address", "Contact Number", "Email Address", "Blood Type", "History of Patient", "Name of Doctor"
                ), show='headings', yscrollcommand=self.tree_scroll_y.set, xscrollcommand=self.tree_scroll_x.set)
                
                self.tree_scroll_y.config(command=self.tree.yview)
                self.tree_scroll_x.config(command=self.tree.xview)

                self.tree.heading("ID", text="ID")
                self.tree.heading("First Name", text="First Name")
                self.tree.heading("Last Name", text="Last Name")
                self.tree.heading("Date of Birth", text="Date of Birth")
                self.tree.heading("Month of Birth", text="Month of Birth")
                self.tree.heading("Year of Birth", text="Year of Birth")
                self.tree.heading("Gender", text="Gender")
                self.tree.heading("Address", text="Address")
                self.tree.heading("Contact Number", text="Contact Number")
                self.tree.heading("Email Address", text="Email Address")
                self.tree.heading("Blood Type", text="Blood Type")
                self.tree.heading("History of Patient", text="History of Patient")
                self.tree.heading("Name of Doctor", text="Name of Doctor")
                self.tree.pack(fill='both', expand=True)

                self.load_data()

                self.sort_frame = Frame(self.f1, bg='#F0FFFF', bd=4, relief='flat')
                self.sort_frame.place(x=10, y=520, width=1270, height=50)

                self.sort_label = Label(self.sort_frame, text="Sort by:", bg='#F0FFFF', font=('Arial', 12))
                self.sort_label.pack(side='left', padx=10)

                self.sort_options = ttk.Combobox(self.sort_frame, values=[
                    "ID", "First Name", "Last Name", "Date of Birth", "Month of Birth", "Year of Birth", "Gender", 
                    "Address", "Contact Number", "Email Address", "Blood Type", "History of Patient", "Name of Doctor"
                ], state="readonly")
                self.sort_options.pack(side='left', padx=10)
                self.sort_options.current(0)

                self.sort_order_label = Label(self.sort_frame, text="Order:", bg='#F0FFFF', font=('Arial', 12))
                self.sort_order_label.pack(side='left', padx=10)

                self.sort_order = ttk.Combobox(self.sort_frame, values=["Ascending", "Descending"], state="readonly")
                self.sort_order.pack(side='left', padx=10)
                self.sort_order.current(0)

                self.sort_button = Button(self.sort_frame, text="Sort", command=self.sort_data)
                self.sort_button.pack(side='left', padx=10)

                self.backbtn = Button(self.f1, width=60, bg='#F0FFFF', activebackground='#F0FFFF', bd=0, relief='flat', command=self.issueback)
                self.backbtn.place(x=5, y=0)
                self.log = PhotoImage(file=r'icon\back.png')
                self.backbtn.config(image=self.log, compound=LEFT)
                self.small_log = self.log.subsample(2, 2)
                self.backbtn.config(image=self.small_log)

                # Menambahkan elemen pencarian
                self.search_button = Button(self.sort_frame, text="Search", command=self.search_data)
                self.search_button.pack(side='right', padx=10)

                self.search_entry = Entry(self.sort_frame, font=('Arial', 11))
                self.search_entry.pack(side='right', padx=10)

                self.search_label = Label(self.sort_frame, text="Search:", bg='#F0FFFF', font=('Arial', 11))
                self.search_label.pack(side='right', padx=10)


            def load_data(self):
                cursor = dbpatient.cursor()
                cursor.execute("SELECT * FROM Patients")
                rows = cursor.fetchall()
                for row in rows:
                    self.tree.insert('', 'end', values=row)

            def sort_data(self):
                sort_by = self.sort_options.get()
                order = self.sort_order.get()
                order_sql = "ASC" if order == "Ascending" else "DESC"
                cursor = dbpatient.cursor()
                cursor.execute(f"SELECT * FROM Patients ORDER BY `{sort_by}` {order_sql}")
                rows = cursor.fetchall()

                # Menghapus data saat ini
                for item in self.tree.get_children():
                    self.tree.delete(item)

                # Memasukkan data yang sudah diurutkan
                for row in rows:
                    self.tree.insert('', 'end', values=row)
            
            def search_data(self):
                search_term = self.search_entry.get()
                cursor = dbpatient.cursor()
                query = f"""
                SELECT * FROM Patients 
                WHERE `ID` LIKE '%{search_term}%' OR 
                    `First Name` LIKE '%{search_term}%' OR 
                    `Last Name` LIKE '%{search_term}%' OR 
                    `Date of Birth` LIKE '%{search_term}%' OR 
                    `Month of Birth` LIKE '%{search_term}%' OR 
                    `Year of Birth` LIKE '%{search_term}%' OR 
                    `Gender` LIKE '%{search_term}%' OR 
                    `Address` LIKE '%{search_term}%' OR 
                    `Contact Number` LIKE '%{search_term}%' OR 
                    `Email Address` LIKE '%{search_term}%' OR 
                    `Blood Type` LIKE '%{search_term}%' OR 
                    `History of Patient` LIKE '%{search_term}%' OR 
                    `Name of Doctor` LIKE '%{search_term}%'
                """
                cursor.execute(query)
                rows = cursor.fetchall()

                # Menghapus data saat ini
                for item in self.tree.get_children():
                    self.tree.delete(item)

                # Memasukkan data hasil pencarian
                for row in rows:
                    self.tree.insert('', 'end', values=row)

            def issueback(self):
                try:
                    self.ff.destroy()
                    self.cur()
                except Exception as e:
                    self.cur()

        display = Display()
    
     

    def mainclear(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        
        
    def code(self):

            self.fm=Frame(root,height=800,width=1290,bg='white')
            self.fm.place(x=0,y=0)

            self.canvas=Canvas(self.fm,height=800,width=1290,bg='#000000')
            self.canvas.place(x=0,y=0)

            self.im=PhotoImage('filename.ico')
            self.canvas.create_image(0,0,image=self.im,anchor=NW)

            self.bg_image = PhotoImage(file=r"icon\background.png")
            self.canvas = Canvas(self.fm, height=800, width=1290, bg='#000000')
            self.canvas.create_image(0, 0, image=self.bg_image, anchor=NW)
            self.canvas.place(x=0, y=0)

            self.fm1=Frame(self.canvas,height=400,width=600,bg='#000000',bd=3,relief='sunken')
            self.fm1.place(x=350,y=120)
            
            self.b1=Label(self.fm1,text='User ID',bg='black',font=('Arial',15,'bold'),fg='white')
            self.b1.place(x=115,y=70)

            self.e1=Entry(self.fm1,width=22,font=('arial',14,'bold'),bd=4,relief='groove')
            self.e1.place(x=225,y=70)

            self.lb2=Label(self.fm1,text='Password',bg='black',font=('Arial',15,'bold'),fg='white')
            self.lb2.place(x=115,y=150)

            self.e2=Entry(self.fm1,width=22,show='*',font=('arial',14,'bold'),bd=4,relief='groove')
            self.e2.place(x=225,y=150)
            
            self.btn1=Button(self.fm1,text='Login',fg='black',bg='yellow',width=155,font=('Arial',16,'bold'),activebackground='black',activeforeground='yellow',command=self.login,bd=3,relief='flat',cursor='hand2')
            self.btn1.place(x=115,y=230)
            self.logo = PhotoImage(file=r'icon\login.png')
            self.btn1.config(image=self.logo, compound=LEFT)
            self.small_logo = self.logo.subsample(1, 1)
            self.btn1.config(image=self.small_logo)


            self.btn2=Button(self.fm1,text='  Clear',fg='black',bg='yellow',width=155,font=('Arial',16,'bold'),activebackground='black',activeforeground='yellow',bd=3,relief='flat',cursor='hand2',command=self.mainclear)
            self.btn2.place(x=314,y=230)
            self.log = PhotoImage(file=r'icon\clear.png')
            self.btn2.config(image=self.log, compound=LEFT)
            self.small_log = self.log.subsample(1, 1)
            self.btn2.config(image=self.small_log)
            
            self.forgot=Label(self.fm1,text='Forgot Password?',fg='White',bg='#000000',activeforeground='black',font=('cursive',12,'bold'))
            self.forgot.place(x=230,y=310)
            self.forgot.bind("<Button>",self.mouseClick)

            root.mainloop()
            
    def mouseClick(self,event):
        self.rog=Tk()
        self.rog.title("Change password")
        self.rog.geometry("400x300+300+210")
        self.rog.iconbitmap("filename.ico")
        self.rog.resizable(0,0)
        self.rog.configure(bg='#000')

        self.framerog=Frame(self.rog,width=160,height=30,bg="#d6ed17")
        self.framerog.place(x=95,y=15)

        self.label=Label(self.framerog,text="SET NEW PASSWORD",bg='#d6ed17',fg='#606060',font=("Calibri",12,'bold'))
        self.label.place(x=5,y=4)

        self.user=Label(self.rog,text='User ID',bg='#000',fg='white',font=("Times New Roman",11,'bold'))
        self.user.place(x=40,y=95)

        self.user = Label(self.rog, text='New Password',bg='#000', fg='white', font=("Times New Roman", 11, 'bold'))
        self.user.place(x=40, y=170)

        self.ef1 = Entry(self.rog, width=24, font=('Calibri', 8, 'bold'), bd=4, relief='groove')
        self.ef1.place(x=170, y=95)

        self.ef2 = Entry(self.rog, width=24, font=('Calibri', 8, 'bold'), bd=4, relief='groove')
        self.ef2.place(x=170, y=170)

        self.btn1 = Button(self.rog, text='SUBMIT', fg='#606060', bg='#d6ed17', width=8, font=('Calibri', 12, 'bold'),activebackground='black', activeforeground='#d6ed17',bd=3, relief='flat',cursor='hand2',command=self.chan_pas)
        self.btn1.place(x=40, y=240)
        
    def chan_pas(self):
        self.a=self.ef1.get()
        self.b=self.ef2.get()
        import sqlite3
        conn=sqlite3.connect('admin.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM UserLogin WHERE UserID='"+self.a+"'")
        conn.commit()
        self.data=cursor.fetchone()

        if self.data!=None:
                cursor = conn.cursor()
                cursor.execute("UPDATE UserLogin SET Password='" + self.b + "' WHERE UserID='" + self.a + "'")
                conn.commit()
                messagebox.showinfo("SUCCESSFUL","Your Password is changed")
                self.rog.destroy()
        else:
                messagebox.showerror("ERROR", "UserID doesn't exist")
                self.rog.destroy()
                
        self.rog.mainloop()
                                                                                

obj=main()
obj.code()
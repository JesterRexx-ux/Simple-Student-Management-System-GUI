from tkinter import*
import tkinter.messagebox
import studentdata

root=Tk()
root.title("Student Management System")
root.geometry("1350x750")
root.config(bg="cadet blue")
#==============================================Varibles==================
std_id=StringVar()
first_name=StringVar()
sur_name=StringVar()
dob=StringVar()
age=StringVar()
gender=StringVar()
address=StringVar()
mobile=StringVar()
#==============================================Function=========================================
def iexit():
    iexit=tkinter.messagebox.askyesno("Student Data Management","config if you want to exit")
    if iexit()>0:
       root.destroy()
       return
def cleardata():
    text_std_id.delete(0,END)
    text_first_name.delete(0,END)
    text_sur_name.delete(0,END)
    text_dob.delete(0,END)
    text_age.delete(0,END)
    text_gender.delete(0,END)
    text_address.delete(0,END)
    text_mobile.delete(0,END)

   

def adddata():
    if(len(std_id.get())!=0):
        studentdata.addnew(std_id.get(),first_name.get(),sur_name.get(),dob.get(),age.get(),gender.get(),address.get(),mobile.get())
        std_list.delete(0,END)
        std_list.insert(std_id.get(),first_name.get(),sur_name.get(),dob.get(),age.get(),gender.get(),address.get(),mobile.get())

def displaydata():
    std_list.delete(0,END)
    for row in studentdata.view():
        std_list.insert(END,row,str(" "))

def studentrec(event):
    global sd
    searchstd=std_list.delete(0,END)
    sd=std_list.get(searchstd)
    
    text_std_id.delete(0,END)
    text_std_id.insert(END,sd[1])
    text_first_name.delete(0,END)
    text_first_name.insert(END,sd[2])
    text_sur_name.delete(0,END)
    text_sur_name.insert(END,sd[3])
    text_dob.delete(0,END)
    text_dob.insert(END,sd[4])
    text_age.delete(0,END)
    text_age.insert(END,sd[5])
    text_gender.delete(0,END)
    text_gender.insert(END,sd[6])
    text_address.delete(0,END)
    text_address.insert(END,sd[7])
    text_mobile.delete(0,END)
    text_mobile.insert(END,sd[8])
def deletedata():
    if(len(std_id.get())!=0):
        studentdata.delete(std_id.get())

def searchdata():
    std_list.delete(0,END)
    for row in studentdata.search(std_id.get(),first_name.get(),sur_name.get(),dob.get(),age.get(),gender.get(),address.get(),mobile.get()):
        std_list.insert(END,row,str(""))
    
def updatedata():
    if(len(std_id.get())!=0):
        studentdata.delete(std_id.get())
    if(len(std_id.get())!=0):
        studentdata.addnew(std_id.get(),first_name.get(),sur_name.get(),dob.get(),age.get(),gender.get(),address.get(),mobile.get())
        std_list.delete(0,END)        
        std_list.insert(END,(std_id.get(),first_name.get(),sur_name.get(),dob.get(),age.get(),gender.get(),address.get(),mobile.get()))

#---------------------------------------------------------------------------------------------------------
#==============================================Frames============================================
mainframe=Frame(root,bg="cadet blue")
mainframe.grid()
titleframe=Frame(mainframe,bd=2,padx=54,pady=8,bg="Yellow",relief=RIDGE)
titleframe.pack(side=TOP)
labletitle=Label(titleframe,font=('arial',47,'bold'),text="Student  Managemant System",bg="Ghost White")
labletitle.pack(side=BOTTOM)

buttonframe=Frame(mainframe,bd=2,width="1350",height="70",padx="18",pady="10",bg="Ghost White",relief=RIDGE)
buttonframe.pack(side=BOTTOM)

dataframe=Frame(mainframe,bd="1",width="1300",height="400",padx="18",pady="20",relief=RIDGE,bg="cadet blue")
dataframe.pack(side=BOTTOM)

dataframeleft=LabelFrame(dataframe,bd=1,width="1000",height="600" ,padx="20",relief=RIDGE,bg="Ghost White",font=('arial',20,'bold'),text="Students INFO")
dataframeleft.pack(side=LEFT)

dataframeright=LabelFrame(dataframe,bd=1,width="450",height="300",padx="31",pady="3",relief=RIDGE,bg="Ghost White",font=('arial',20,'bold'),text="Students Details")
dataframeright.pack(side=RIGHT)
#========================================================label and Entry Area=====================================================
label_std_id=Label(dataframeleft,font=('arial',20,'bold'),text="Student ID",padx="2",pady="2",bg="Ghost White")
label_std_id.grid(row=0,column=0,sticky=W)
text_std_id=Entry(dataframeleft,font=('arial',20,'bold'),textvariable=std_id,width=39)
text_std_id.grid(row=0,column=1)

label_first_name=Label(dataframeleft,font=('arial',20,'bold'),text="First Name",padx="2",pady="2",bg="Ghost White")
label_first_name.grid(row=1,column=0,sticky=W)
text_first_name=Entry(dataframeleft,font=('arial',20,'bold'),textvariable=first_name,width=39)
text_first_name.grid(row=1,column=1)

label_sur_name=Label(dataframeleft,font=('arial',20,'bold'),text="Sur Name",padx="2",pady="2",bg="Ghost White")
label_sur_name.grid(row=2,column=0,sticky=W)
text_sur_name=Entry(dataframeleft,font=('arial',20,'bold'),textvariable=sur_name,width=39)
text_sur_name.grid(row=2,column=1)

label_dob=Label(dataframeleft,font=('arial',20,'bold'),text="D O B",padx="2",pady="2",bg="Ghost White")
label_dob.grid(row=3,column=0,sticky=W)
text_dob=Entry(dataframeleft,font=('arial',20,'bold'),textvariable=dob ,width=39)
text_dob.grid(row=3,column=1)

label_age=Label(dataframeleft,font=('arial',20,'bold'),text="Age" ,padx="2",pady="2",bg="Ghost White")
label_age.grid(row=4,column=0,sticky=W)
text_age=Entry(dataframeleft,font=('arial',20,'bold'),textvariable=age ,width=39)
text_age.grid(row=4,column=1)

label_gender=Label(dataframeleft,font=('arial',20,'bold'),text="Gender" ,padx="2",pady="2",bg="Ghost White")
label_gender.grid(row=5,column=0,sticky=W)
text_gender=Entry(dataframeleft,font=('arial',20,'bold'),textvariable=gender ,width=39)
text_gender.grid(row=5,column=1)

label_address=Label(dataframeleft,font=('arial',20,'bold'),text="Address" ,padx="2",pady="2",bg="Ghost White")
label_address.grid(row=6,column=0,sticky=W)
text_address=Entry(dataframeleft,font=('arial',20,'bold'),textvariable=address ,width=39)
text_address.grid(row=6,column=1)

label_mobile=Label(dataframeleft,font=('arial',20,'bold'),text="Mobile" ,padx="2",pady="2",bg="Ghost White")
label_mobile.grid(row=7,column=0,sticky=W)
text_mobile=Entry(dataframeleft,font=('arial',20,'bold'),textvariable=mobile ,width=39)
text_mobile.grid(row=7,column=1)

#==========================================================Listbox and Scroll bar=======================================================
scrollbar=Scrollbar(dataframeright)
scrollbar.grid(row=0,column=0,sticky='ns')

std_list=Listbox(dataframeright,width=41,height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
std_list.bind('<<ListBoxSelect>>',studentrec)
std_list.grid(row=0,column=0,padx=8)
scrollbar.config(command = std_list.yview)
#=========================================================Button Widge===============================================================================
btn_add_new=Button(buttonframe,text="Add new",font=('arial',20,'bold'),height=1,width=10,bd=4,command=adddata)
btn_add_new.grid(row=0,column=0)
btn_add_display=Button(buttonframe,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4,command=displaydata)
btn_add_display.grid(row=0,column=1)
btn_add_clear=Button(buttonframe,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4,command=cleardata)
btn_add_clear.grid(row=0,column=2)
btn_add_delete=Button(buttonframe,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4,command=deletedata)
btn_add_delete.grid(row=0,column=3)
btn_add_search=Button(buttonframe,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4,command=searchdata)
btn_add_search.grid(row=0,column=4)
btn_add_update=Button(buttonframe,text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4,command=updatedata)
btn_add_update.grid(row=0,column=5)
btn_add_exit=Button(buttonframe,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4,command=iexit)
btn_add_exit.grid(row=0,column=6)

root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root=Tk()
root.geometry("500x600")
root.title("To-Do List")
root.maxsize(500,600)
root.minsize(500,600)
root.configure(bg="#C4A484")
root.wm_iconbitmap("CodSoft_Task1\\todo.ico")

img=ImageTk.PhotoImage((Image.open("CodSoft_Task1\\todo.jpg").resize((500,600))))
label=Label(root,image=img)
label.pack(fill=BOTH)

title=Label(label, text="To-Do List", font=("Lucida",26),justify="center",foreground="brown",bg="#C4A484")
title.pack(fill=X)

task=StringVar()
task.set("")
msgbox=Entry(label,textvar=task,font="lucida 16 bold")
msgbox.focus()
msgbox.pack(pady=30)


frm=Frame(label)
lbx=Listbox(frm, font=("Lucida 20"),bg="#C4A484",foreground="white",relief=SUNKEN,border=10,height=300,selectbackground="#653A1C")

#Setting time
frm1=Frame(label)
time=Label(frm1,text="Time: ",font=("Lucida",10,"bold"),foreground="brown")
h=StringVar()
h.set("0")
m=StringVar()
m.set("0")
hour = Spinbox(frm1, from_=0, to=23, width=2,textvariable=h)
minute = Spinbox(frm1, from_=0, to=59, width=2,textvariable=m)
time.pack(side=TOP)
hour.pack(side=LEFT)
minute.pack(side=LEFT)
frm1.pack(side=TOP)


def add():
    global task
    if(task.get().isspace()==False and task.get()!=""):
        if(hour.get()!="0" and minute.get()!="0"):
            lbx.insert(END,f"{task.get()}   {hour.get()}:{minute.get()}")
            h.set("0")
            m.set("0")
            hour.update()
            minute.update()
            lbx.pack()
            task.set("")
            msgbox.update()
        else:
            lbx.insert(END,f"{task.get()}")
            lbx.pack()
            task.set("")
            msgbox.update()
def delete():
    lbx.delete(ANCHOR)

addTask=Button(label,text="Add Task", font=("Lucida 10 bold"),background="brown",foreground="white",command=add)
addTask.pack(padx=10,pady=10,ipadx=5,ipady=5)

lbx.pack()

scrollbar=Scrollbar(frm)
scrollbar.pack(side=RIGHT,fill=BOTH)
lbx.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lbx.yview)

delete_icon=ImageTk.PhotoImage((Image.open("CodSoft_Task1\dlt.png").resize((20,20))))
Button(label,image=delete_icon,bd=0,command=delete).pack(side=BOTTOM,pady=13)

frm.pack()

root.mainloop()
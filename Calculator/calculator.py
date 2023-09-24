from tkinter import *
i=9

root=Tk()

root.geometry("400x600")
root.maxsize(400,600)
root.minsize(400,600)
root.title("Calculator")
root.configure(background="black")
root.wm_iconbitmap("CodSoft_Task2\Calculator.ico")

scvalue=StringVar()
scvalue.set("")
numbox=Entry(root,textvar=scvalue,font="lucida 40 bold")
numbox.pack(fill=X, ipadx=8, pady=20,padx=20)

def click(event):
    global scvalue
    text=event.widget.cget("text")

    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(numbox.get())
        scvalue.set(value)
        numbox.update()
    elif text=="C":
        scvalue.set("")
        numbox.update()    
    else:
        scvalue.set(scvalue.get()+text)
        numbox.update()

def button(frm):
    global i
    b =  Button(frm, text=(f"{i}"), padx=15, pady=15, font="lucida 25 bold", background="orange")
    b.pack(side=LEFT, padx=12, pady=12)
    b.bind("<Button-1>",click)
    i-=1

    if i==6:
        b =  Button(frm, text="*", padx=15, pady=15, font="lucida 25 bold", background="orange")
        b.pack(side=LEFT, padx=12, pady=12)
        b.bind("<Button-1>",click)
    elif i==3:
        b =  Button(frm, text="-", padx=15, pady=15, font="lucida 25 bold", background="orange")
        b.pack(side=LEFT, padx=12, pady=12)
        b.bind("<Button-1>",click)
    elif i==0:
        b =  Button(frm, text="+", padx=15, pady=15, font="lucida 25 bold", background="orange")
        b.pack(side=LEFT, padx=12, pady=12)
        b.bind("<Button-1>",click)
    elif i<0:
        b =  Button(frm, text="C", padx=15, pady=15, font="lucida 25 bold", background="orange")
        b.pack(side=LEFT, padx=12, pady=12)
        b.bind("<Button-1>",click)
        b =  Button(frm, text="/", padx=15, pady=15, font="lucida 25 bold", background="orange")
        b.pack(side=LEFT, padx=12, pady=12)
        b.bind("<Button-1>",click)
        b =  Button(frm, text="=", padx=15, pady=15, font="lucida 25 bold", background="orange")
        b.pack(side=LEFT, padx=12, pady=12)
        b.bind("<Button-1>",click)

def mkframe():
    for j in range(0,4):
        frm=Frame(root,bg="black")
        button(frm)
        if j!=3:
            button(frm)
            button(frm)
        frm.pack()

mkframe()
root.mainloop()
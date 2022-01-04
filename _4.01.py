from tkinter import*
klik=0
def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)
def klikker_minus(event):
    global klik
    klik-=1
    lbl.configure(text=klik)
def txt_to_lbl(event):
    #pass
    text_to_lbl=txt.get()#From Entry to text
    lbl.configure(text=text_to_lbl)
    txt.delete(0,END)
def valik():
    valik_=var.get()
    lbl.configure(text=valik_)
    txt.insert(0,valik_)
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("400x600")
nupp=Button(aken,text="Mina olen nupp\nValjutada mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)
#RAISED,SUNKEN,
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_minus)
knop=Button(aken,text="Nazjmi\nNa menja!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)
knop.bind("<Button-1>",klikker)
knop.bind("<Button-3>",klikker_minus)
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="lightblue",relief=GROOVE)
txt=Entry(aken,width=20,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt.bind("<Return>",txt_to_lbl)#enter

i1=PhotoImage(file="aaaa.gif")
i2=PhotoImage(file="aaaa.png")
i3=PhotoImage(file="yes.gif")
var=StringVar()
var.set("Üks")
r1=Radiobutton(aken,image=i1,variable=var, value="Üks",command=valik)
r2=Radiobutton(aken,image=i2,variable=var, value="Kaks",command=valik)
r3=Radiobutton(aken,image=i3,variable=var, value="Kolm",command=valik)


lbl.pack()
nupp.pack()#side=LEFT
txt.pack()
r1.pack()
r2.pack()
r3.pack()
knop.pack()

aken.mainloop()

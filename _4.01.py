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
aken=Tk()
aken.title("Akna nimetus")
aken.geometry("400x600")
nupp=Button(aken,text="Mina olen nupp\nValjutada mind!",font="Arial 20",fg="red",bg="lightblue",height=4,width=20,relief=GROOVE)
#RAISED,SUNKEN,
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker_minus)

lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="lightblue",relief=GROOVE)
txt=Entry(aken,width=20,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt.bind("<Return>",txt_to_lbl)#enter
r1=Radibutton(aken,)





lbl.pack()
nupp.pack(side=LEFT)#TOP,RIGHT
txt.pack()

aken.mainloop()

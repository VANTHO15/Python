from tkinter import *

def tiepAction():
    stringA.set("")
    stringB.set("")
    stringKQ.set("")
def giaiAction():
    a=float(stringA.get())
    b= float(stringB.get())
    if a==0 and b==0 :
        stringKQ.set("Vô số nghiệm")
    elif a==0 and b!=0:
        stringKQ.set("Vô nghiệm")
    else:
        stringKQ.set("x={0}".format(-b/a))
root=Tk()

stringA=StringVar()
stringB=StringVar()
stringKQ=StringVar()

root.title("PTB1")
root.resizable(height=True,width=True)
root.minsize(height=150,width=250)

Label(root,text="Phương Trình Bậc 1",fg="red",font=("tahoma",16),justify=CENTER).grid(row=0,columnspan=2)

Label(root,text="Hệ số a= ",font=("tahoma",10)).grid(row=1,column=0)
Entry(root,width=30,textvariable=stringA).grid(row=1,column=1)

Label(root,text="Hệ số b= ",font=("tahoma",10)).grid(row=2,column=0)
Entry(root,width=30,textvariable=stringB).grid(row=2,column=1)

frameButton=Frame()
Button(frameButton,text="GIẢI",command=giaiAction).pack(side=LEFT)
Button(frameButton,text="TIẾP",command=tiepAction).pack(side=LEFT)
Button(frameButton,text="THOÁT",command=root.quit).pack(side=LEFT)
frameButton.grid(row=3,columnspan=2)

Label(root,text="Kết Quả: ",font=("tahoma",10)).grid(row=4,column=0)
Entry(root,width=30,textvariable=stringKQ).grid(row=4,column=1)

def makecenter(root):
    root.update_idletasks()
    width=root.winfo_width()
    height=root.winfo_height()
    x=(root.winfo_screenwidth() // 2) - (width//2)
    y= (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry("{}x{}+{}+{}".format(width,height,x,y))
makecenter(root)
root.mainloop()
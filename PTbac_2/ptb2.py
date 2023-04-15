from math import sqrt
from tkinter import *

root=Tk()
root.title("PTB2")
root.resizable(height=True,width=True)
root.minsize(height=180,width=300)

a=StringVar()
b=StringVar()
c=StringVar()
kq=StringVar()
def function_tiep():
    a.set("")
    b.set("")
    c.set("")
    kq.set("")
def function_giai():
    a1=float(a.get())
    b1=float(b.get())
    c1=float(c.get())
    if a1==0:
        if b1==0:
            if c1==0:
                kq.set("Vô số nghiệm")
            else:
                kq.set("Vô nghiệm")
        else:
            x=-c1/b1
            kq.set("X1= {0}".format(x))
    else:
        d=b1**2-4*a1*c1
        if d<0:
            kq.set("Vô nghiệm")
        elif d==0:
            kq.set("X1=X2= {0}".format(-b1/(2*a1)))
        else:
            x1=(-b1+sqrt(d))/(2*a1)
            x2=(-b1-sqrt(d))/(2*a1)
            kq.set("X1= {0} ; X2= {1}".format(x1,x2))

# tiêu đề
Label(root,text="Phương Trình Bậc 2",fg="blue",font=("tahoma",16)).grid(row=0,columnspan=2)
# hệ số a
Label(root,text="Hệ số a:",font=("tahoma",13)).grid(row=1,column=0)
Entry(root,width=35,textvariable=a).grid(row=1,column=1)
# hệ số b
Label(root,text="Hệ số b:",font=("tahoma",13)).grid(row=2,column=0)
Entry(root,width=35,textvariable=b).grid(row=2,column=1)
# hệ số c
Label(root,text="Hệ số c:",font=("tahoma",13)).grid(row=3,column=0)
Entry(root,width=35,textvariable=c).grid(row=3,column=1)
# NÚT BẤM
frame_nut=Frame()
Button(frame_nut,text="TIẾP TỤC",background="yellow",width=7,command=function_tiep).pack(side=LEFT)
Button(frame_nut,text="GIẢI",background="#00FF00",width=7,command=function_giai).pack(side=LEFT)
Button(frame_nut,text="THOÁT",background="red",width=7,command=root.quit).pack(side=LEFT)# thêm  fill=X vapf trong pack cho dài đều các nút
frame_nut.grid(row=4,columnspan=2)
# kết quả
Label(root,text="KẾT QUẢ:",font=("tahoma",15),fg="red").grid(row=5,column=0)
Entry(root,width=35,textvariable=kq,bd = 5).grid(row=5,column=1)


def makecenter(root):
    root.update_idletasks()
    width=root.winfo_width()
    height=root.winfo_height()
    x=(root.winfo_screenwidth() // 2) - (width//2)
    y= (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry("{}x{}+{}+{}".format(width,height,x,y))
makecenter(root)
root.mainloop()


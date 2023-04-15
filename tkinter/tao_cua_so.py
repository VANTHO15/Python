from tkinter import *
root=Tk()
root.title("HELLO VANTHO15")
root.resizable(height=True,width=True)
root.minsize(height=300,width=500)

def makecenter(root):
    root.update_idletasks()
    width=root.winfo_width()
    height=root.winfo_height()
    x=(root.winfo_screenwidth() // 2) - (width//2)
    y= (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry("{}x{}+{}+{}".format(width,height,x,y))
makecenter(root)
root.mainloop()

import matplotlib.pyplot as pyplot
import matplotlib.animation as animation

fig=pyplot.figure()
ax1=fig.add_subplot(1,1,1)

def refreshInputdata(i):
    print("Refeshing data....")
    dulieu=open("dulieu.txt","r").read()
    lines=dulieu.split("\n")
    xvalue=[]
    yValue=[]
    for line in lines:
        if(len(line)>1):
            x,y=line.split(",")
            xvalue.append(x)
            yValue.append(y)
    ax1.clear()
    ax1.plot(xvalue,yValue,"o")

ani= animation.FuncAnimation(fig,refreshInputdata,interval=1000)
pyplot.show()
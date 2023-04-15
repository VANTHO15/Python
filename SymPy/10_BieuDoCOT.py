import matplotlib.pyplot as pyplot
x1value=[1,3,5,7,9]
y1value=[3,2,5,7,3]
pyplot.bar(x1value,y1value,width=0.5,label="This is Thọ",color="red")

x2value=[2,4,6,8,10]
y2value=[3,5,5,5,3]
pyplot.bar(x2value,y2value,width=0.5,label="This is Yến",color="blue")

pyplot.xlabel("Trục X")
pyplot.ylabel("Trục Y")
pyplot.title("Nguyễn văn Thọ \n Biểu đồ cột !")
pyplot.legend()
pyplot.show()


import matplotlib.pyplot as pyplot

mobie=["Apple","Samsung","Nokia","VanTho"]
Cat=[30,30,30,10]
colors=["red","blue","yellow","purple"]
explode=[0.05,0,0,0]
pyplot.pie(Cat,
           labels=mobie,
           colors=colors,
           startangle=0,
           explode=explode,
           autopct="%1.1f%%"
           )
pyplot.title("Nguyễn Văn Thọ \n Biểu đồ cột !")
pyplot.show()

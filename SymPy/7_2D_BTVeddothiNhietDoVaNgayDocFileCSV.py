import csv
from pylab import plot,show
days=[]
temps=[]
with open("nhietdo.csv",newline="",) as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        days.append(int(row[0]))
        temps.append(float(row[1]))

print(days)
print(temps)
plot(days,temps,"o")
show()
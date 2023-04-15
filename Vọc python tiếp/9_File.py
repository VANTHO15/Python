SoByteMoilanGhi=2500
rfile=open("../data/data.txt","r",encoding="utf-8")
wfile=open("../data/list.txt","w",encoding="utf-8")

buffer=rfile.read(SoByteMoilanGhi)
i=0
while(len(buffer)):
    i+=1
    wfile.write(buffer)
    print(i,"{0} byte ".format(len(buffer)))
    buffer=rfile.read(SoByteMoilanGhi)
print("Done")
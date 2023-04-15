def luufile(path,data):
    file=open(path,'a',encoding='utf-8')
    file.writelines(data)
    file.writelines("\n")
    file.close()
def docfile(path):
    arr2d=[]
    file=open(path,'r',encoding="utf-8")
    for line in file:
        data=line.strip()
        arr=data.split(";")
        arr2d.append(arr)
    file.close()
    return arr2d
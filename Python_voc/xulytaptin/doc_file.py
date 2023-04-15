def DocFile(path):
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data=line.strip()
        print(data)
    file.close()
DocFile("file.txt")
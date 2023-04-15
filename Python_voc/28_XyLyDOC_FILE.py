def DocFile():
    file=open("file.txt","r",encoding="utf-8")
    for i in file:
        print(i.strip())
    file.close()
DocFile()



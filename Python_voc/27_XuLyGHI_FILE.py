def LuuFile(path):
    file=open(path,"w",encoding="utf-8")  # w là ghi mới, a là ghi nối đuôi, r là đọc
    file.writelines("101180204;Nguyễn Văn Thọ;18CDT1\n")
    file.writelines("101180205;Nguyễn Văn A;18CDT1\n")
    file.writelines("101180206;Nguyễn Văn B;18CDT1\n")
    file.close()
LuuFile("file.txt")


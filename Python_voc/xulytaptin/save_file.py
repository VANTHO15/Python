def LuuFile(path):
    file=open(path,"w",encoding="utf-8")  #nếu là w thì mỗi lần nap code bị mất,còn là a thì viết vào nối tiếp
    file.writelines("101180204;nguyễn văn thọ;18CDT1\n")
    file.writelines("1911919119;huynh thị yến phi ;18QLMT\n")
    file.writelines("256423743;nguyễn Thị Bảo Yến;18Kx\n")
    file.close()
LuuFile("file.txt")